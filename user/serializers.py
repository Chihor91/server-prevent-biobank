from rest_framework import serializers
from .models import (
	User
)

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = [
			'id',
			'email',
			'username',
			'password',
			'is_superuser'
		]