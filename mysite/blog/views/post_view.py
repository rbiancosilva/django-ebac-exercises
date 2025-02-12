from django.views import generic
from django.http import HttpResponse

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is a response from Post view')