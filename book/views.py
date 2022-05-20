from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from . import models, forms


# Create your views here.
def title(request):
    return HttpResponse("<h1>Library</h1>")


def all_books(request):
    books = models.Book.objects.all()
    return render(request, "book.html", {"books": books})


def book_info(request):
    object = get_object_or_404(models.Book, id=id)
    return render(request, "detail.html", {"book": object})


def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse("TVShow Created successfully")
            return redirect(reverse("books_url:all_books_url"))
    else:
        form = forms.BookForm()
    return render(request, "add_book.html", {"form": form})
