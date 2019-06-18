from django.contrib import admin
from main.models import news
from main.models import comments
from main.models import que

admin.site.register(news)
admin.site.register(comments)
admin.site.register(que)
