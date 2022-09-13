from django.contrib import admin
from . models import *
# Register your models here.

class AnswereAdmin(admin.StackedInline):
    model = Answere

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswereAdmin]

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answere)
