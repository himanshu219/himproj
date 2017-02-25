import csv
import traceback
from optparse import make_option

import unicodedata
from django.core.management import BaseCommand
from himapp.models import Company, Director, Country, City, Subcategory, State, Category, DirectorCompany


def normalize_name(name, is_capitalize=False, isNull=False):
    name = name.strip()
    if name:
        if is_capitalize:
            name = name.upper()
        return unicode(name)
    else:
        return u'NA' if not isNull else None

def create_company(company, is_commit):
    print "creating Company  : %s" % (company[0])
    country, _ = Country.objects.get_or_create(name=normalize_name(company[12],True))
    state, _ = State.objects.get_or_create(name=normalize_name(company[10],True), country=country)
    city, _ = City.objects.get_or_create(name=normalize_name(company[10],True), state=state, country=country)
    category, _ = Category.objects.get_or_create(name = normalize_name(company[2], True))
    subcategory, _ = Subcategory.objects.get_or_create(name = normalize_name(company[3], True), category=category)
    company_data = {
        "cin":normalize_name(company[0],True),
        "company_name": normalize_name(company[1]),
        "status":normalize_name(company[17], True),
        "subcategory_id":subcategory.id,
        "type":normalize_name(company[4], True),
        "authorised_capital":company[5],
        "paidup_capital":company[6],
        "incorporation_date":company[7],
        "agm_date":company[15] if company[15] else None,
        "balancesheet_date":company[16] if company[16] else None,
        "address1":normalize_name(company[8], False,True),
        "address2":normalize_name(company[9], False,True),
        "full_address":normalize_name(company[14],False,True),
        "city_id": city.id,
        "pincode":normalize_name(company[13],False,True)
    }
    company, _ = Company.objects.get_or_create(**company_data)
    return company


def create_director(director, is_commit):
    print "creating Director : %s" % (director[0])
    director, _ = Director.objects.get_or_create(din = normalize_name(director[0], True), name = normalize_name(director[1], True))
    return director


class Command(BaseCommand):
    """
        this script should be run after adding new state in admin
    """

    option_list = BaseCommand.option_list + (
        make_option('-c', '--commit', dest='commit', action='store_true', default=False, help='saves changes in db'),
    )


    def handle(self, *args, **options):
        """
            8 CIN,Company Name,Category,Subcategory,Type,Authorized Capital,Paidup Capital,IncorporationDate,
            10 Address Line 1,Address Line 2,City,State,Country,PIN,Full Address,AGM Date,Balance Sheet Date,Status,
            4 DIN,Name,Designation,Appointment Date,
            nonmandatory Address Line 1,Address Line 2,City,PIN,full address,agmdate,balancesheetdate, capitalize, strip
        """
        is_commit = options.get('commit', False)

        FILE_NAME = "/home/darkknight/development/himproj/company_data.csv"
        COL_NO = 17
        DIR_FIELDS_LENGTH = 4
        try:
            with open(FILE_NAME, 'r') as f:
                next(f)#for skipping header
                reader = csv.reader(f)
                for row in reader:
                    company = row[:COL_NO+1]
                    directors = row[COL_NO+1:]
                    all_directors = []
                    # import pdb;pdb.set_trace()
                    company = create_company(company, is_commit)
                    for dr in xrange(0,len(directors), DIR_FIELDS_LENGTH):
                        director_data = directors[dr:dr+DIR_FIELDS_LENGTH]
                        director = create_director(director_data, is_commit)
                        DirectorCompany.objects.get_or_create(director=director,company=company, designation=normalize_name(director_data[2],True), appointment_date=director_data[3])
        except Exception as e:
            print "Error", str(e), traceback.format_exc()
