from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from quickstart.models import NewIDUser

def index(request):
    new_id_user_list = NewIDUser.objects.all().order_by('first_name')
    template = loader.get_template('register_new_user/index.html')
    context = {
        'new_id_user_list': new_id_user_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, new_user_id):
	new_user_entity = NewIDUser.objects.filter(user_id=new_user_id)
	context = {
        'new_user_entity': new_user_entity,
    }
	print(new_user_entity)
	template = loader.get_template('register_new_user/details.html')
	return HttpResponse(template.render(context, request))
	
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)