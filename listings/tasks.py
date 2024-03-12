from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from realestate.celery import app
from datetime import datetime


# for start - run:
# celery -A realestate worker --beat --loglevel=debug

@app.task
def load_alnair_realty():
    print('Update Alnair realty database started at ' + str(datetime.now()))
    try:
        pass
        return {"status": True, "message": f"Alnair realty database updated successfully"}
    except Exception as e:
        return {"status": False, "Error load_alnair_realty, message": str(e)}


@app.task
def load_airbnb_offer():
    print('Load Airbnb offer started at ' + str(datetime.now()))
    try:
        pass
        return {"status": True, "message": f"Airbnb offer loaded successfully"}
    except Exception as e:
        return {"status": False, "Error load_airbnb_offer, message": str(e)}


@app.task
def create_and_send_contacts_xlsx_report():
    print('Contacts xlsx report sending started at ' + str(datetime.now()))
    try:
        pass
        return {"status": True, "message": f"Contacts xlsx report sent successfully"}
    except Exception as e:
        return {"status": False, "Error create_and_send_contacts_xlsx_report, message": str(e)}


@app.task
def send_reg_email():
    print('Reg email sending started at ' + str(datetime.now()))
    try:
        pass
        return {"status": True, "message": f"Reg email sent successfully"}
    except Exception as e:
        return {"status": False, "Error send_reg_email, message": str(e)}

#
# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=10,
#     period=IntervalSchedule.SECONDS,
# )
#
# print('app.conf.beat_schedule', app.conf.beat_schedule)
#
# app.conf.beat_schedule = {
#     'Import_Data_3': {
#         'task': 'listings.tasks.run_load',
#         'schedule': schedule,
#     },
# }
#
# print('app.conf.beat_schedule', app.conf.beat_schedule)
#
#

# task, created = PeriodicTask.objects.get_or_create(
#     name='Import_Data_2',
#     defaults={'task': 'listings.tasks.run_load', 'interval': schedule}
# )

