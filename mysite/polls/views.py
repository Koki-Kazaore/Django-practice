from django.http import HttpResponse


def index(request):
    return HttpResponse("こんにちは！ You're at the polls index.")
    