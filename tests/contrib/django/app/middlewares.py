from django.http import HttpResponse


class CatchExceptionMiddleware(object):
    def process_exception(self, request, exception):
        return HttpResponse(status=500)
