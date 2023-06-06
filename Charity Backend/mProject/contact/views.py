from django.shortcuts import render
from news.models import subscribeList
from .models import contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        if 'name' in request.POST and 'mail' in request.POST and 'number' in request.POST and 'sms' in request.POST:
            name = request.POST['nam']
            mail = request.POST['mal']
            number = request.POST['nmb']
            sms = request.POST['sms']
            cBook = contact(name=name, mail=mail, number=number, sms=sms)
            cBook.save()
        elif 'subsMail' in request.POST:
            mail = request.POST['subsMail']
            sbook = subscribeList(mail=mail)
            sbook.save()

    return render(request, 'contact/contact.html')
