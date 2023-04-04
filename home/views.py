from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

from django.shortcuts import render
from .models import Jewelry, JewelryPrice


def jewellery(request):
    jewelry_items = Jewelry.objects.all()
    prices = JewelryPrice.objects.all()
    context = {
        'jewelry_items': jewelry_items,
        'prices': prices,
    }
    return render(request, 'home/jewellery.html', context)

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        contact.save()
        HttpResponseRedirect('thankyou for contacting')
          # Redirect to a thank you page

    return render(request, 'home/contact.html')



def about(request):
    return render(request, 'home/about.html')