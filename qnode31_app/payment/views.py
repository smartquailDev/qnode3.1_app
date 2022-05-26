import braintree
from django.shortcuts import render, redirect, get_object_or_404 
from ordenes_servicios.models import Order 
from .models import Check_Payment
from .forms import CheckForm,TransForm
from cart.cart import Cart
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()

            # create invoice e-mail
            subject = 'My Shop - Invoice no. {}'.format(order.id)
            message = 'Please, find attached the invoice for your recent purchase.'
            email = EmailMessage(subject,
                                 message,
                                 'presidencia@profixgroup.io',
                                 [order.email])

            # generate PDF
            html = render_to_string('orders/order/pdf.html', {'order': order})
            out = BytesIO()
            stylesheets=[weasyprint.CSS('static/css/pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out,
                                                   stylesheets=stylesheets)
            # attach PDF file
            email.attach('order_{}.pdf'.format(order.id),
                         out.getvalue(),
                         'application/pdf')
            # send e-mail
            email.send()

            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token 
        client_token = braintree.ClientToken.generate()
        return render(request, 
                      'payment/process.html', 
                      {'order': order,
                       'client_token': client_token})



def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')



def payment_check_process(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            check = form.save()

        return render(request, 
                      'payment/payment_check.html', 
                      {'check': check})

    else:
        form = CheckForm() 
    return render(request, 'payment/payment_check.html',{'form':form})

def payment_trans_process(request):
    if request.method == 'POST':
        form = TransForm(request.POST)
        if form.is_valid():
            check = form.save()

        return render(request, 
                      'payment/payment_trans.html', 
                      {'trans': trans})

    else:
        form = TransForm() 
    return render(request, 'payment/payment_trans.html',{'form':form})


