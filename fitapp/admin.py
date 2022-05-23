from django.contrib import admin
from .models import UserFitbit, TimeSeriesData

# Register your models here.
admin.site.register(UserFitbit)
admin.site.register(TimeSeriesData)