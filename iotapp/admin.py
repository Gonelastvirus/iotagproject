from django.contrib import admin
from .models import SensorData,DailySensorData,Vegetable
from django.contrib.auth.decorators import user_passes_test
from iotapp.models import CustomUser
# Register your models here.
admin.site.register(SensorData)
admin.site.register(DailySensorData)
admin.site.register(Vegetable)
admin.site.register(CustomUser)
def admin_only(user):
# check if the user is a staff member or superuser
    print(user)
    return user.is_anonymous or (user.is_staff or user.is_superuser)
# Apply this decorator to the login view
admin.site.login = user_passes_test(admin_only, login_url='permission_denied')(admin.site.login)
    