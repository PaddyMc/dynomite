from quickstart.models import IDUser, NewIDUser
from rest_framework import serializers

class IDUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = IDUser
		fields = ('url', 'user_id', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'pictureURL')

class NewIDUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = NewIDUser
		fields = ('url', 'user_id', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'pictureURL')
