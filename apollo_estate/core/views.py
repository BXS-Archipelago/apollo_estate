from django.shortcuts import render

# function based views :

def frontpage(request): 
    return render(request, 'core/frontpage.html')

def about(request):
    return render(request, 'core/about.html')