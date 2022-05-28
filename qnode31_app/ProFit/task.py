from celery import Celery
from django.core.mail import send_mail
from .models import UserRequest

app=Celery()

@app.task
def User_Request(requester_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """
    requester = UserRequest.objects.get(id=requester_id)
    subject = 'Solicitud de registro. {}'.format(requester.id)
    message = 'Gracias por solicitar una cuenta de usuraio para el edificio. {} en el sistema de ProFix IT. Un acesor comercial se \
    comunicará con usted en los proximos minuto. '.format(requester.edificio)
    
    mail_sent = send_mail(subject,
                          message,
                          'smartquail.info@gmail.com',
                          [requester.email])
    return mail_sent
