from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse
import os
from django.conf import settings
import shutil

from quickstart.models import NewIDUser, IDUser

# def index(request):
#     new_id_user_list = NewIDUser.objects.all().order_by('first_name')
#     template = loader.get_template('register_new_user/index.html')
#     context = {
#         'new_id_user_list': new_id_user_list,
#     }
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'register_new_user/index.html'
    context_object_name = 'new_id_user_list'

    def get_queryset(self):
        return NewIDUser.objects.all().order_by('first_name')

def detail(request, new_user_id):
	new_user_entity = NewIDUser.objects.filter(user_id=new_user_id)
	context = {
        'new_user_entity': new_user_entity,
    }
	template = loader.get_template('register_new_user/details.html')
	return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "Successfully created a new user, ID_USER is DB %s."
    return HttpResponse(response % question_id)

def register(request, new_user_id):
	print(new_user_id)
	new_user_entity = NewIDUser.objects.get(user_id=new_user_id)

	#for new_users in new_user_entity:
	user = IDUser()
	user.first_name = new_user_entity.first_name
	user.last_name = new_user_entity.last_name
	user.email = new_user_entity.email
	user.password = new_user_entity.password
	user.date_of_birth = new_user_entity.date_of_birth
	user.pictureURL = new_user_entity.pictureURL
	user.save()

	new_user_entity.delete()
	new_path = os.path.join(settings.BASE_DIR, 'static')
	new_path_add = os.path.join(new_path, 'idphotos')
	new_path_remove = os.path.join(new_path, 'newidphotos')

	shutil.move(new_path_remove+"/"+user.pictureURL, new_path_add+"/"+user.pictureURL)
	
	return HttpResponseRedirect(reverse('results', args=(new_user_id,)))
