from django import forms

class UploadFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

def handle_uploaded_file(f):
    with open('mymap/a.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
