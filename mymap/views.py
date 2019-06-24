from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mymap.buildmap import buildmap

#def buildmap(request):
#    return osm

#def hello(request):
    #return HttpResponse("Hello, world. You're at the hello.")


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
#from .forms import handle_uploaded_file
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def handle_uploaded_file(f):
    file_name = f.name
    file_save = 'mymap/upload/' + file_name
    with open(file_save, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f)
            buildmap()
        return render(request, 'mymap/map.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'mymap/upload.html', {'form': form})
