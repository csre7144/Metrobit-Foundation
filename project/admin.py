from django.contrib import admin
from project.models import feedback
from contact.models import contactuser
# Register your models here.

class feedbackAdmin(admin.ModelAdmin):
      list_display = ('name', 'email')

class contactuserAdmin(admin.ModelAdmin):
      list_display = ('name1', 'phone1')

admin.site.register(feedback, feedbackAdmin)
admin.site.register(contactuser, contactuserAdmin)
