from django import forms

class UploadFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

def handle_uploaded_file(f):
    file_name = f.name
    file_save = 'mymap/upload/' + file_name
    with open(file_save, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
