from celery import Celery
from django.core.mail import send_mail
from .models import ProFit

app=Celery()

@app.task
def cotizacion_created(coti_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """
    coti = ProFit.objects.get(id=coti_id)
    subject = 'Cotización nr. {}'.format(coti.id)
    message = 'Querido Promain {},\n\nYou have successfully placed an order.\
                  Your order id is {}.'.format(coti.activity,
                                            coti.id)
    mail_sent = send_mail(subject,
                          message,
                          'presidencia@profixgroup.io',
                          'presidencia@profixgroup.io')
    return mail_sent
