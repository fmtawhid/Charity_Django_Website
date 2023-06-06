from django.shortcuts import render
from . models import donarList
from news.models import subscribeList

# Create your views here.
def donate(request):

    #DonarList Form View
    if request.method== 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        numb = request.POST['number']

        newBook =donarList(name = name, mail = mail, number=numb)
        newBook.save()



    #Subscribe Form View
    if request.method=='post':
        mail = request.post['subsMail']
        sbook =subscribeList(mail = mail)
        sbook.save()

    return render(request, 'donate/donate.html', )

