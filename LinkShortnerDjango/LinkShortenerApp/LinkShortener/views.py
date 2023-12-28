from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Link
import uuid
import webbrowser

# Create your views here.
def home(request):
    if request.method == "POST":
        longLink = request.POST['link']
        shortId = createShortId()
        new_link = Link(originalLink=longLink, shortLink=shortId)
        new_link.save()

        context = {}
        context['shortUrl'] = shortId

        print("New link has been created.")
        return render(request, "linkcreated.html", context)

    return render(request, "home.html")

def createShortId():
    return str(uuid.uuid4())[:8]

def redirectPage(request, id):
    for item in Link.objects.all():
        if item.shortLink == id:
            webbrowser.open(item.originalLink)
        #else:
            # create url not found page

    return render(request, "home.html")