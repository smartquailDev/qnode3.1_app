from celery import Celery
from django.core.mail import send_mail
from .models import Edificios


app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )




@app.task
def building_created(edificio_id):
    """
    Task to send an e-mail notification when an building is
    successfully register.
    """
    edificio = Edificios.objects.get(id=edificio_id)
    subject = 'Edificio :{}'.format(edificio.building_name)
    message = 'ProFix Sistems {},\n\n Se ha registrado un edificio de Home Detail en el sistema ProFix.'
    mail_sent = send_mail(subject,
                          message,
                          'profixmainhousing@gmail.com',
                          [edificio.administrator_email])
    return mail_sent

@app.task
def cotizacion_created(cotizacion_id):
    """
    Task to send an e-mail notification when an building is
    successfully register.
    """
    cotizacion = cotizacion.objects.get(id=cotizacion_id)
    subject = 'Cotizacion Realizada del proyecto :{}'.format(cotizacion.project_name)
    message = 'ProFix Sistems {},\n\n Se ha cotizado exitosamente el proyecto  en el sistema ProFix.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [administrator_email.email])
    return mail_sent
