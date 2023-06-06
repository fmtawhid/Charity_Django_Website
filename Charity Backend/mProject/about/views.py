from django.shortcuts import render
from news.models import subscribeList
# Create your views here.
def about(request):
        if request.method=='POST':
            mail = request.POST['subsMail']
            sBook =subscribeList(mail = mail)
            sBook.save()
        return render(request, 'about/about.html')

