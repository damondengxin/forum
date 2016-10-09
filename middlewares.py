import logging
from django.http import  HttpResponse

LOGGER=logging.getLogger('forum')

class PrintParamsMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print(request.GET)
        print(request.POST)
        response = self.get_response(request)
        return  response



class logExceptionMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            LOGGER.exception(e)
            return HttpResponse("出错了")
        return response