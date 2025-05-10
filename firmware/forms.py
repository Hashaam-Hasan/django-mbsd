from django import forms

class FirmwareUploadForm(forms.Form):
    version = forms.CharField(max_length=10)
    bin_file = forms.FileField()
