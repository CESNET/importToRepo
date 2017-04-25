from django.core.management.base import BaseCommand, CommandError

from importToRepo.models import Reaction


class Command(BaseCommand):
    help = 'Imports specified reaction from Open Enventory'

    def add_arguments(self, parser):
        parser.add_argument('reaction_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for reaction_id in options['reaction_id']:
            reaction = Reaction.objects.get(pk=reaction_id)

            self.stdout.write('Reaction id "%s"' % reaction.reaction_carried_out_by)

        self.stdout.write(self.style.SUCCESS('Successfully imported reaction "%s"'))