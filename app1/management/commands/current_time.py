from django.core.management.base import BaseCommand
import datetime

class Command(BaseCommand):
    help = 'Display current time'

    def handle(self, *args, **kwargs):
        time = datetime.datetime.now().strftime("%H:%M:%S %d-%b-%Y")
        return f'Its now {time}'
