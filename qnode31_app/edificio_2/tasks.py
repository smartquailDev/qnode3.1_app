from celery import Celery
from django.core.mail import send_mail
from .models import Coti_Order

app=Celery()

@app.task
def coti_order_created(coti_order_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """
    order = Coti_Order.objects.get(id=coti_order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                  Your order id is {}.'.format(order.first_name,
                                            order.id)
    mail_sent = send_mail(subject,
                          message,
                          'presidencia@profixgroup.io',
                          [order.email])
    return mail_sent