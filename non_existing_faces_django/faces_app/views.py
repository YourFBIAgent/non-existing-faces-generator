from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from . import functions
from . import forms

def index(request):
    if request.method == "GET":
        form = forms.GeneratorForm()

        return render(request,"index.html",{"form":form})

    elif request.method == "POST":
        form = forms.GeneratorForm(request.POST)

        if not form.is_valid():
            return HttpResponse("Invalid form data!",status=422)

        effects = form.cleaned_data.get("effects")
        images = functions.get_random_faces(effects)

        return JsonResponse(images,safe=False)

    return HttpResponse("Invalid request method!",status=400)
