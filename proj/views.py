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
URL = ''
def index(request):
    return render(request, 'proj/index.html')

def main(request):
    return render(request, 'proj/main.html')

def info(request):
    return render(request, 'proj/tech.html')

def demo(request):
    return render(request, 'proj/demo.html')

def testurl(request):
    if request.method == "POST":
        name = request.POST['name']

        if name == 'AR':
            name = 'AR'
        elif name == 'VR':
            name = 'VR'
        elif name == "GPU":
            name = 'GPU'
        request.session['URL'] = name
        return redirect('result')

    return render(request, 'proj/testurl.html')

def result(request):
    name = request.session['URL']
    plist = patent.filetoList(name)

    portName = patent.Portfolio(plist)
    grantyear = patent.GrantYear(plist)
    grantperson = patent.GrantPerson(plist)

    yearimageName = patent.grantYearGraph(grantyear)
    personimageName = patent.grantPersonGraph(grantperson, 5)
    portName = 'img/' + portName
    return render(request, 'proj/result.html',{'URL' : URL, 'portsrc':portName,})

def test(request):
    patentlist = demo.filetoList()
    testvalue = demo.GrantYear(patentlist)
    imageName = demo.grantYearGraph(testvalue)  
    imageName = 'img/'+ imageName
    tests = {
        'url' : "{% static" + imageName + "%}"
    }
    return HttpResponse(json.dumps(tests), content_type='application/json')
   
