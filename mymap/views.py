from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import buildmap

def buildmap(request):
    return osm

#def hello(request):
    #return HttpResponse("Hello, world. You're at the hello.")


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .forms import handle_uploaded_file
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = handle_uploaded_file(request.FILES['file'])
            return render(request, 'mymap/success.html', {'file' : file})
    else:
        form = UploadFileForm()
    return render(request, 'mymap/upload.html', {'form': form})
