from django.contrib import admin
from .models import Callback,Visitor,Ip,Round1,Round2,Mopup,College_predictor
# Register your models here.
admin.site.register(Callback)
admin.site.register(Visitor)
admin.site.register(Ip)
admin.site.register(Round1)
admin.site.register(Round2)
admin.site.register(Mopup)
admin.site.register(College_predictor)