from django.shortcuts import render

# Create your views here.
home_page = "home_page.html"

def go_to_home_page(request):
    return render(request, home_page)
