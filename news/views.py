from django.template import RequestContext
from django.shortcuts import render_to_response

from news.models import *
moj_tekst = "jestem widokiem gloalnym"
#from django.contrib.auth import authenticate, logi

def index(request):
    news = News.objects.all().order_by('-posted_date')
    category = Category.objects.all()

    return render_to_response('index.html',
            {'news': news, 'zmienna': moj_tekst, 'category': category},
            context_instance=RequestContext(request))
# Create your views here.
# def login_user(request):
# 	"""
# 	django.contrib.auth.views.login login view
# 	"""
# 	if not request.user.is_authenticated():
# 		return django.contrib.auth.views.login(request, template_name='userpanel/login.html')
# 	else:
# 		return HttpResponseRedirect("/user/")
#
# def logout_then_login(request):
# 	"""
# 	django.contrib.auth.views.logout_then_login logout view
# 	"""
# 	return django.contrib.auth.views.logout_then_login(request, login_url = '/')