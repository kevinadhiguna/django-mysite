from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello World. You're at polls index.")

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)
