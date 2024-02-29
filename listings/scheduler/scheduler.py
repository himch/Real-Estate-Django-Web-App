from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys

from loader.load_alnair_realty import load_alnair_realty
from modules.services.contacts_to_excel_file import contacts_to_excel_file


def start():
    return
    scheduler = BackgroundScheduler()

    scheduler.add_jobstore(DjangoJobStore(), alias="default")
    scheduler.remove_jobstore(alias="default")
    scheduler.add_jobstore(DjangoJobStore(), alias="default")
    scheduler.remove_all_jobs(jobstore="default")
    job = scheduler.add_job(contacts_to_excel_file, 'interval', minutes=1, name='contacts_to_excel_file', jobstore='default', replace_existing=True)
    # job = scheduler.add_job(load_alnair_realty, 'interval', hours=24, name='load_alnair_realty', jobstore='default', replace_existing=True)
    scheduler.start()
    print("Scheduler started...")
