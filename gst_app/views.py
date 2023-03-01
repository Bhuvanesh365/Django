from django.http import HttpResponse
from django.template import loader
from .models import Gst_app

def gst_app(request):
  mycustomers = Gst_app.objects.all().values()
  template = loader.get_template('main.html')
  context = {
    'mycustomers': mycustomers,
  }
  return HttpResponse(template.render(context, request))

