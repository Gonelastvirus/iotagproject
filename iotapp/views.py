from django.shortcuts import render,redirect
from django.utils import timezone
from iotapp.models import CustomUser
from django.contrib.auth.models import User,auth
from .models import Vegetable,SensorData
# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request,'permission_denied.html')
    user_instance = CustomUser.objects.get(id=request.user.id)
    
    if not user_instance.is_superuser:
        print(user_instance)
        return render(request,'dashboard.html',{'token':user_instance.token,'is_not_superuser': not user_instance.is_superuser})
    else:
        return redirect('/admin')
def permission_denied(request):
    return render(request,"permission_denied.html")
def recentactivity(request):
    interval = request.GET.get('interval')
    if interval:
        interval = int(interval)
        now = timezone.now()
        data = SensorData.objects.filter(timestamp__gte=now-timezone.timedelta(minutes=interval), user_id=request.user.id)
    else:
        data = []
    return render(request,"recentactivity.html",{'data': data})
def soiltempdata(request):
    vegetables = Vegetable.objects.all()
    return render(request,"soiltemperature.html",{'vegetables': vegetables})
def settings(request):
    if request.method == 'POST':
        # Update the user's information
        field_map = {
            'username': 'username',
            'email': 'email',
            'token': 'token',
        }
        user = CustomUser.objects.get(pk=request.user.id)
        for field_name, attr_name in field_map.items():
            if field_name in request.POST:
                setattr(user, attr_name, request.POST[field_name])
        user.save()
        auth.logout(request)
        return redirect('login')

    # If the request method is not POST, render the form
    user = CustomUser.objects.get(pk=request.user.id)
    context = {'user': user}
    return render(request, 'setting.html', context)