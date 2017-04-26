import datetime

from fedoralink.models import get_or_create_object
from importToRepo.models import Reaction
from uoch.models import LabJournalsCollection, LabJournal
from tzlocal import get_localzone


class ImportReaction:
    def import_reaction(self, reaction_id, user):
        reaction = Reaction.objects.get(pk=reaction_id)
        self.create_lab_journal(reaction, user)

        print('Reaction "%s" is being imported' % reaction.reaction_id)

        return False

    def create_lab_journal(self, reaction, user):
        lab_journal = reaction.lab_journal
        object = get_or_create_object(
            ({'name': "Laboratory Journals", 'slug': "lab-journals", 'flavour': LabJournalsCollection},
             {'name': lab_journal.lab_journal_code, 'slug': lab_journal.lab_journal_code, "flavour": LabJournal}))
        object.openEnventoryId = str(lab_journal.lab_journal_id)
        object.labJournalCode = lab_journal.lab_journal_code
        object.creationDate = lab_journal.lab_journal_created_when
        object.changedDate = lab_journal.lab_journal_changed_when
        if not object.dateSubmitted:
            object.dateSubmitted = datetime.datetime.now(tz=get_localzone())
        if not object.dateAvailable:
            object.dateAvailable = datetime.datetime.now(tz=get_localzone())
        if not user.get_full_name():
            user_full_name=user.username
        else:
            user_full_name=user.get_full_name()
        object.creator = user_full_name
        object.save()