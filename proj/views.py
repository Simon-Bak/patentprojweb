from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import URL
from .forms import URLForm
from django.shortcuts import redirect
from django.http import HttpResponse
from . import patent
from . import demo
import json

# Create your views here.
def index(request):
    return render(request, 'proj/index.html')

def main(request):
    return render(request, 'proj/main.html')

def info(request):
    return render(request, 'proj/tech.html')

def demourl(request):
    if request.method == "POST":
        word0 = request.POST['word0']
        word1 = request.POST['word1']
        word2 = request.POST['word2']
        wordandor01 = request.POST['wordandor01']
        wordandor02 = request.POST['wordandor02']
        
        status = request.POST['status']
        country = request.POST['country']

        person0 = request.POST['person0']
        person1 = request.POST['person1']
        person2 = request.POST['person2']
        personandor1 = request.POST['personandor0']
        personandor2 = request.POST['personandor1']

        return render(request, 'proj/index.html')

    return render(request, 'proj/demourl.html')

def demo(request):
    return render(request, 'proj/index.html')

def test(request):
    patentlist = demo.filetoList()
    testvalue = demo.GrantYear(patentlist)
    imageName = demo.grantYearGraph(testvalue)
    imageName = 'img/'+ imageName
    tests = {
        'url' : "{% static" + imageName + "%}"
    }
    return HttpResponse(json.dumps(tests), content_type='application/json')
   
