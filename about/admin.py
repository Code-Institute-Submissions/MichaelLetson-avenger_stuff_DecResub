from django.contrib import admin

# Register your models here.
from .models import Contact, Newsletter, Review

admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Review)
