from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author

def get_all_authors(request):
    author = Author.objects.all()
    return render(request, "author.html", {"author": author})



# Create your views here.
