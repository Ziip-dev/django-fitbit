from django.contrib import admin
from .models import UserFitbit, TimeSeriesDataType, TimeSeriesData

# Register your models here.
admin.site.register(UserFitbit)
admin.site.register(TimeSeriesDataType)
admin.site.register(TimeSeriesData)