from django.http import HttpResponse


def text_sos(request):
    return HttpResponse("<h1>This is my django project sos</h1>")
