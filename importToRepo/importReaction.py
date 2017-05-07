import datetime
import io
import re

import unicodedata

from fedoralink.models import get_or_create_object
from fedoralink.utils import TypedStream
from importToRepo.models import Reaction, ProjectPerson, ReactionChemical
from uoch.models import LabJournalsCollection, LabJournal, ProjectsCollection, Project, InstitutionsCollection, \
    Institution, ScientistsCollection, ScientistPerson, ChemicalsCollection, Chemical, ChemicalInReaction, \
    SourceDataCollection, SourceData, Image, File
from uoch.models import Reaction as ReactionObject
from tzlocal import get_localzone


class ImportReaction:
    def import_reaction(self, reaction_id, user):
        reaction = Reaction.objects.get(reaction_id=reaction_id)
        self.create_lab_journal(reaction, user)
        self.create_project(reaction, user)
        reaction_object = self.create_reaction(reaction)
        reaction_object.rxnImage = self.create_reaction_image(reaction.lab_journal, reaction)
        reaction_object.save()

        self.create_chemicals(reaction)

        print('Reaction "%s" is being imported' % reaction.reaction_id)

        return False

    def create_reaction(self, reaction):
        lab_journal = reaction.lab_journal
        reaction_object = get_or_create_object(
            ({'name': "Laboratory Journals", 'slug': "lab-journals", 'flavour': LabJournalsCollection},
             {'name': lab_journal.lab_journal_code, 'slug': ImportReaction.create_slug(lab_journal.lab_journal_code),
              "flavour": LabJournal},
             {'name': self.get_reaction_title(reaction), 'slug': ImportReaction.create_slug(self.get_reaction_title(reaction)), "flavour": ReactionObject}
             ))

        reaction_object.save()
        return reaction_object

    def create_lab_journal(self, reaction, user):
        lab_journal = reaction.lab_journal
        object = get_or_create_object(
            ({'name': "Laboratory Journals", 'slug': "lab-journals", 'flavour': LabJournalsCollection},
             {'name': lab_journal.lab_journal_code, 'slug': ImportReaction.create_slug(lab_journal.lab_journal_code),
              "flavour": LabJournal}))
        object.openEnventoryId = str(lab_journal.lab_journal_id)
        object.labJournalCode = lab_journal.lab_journal_code
        object.creationDate = lab_journal.lab_journal_created_when
        object.changedDate = lab_journal.lab_journal_changed_when
        if not object.dateSubmitted:
            object.dateSubmitted = datetime.datetime.now(tz=get_localzone())
        if not object.dateAvailable:
            object.dateAvailable = datetime.datetime.now(tz=get_localzone())
        if user.get_full_name():
            user_full_name = user.get_full_name()
        else:
            user_full_name = user.username
        object.creator = user_full_name
        object.save()

    def create_project(self, reaction, user):
        project = reaction.project
        object = get_or_create_object(({'name': "Projects", "slug": "projects", 'flavour': ProjectsCollection},
                                       {'name': project.project_name, "slug":
                                           ImportReaction.create_slug(project.project_name), 'flavour': Project}))
        object.abstract = project.project_text
        object.openEnventoryId = str(project.project_id)

        institution = get_or_create_object(
            ({'name': "institutions", 'slug': "institutions", 'flavour': InstitutionsCollection},
             {'name': "UCT Prague", 'slug': "uct-prague", "flavour": Institution},
             {'name': "Department of Organic Chemistry", "slug": "uoch", "flavour": Institution}))
        object.institutions = [institution]
        object.collaborators = self.create_scientists(project)
        if not object.dateSubmitted:
            object.dateSubmitted = datetime.datetime.now(tz=get_localzone())
        if not object.dateAvailable:
            object.dateAvailable = datetime.datetime.now(tz=get_localzone())
        if not user.get_full_name():
            user_full_name = user.username
        else:
            user_full_name = user.get_full_name()
        object.creator = user_full_name
        object.save()
        return object

    def create_scientists(self, project):
        project_persons = ProjectPerson.objects.filter(project=project)
        scientists = []
        for project_person in project_persons:
            person = project_person.person
            scientist = get_or_create_object(
                ({'name': "Scientists", 'slug': "scientists", 'flavour': ScientistsCollection},
                 {'name': person.get_fullname(), 'slug': ImportReaction.create_slug(person.get_fullname()),
                  "flavour": ScientistPerson}))
            scientist.firstName = person.first_name
            scientist.surname = person.last_name
            scientist.titles = person.title
            scientist.email = person.email
            scientist.changedDate = person.person_changed_when
            scientist.openEnventoryId = str(person.person_id)
            scientist.save()

            scientists.append(scientist)
        return scientists

    def create_chemicals(self, reaction):
        reaction_chemicals = ReactionChemical.objects.filter(reaction=reaction)

        for chemical in reaction_chemicals:
            chemical_in_reaction_object = self.create_chemical_in_reaction(chemical, reaction=reaction,
                                                                           lab_journal=reaction.lab_journal)

    def create_chemical_in_reaction(self, chemical, lab_journal, reaction):
        title = self.get_chemical_title(chemical)
        chemical_in_reaction_object = ChemicalInReaction.objects.filter(openEnventoryId=chemical.reaction_chemical_id).first()
        if not chemical_in_reaction_object:
            chemical_in_reaction_object = get_or_create_object(
                ({'name': "Laboratory Journals", 'slug': "lab-journals", 'flavour': LabJournalsCollection},
                 {'name': lab_journal.lab_journal_code,
                  'slug': ImportReaction.create_slug(lab_journal.lab_journal_code),
                  "flavour": LabJournal},
                 {'name': self.get_reaction_title(reaction), 'slug': ImportReaction.create_slug(self.get_reaction_title(reaction)),
                  "flavour": ReactionObject},
                 {'name': title, 'slug': ImportReaction.create_slug(title),
                  "flavour": ChemicalInReaction}
                 ))
            chemical_in_reaction_object.save()

        chemical_in_reaction_object.update()

        if chemical.molecule and not chemical_in_reaction_object.chemical:
            chemical_in_reaction_object.chemical = self.create_chemical(chemical)
        chemical_in_reaction_object.save()

        chemical_in_reaction_object.roleInReaction = chemical.role
        chemical_in_reaction_object.amount = str(chemical.rc_amount)
        chemical_in_reaction_object.amountUnit = chemical.rc_amount_unit
        chemical_in_reaction_object.stochasticCoeficient = str(chemical.stoch_coeff)
        chemical_in_reaction_object.concentration = str(chemical.rc_conc)
        chemical_in_reaction_object.concentrationUnit = chemical.rc_conc_unit
        chemical_in_reaction_object.weight = str(chemical.m_brutto)
        chemical_in_reaction_object.weightUnit = chemical.mass_unit
        chemical_in_reaction_object.volume = str(chemical.volume)
        chemical_in_reaction_object.volumeUnit = chemical.volume_unit
        chemical_in_reaction_object.yieldField = str(chemical.yield_field)
        chemical_in_reaction_object.measured = chemical.measured
        chemical_in_reaction_object.openEnventoryId = str(chemical.reaction_chemical_id)

        chemical_in_reaction_object.save()
        return chemical_in_reaction_object

    def create_chemical(self, chemical):
        title = self.get_chemical_title(chemical)
        chemical_object = None
        if chemical.molecule:
            chemical_object = Chemical.objects.filter(openEnventoryId=chemical.molecule.molecule_id).first()
            return chemical_object
        if not chemical_object:
            chemical_object = get_or_create_object(
                ({'name': "Chemicals", 'slug': "chemicals", 'flavour': ChemicalsCollection},
                 {'name': title, 'slug': ImportReaction.create_slug(title), "flavour": Chemical}
                 ))
            chemical_object.save()
        chemical_object.update()

        chemical_object.dateChanged = chemical.reaction_chemical_changed_when
        chemical_object.casNumber = chemical.cas_nr
        chemical_object.SMILES = chemical.smiles
        chemical_object.INCHI = chemical.inchi
        chemical_object.empFormula = chemical.emp_formula
        chemical_object.molecularWeight = str(chemical.mw)
        if chemical.molecule:
            chemical_object.openEnventoryId = str(chemical.molecule.molecule_id)
        # chemical_object.spectroscopyPureCompound
        chemical_object.chemicalStructure= self.create_chemical_structure(chemical, title)
        chemical_object.molFile = self.create_source_data(blob=chemical.molfile_blob,
                                                          source_data_title=title + ' mol file',
                                                          date_changed=chemical.reaction_chemical_changed_when,
                                                          role="Mol file")
        chemical_object.save()
        return chemical_object

    def get_chemical_title(self, chemical):
        title = ''
        if (chemical.standard_name):
            title = chemical.standard_name
        else:
            if (chemical.emp_formula):
                title = chemical.emp_formula
            else:
                title = str(chemical.molecule.molecule_id)
        return title

    def get_reaction_title(self, reaction):
        title = ''
        if (reaction.reaction_title):
            title = reaction.reaction_title
        else:
            title = str(reaction.reaction_id)
        return title

    def create_source_data(self, blob, source_data_title, date_changed, role):
        source_data = get_or_create_object(({'name': "Source Data", 'slug': "source-data", 'flavour': SourceDataCollection},
                              {'name': source_data_title, 'slug': ImportReaction.create_slug(source_data_title),
                               "flavour": SourceData}))
        source_data.save()
        source_data.dateChanged = date_changed
        source_data.blob = self.create_source_data_blob(source_data_title, blob)
        source_data.role = role
        source_data.save()
        return source_data

    def create_source_data_blob(self, source_data_title, blob):
        source_data_blob = get_or_create_object(
            ({'name': "Source Data", 'slug': "source-data", 'flavour': SourceDataCollection},
             {'name': source_data_title, 'slug': ImportReaction.create_slug(source_data_title),
              "flavour": SourceData},
             {'name': source_data_title + ' blob', 'slug': ImportReaction.create_slug(source_data_title+' blob'),
              "flavour": File}))
        source_data_blob.save()
        data = self.DataStream(io.BytesIO(blob))
        source_data_blob.set_local_bitstream(data)
        source_data_blob.save()
        return source_data_blob

    def create_chemical_structure(self, chemical, title):
        image_object = get_or_create_object(
            ({'name': "Chemicals", 'slug': "chemicals", 'flavour': ChemicalsCollection},
             {'name': title, 'slug': ImportReaction.create_slug(title), "flavour": Chemical},
             {'name': title + ' structure', 'slug': ImportReaction.create_slug(title + ' structure'), "flavour": Image}
             ))
        data = self.DataStream(io.BytesIO(chemical.gif_file), 'image/gif')
        image_object.set_local_bitstream(data)
        image_object.save()
        return image_object

    def create_reaction_image(self, lab_journal, reaction):
        image_object = get_or_create_object(
            ({'name': "Laboratory Journals", 'slug': "lab-journals", 'flavour': LabJournalsCollection},
             {'name': lab_journal.lab_journal_code,
              'slug': ImportReaction.create_slug(lab_journal.lab_journal_code),
              "flavour": LabJournal},
             {'name': self.get_reaction_title(reaction),
              'slug': ImportReaction.create_slug(self.get_reaction_title(reaction)),
              "flavour": ReactionObject},
             {'name': self.get_reaction_title(reaction)+'_equation', 'slug': ImportReaction.create_slug(self.get_reaction_title(reaction)+'_equation'),
              "flavour": ChemicalInReaction}
             ))
        data = self.DataStream(io.BytesIO(reaction.rxn_gif_file), 'image/gif')
        image_object.set_local_bitstream(data)
        image_object.save()
        return image_object

    @staticmethod
    def create_slug(s):
        s = ImportReaction.strip_accents(s)
        return re.sub('[^a-zA-Z0-9]', '', s)

    @staticmethod
    def strip_accents(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')

    class DataStream:
        stream = None
        mimetype = ''
        filename = ''

        def __init__(self, stream, mimetype='application/octet-stream', filename = 'blob'):
            self.stream = stream
            self.mimetype = mimetype
            self.filename = filename
