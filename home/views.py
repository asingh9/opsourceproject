from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .forms import UploadFileForm
from .models import Question, Result

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #results = handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/home/results/')
    else:
        form = UploadFileForm()
    return render(request, 'home/upload.html', {'form': form})


def results(request):
	response = "Results go here"
	return HttpResponse(response)