from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ProFitCreateForm
from cart.cart import Cart
from .tasks import cotizacion_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

#from Proyectos.models import Project,mantenimiento 
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.utils.translation import gettext_lazy as _
from .models import ProFit,Visit 
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar


from datetime import datetime, date
#from profixinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
#from profixinvoice.templates import SimpleInvoice



def cotizacion_create(request):

    if request.method == 'POST':
        form = ProFitCreateForm(request.POST)
        form.instance.usuario = request.user
        if  form.is_valid():
            coti = form.save(commit=False)
            coti.save()
            # launch asynchronous task
            cotizacion_created.delay(coti.id)
        
            # set the order in the session
            request.session['coti_id'] = coti.id
            # redirect for payment
            return redirect(reverse('payment:done'))
    else:
        form = ProFitCreateForm()
    return render(request,
                  'cotizaciones/profit/create.html',
                  {'form': form})



class CalendarView(generic.ListView):
    model = Visit
    template_name = 'cotizaciones/profit/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()