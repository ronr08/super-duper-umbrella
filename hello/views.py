from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from models import Post
from django.utils import timezone

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


# Create your views here.
def myverb( request ):
	return HttpResponse('Sample')

@csrf_exempt
def echo( request ):
	if request.method == 'POST':
		return HttpResponse('This is a POST request')
	else:
		string = 'Variables: <br/><br/>'
		for k,v in request.GET.iteritems():
			string += '<b>' + k  + '</b>' + ': ' + v + '<br/>'
		return HttpResponse( string )

def post_list(request):
	posts = Post.objects.filter(created_date__lte = timezone.now()).order_by('created_date')
	return render(request, 'myApp/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'myApp/post_detail.html', {'post': post})

