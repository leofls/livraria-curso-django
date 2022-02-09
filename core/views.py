from django.http import HttpResponse

def teste(request):
    return HttpResponse("hello world ..!")

def teste2(request):
    return HttpResponse("bloa ..!")