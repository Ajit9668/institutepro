from django.contrib import admin
from .models import course

class admincourse(admin.ModelAdmin):
    list_display=['course_name','fee','duration','start_date','trainer_name','trainer_exp','training_mode']
admin.site.register(course,admincourse)
