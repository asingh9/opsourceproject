from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=3)
    file = forms.FileField(
    	label='Choose a PDF to Upload'
    )