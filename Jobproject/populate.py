import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Jobproject.settings')
import django
django.setup()

from modelapp.models import HydJobs,BngJobs,PuneJobs
from faker import Faker
from random import *
fake=Faker()
def phonenumber():
    d1 =randint(6,9)
    num =''+str(d1)
    for i in range(9):
            num +=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','HR','Associate Engineer'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumber()
        hyd_jobs_records=HydJobs.objects.get_or_create(
                        date=fdate,
                        company=fcompany,
                        title=ftitle,
                        address=faddress,
                        email=femail,
                        phonenumber=fphonenumber,
        )
        bng_jobs_records = BngJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
        pune_jobs_records = PuneJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Record inserted successfully......')