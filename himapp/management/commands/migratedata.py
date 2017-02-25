import csv
import traceback
from optparse import make_option
from django.core.management import BaseCommand

class Command(BaseCommand):
    """
        this script should be run after adding new state in admin
    """

    option_list = BaseCommand.option_list + (
        make_option('-c', '--commit', dest='commit', action='store_true', default=False, help='saves changes in db'),
    )


def handle(self, *args, **options):

    is_commit = options.get('commit', False)

    FILE_NAME = "/home/darkknight/development/himproj/company_data.csv"

    try:
        with open(FILE_NAME, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print row
    except Exception as e:
        print "Error", str(e), traceback.format_exc()

