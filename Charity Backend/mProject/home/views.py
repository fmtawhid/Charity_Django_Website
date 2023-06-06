from django.shortcuts import render
from donate.models import donarList
from news.models import subscribeList

def home(request):
    if request.method == 'POST':
        if 'name' in request.POST and 'mail' in request.POST and 'number' in request.POST:
            name = request.POST['name']
            mail = request.POST['mail']
            numb = request.POST['number']
            newBook = donarList(name=name, mail=mail, number=numb)
            newBook.save()
        elif 'subsMail' in request.POST:
            mail = request.POST['subsMail']
            sbook = subscribeList(mail=mail)
            sbook.save()

    return render(request, 'home/index.html')



