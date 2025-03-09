from .models import User
from django.db import models
from django.contrib import admin
from django.forms import Textarea
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdminConfig(UserAdmin):
	model = User
	search_fields = ('email', 'username',)
	list_filter = ('email', 'username',)
	ordering = ('-date_created',)
	list_display = ('email', 'username',)

	fieldsets = (
		(None, {'fields': ('email', 'username',)}),
	)

	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
	}

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'username', 'password1', 'password2')
		})
	)

admin.site.register(User, UserAdminConfig)