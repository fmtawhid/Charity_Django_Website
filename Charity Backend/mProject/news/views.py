from django.shortcuts import render
from .models import subscribeList
from donate.models import donarList
# Create your views here.
def news(request):
    if request.method == 'POST':
        mail = request.POST['subsMail']
        sbook = subscribeList(mail=mail)
        sbook.save()
    return render(request, 'news/news.html')

 