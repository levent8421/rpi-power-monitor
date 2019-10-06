from django.http import HttpResponseRedirect


def index(request, *args, **kwargs):
    return HttpResponseRedirect('/static/index.html')
