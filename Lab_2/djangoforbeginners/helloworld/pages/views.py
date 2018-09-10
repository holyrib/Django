from django.shortcuts import render

def homePageView(request):
    return HttpResponse('Hello, World!')
