from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from fedoralink.authentication.as_user import as_admin
from fedoralink.models import get_or_create_object
from importToRepo.importReaction import ImportReaction
from uoch.models import InstitutionsCollection, Institution


class Command(BaseCommand):
    help = 'Imports specified reaction from Open Enventory'

    def add_arguments(self, parser):
        parser.add_argument('reaction_id', nargs='+', type=int)

    def handle(self, *args, **options):
        with as_admin():
            import_object = ImportReaction()
            self.create_uoch_institution()


            for reaction_id in options['reaction_id']:
                import_object.import_reaction(reaction_id, User.objects.get(username = "admin"))

                self.stdout.write(self.style.SUCCESS('Successfully imported reaction "%s"' %reaction_id))

            self.stdout.write(self.style.SUCCESS('Import finished succesfully.'))

    def create_uoch_institution(self):
        object = get_or_create_object(({'name': "institutions", 'slug': "institutions", 'flavour': InstitutionsCollection},
                              {'name': "UCT Prague", 'slug': "uct-prague", "flavour": Institution},
                              {'name': "Department of Organic Chemistry", "slug": "uoch", "flavour": Institution}))
        object.save()

