from dataclasses import field, fields
from django.contrib import admin
from .models import Suggestion


admin.site.register(Suggestion)
