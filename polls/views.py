from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello. Your in the main page of polls app.")

