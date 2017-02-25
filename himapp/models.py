from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, validate_integer
from django.utils.text import slugify

from .choices import COMPANY_TYPE, COMPANY_STATUS


class BasicConfigurationField(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    show_on_site = models.BooleanField(default=True)
    modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BasicConfigurationField, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class City( BasicConfigurationField ):
    """ Stores all the City details. """

    country = models.ForeignKey( 'Country' )#this is to reduce queries
    state = models.ForeignKey( 'State', blank = True, null = True )


    class Meta:
        ordering = ['name']
        app_label = 'himapp'


class State( BasicConfigurationField ):
    """ Stores all the States details. State to Country Mapping. """

    country = models.ForeignKey( 'Country' )


    class Meta:
        ordering = ['name']
        app_label = 'himapp'

class Country( BasicConfigurationField ):
    """ Stores all the Country Details. """



    class Meta:
        app_label = 'himapp'


class Category(BasicConfigurationField):
    """ Holds  Category relevant data. """



    class Meta:
        app_label = 'himapp'


class Subcategory(BasicConfigurationField):
    """ Holds  Subcategory relevant data. Mapping to Category. """

    category = models.ForeignKey(Category)


    class Meta:
        app_label = 'himapp'


class Director(BasicConfigurationField):
    din = models.CharField(unique=True, max_length=25)

    def __unicode__(self):
        return "%s : %s" % (self.name, str(self.din))

class Company(models.Model):
    cin = models.CharField(unique=True, max_length=25)
    company_name = models.CharField(max_length=100)

    slug = models.SlugField(max_length=100, blank=True)
    status = models.CharField(max_length=25)
    modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    # category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(Subcategory)
    type = models.CharField(max_length=25)
    authorised_capital = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    paidup_capital = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    incorporation_date = models.DateField()
    agm_date = models.DateField(null=True, blank=True)
    balancesheet_date = models.DateField(null=True, blank=True)
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    full_address = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City)
    pincode = models.PositiveIntegerField(null=True, blank=True)
    alldirectors = models.ManyToManyField(Director, through="DirectorCompany")

    def __unicode__(self):
        return "%s : %s" % (self.cin, self.company_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.company_name)
        super(Company, self).save(*args, **kwargs)


class DirectorCompany(models.Model):
    company = models.ForeignKey(Company)
    director = models.ForeignKey(Director)
    designation = models.CharField(max_length=50)  # make it fk or not
    appointment_date = models.DateField()
    modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

