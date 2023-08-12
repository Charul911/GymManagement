from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from tracker.models import Activity,Session_Year,CustomUser,Customer,Trainer
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request,'trainer/home.html')

@login_required(login_url='/')
def ADD_CUSTOMER(request):
    activity = Activity.objects.all()
    session_year = Session_Year.objects.all()
    
    context = {
        'activity' : activity,
        'session_year' : session_year,
    }
    
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        activity_id = request.POST.get('activity_id')
        session_year_id = request.POST.get('session_year_id')
        
        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('add_customer')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Is Already Taken')
           return redirect('add_customer')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()
            
            activity = Activity.objects.get(id=activity_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            customer = Customer(
                admin = user,
                address = address,
                session_year_id = session_year,
                activity_id = activity,
                gender = gender,
            )
            customer.save()
            messages.success(request, user.first_name + "  " + user.last_name + " is Successfully Added !")
    return render(request,'trainer/add_customer.html', context)

def VIEW_CUSTOMER(request):
    customer = Customer.objects.all()
    context = {
        'customer':customer,
    }
    return render(request,'trainer/view_customer.html', context)

def EDIT_CUSTOMER(request,id):
    customer = Customer.objects.filter(id = id)
    activity = Activity.objects.all()
    session_year = Session_Year.objects.all()
    context = {
        'customer':customer,
        'activity':activity,
        'session_year':session_year,
    }
    return render(request,'trainer/edit_customer.html', context)

def UPDATE_CUSTOMER(request):
    if request.method == "POST":
        customer_id = request.POST.get('customer_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        activity_id = request.POST.get('activity_id')
        session_year_id = request.POST.get('session_year_id')
        
        user = CustomUser.objects.get(id=customer_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email
        if password !=None and password != "":
            user.set_password(password)
        if profile_pic !=None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        
        customer = Customer.objects.get(admin=customer_id)
        customer.address=address
        customer.gender=gender
        
        activity=Activity.objects.get(id=activity_id)
        customer.activity_id=activity
        
        session_year=Session_Year.objects.get(id=session_year_id)
        customer.session_year_id=session_year
        
        customer.save()
        
        messages.success(request,"Record is successfully updated!")
        return redirect('view_customer')
    return render(request,'trainer/edit_customer.html')

def DELETE_CUSTOMER(request,admin):
    customer = CustomUser.objects.get(id = admin)
    customer.delete()
    messages.success(request,'Record is successfully deleted!')
    return redirect('view_customer')

def ADD_ACTIVITY(request):
    if request.method == "POST":
        activity_name = request.POST.get('activity_name')

        activity = Activity(
            name = activity_name,
        )
        
        activity.save()
        messages.success(request, 'Activity added successfully!')
        return redirect('add_activity')
    return render(request,'trainer/add_activity.html')

def VIEW_ACTIVITY(request):
    activity = Activity.objects.all()
    context = {
        'activity' : activity,
    }
    return render(request,'trainer/view_activity.html', context)

def EDIT_ACTIVITY(request,id):
    activity = Activity.objects.get(id=id)
    context = {
        'activity' : activity
    }
    return render(request,'trainer/edit_activity.html',context)

def UPDATE_ACTIVITY(request):
    if request.method == "POST":
        name = request.POST.get('name')
        activity_id = request.POST.get('activity_id')
        activity = Activity.objects.get(id = activity_id)
        activity.name = name
        activity.save()
        messages.success(request, 'Activity updated successfully!')
        return redirect('view_activity')
    return render(request,'trainer/edit_activity.html')

def DELETE_ACTIVITY(request,id):
    activity = Activity.objects.get(id=id)
    activity.delete()
    messages.success(request,'Record deleted Successfully!')
    return redirect('view_customer')

def ADD_TRAINER(request):      
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        contactNo = request.POST.get('contactNo')
        
        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('add_trainer')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Is Already Taken')
           return redirect('add_trainer')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()

            trainer = Trainer(
                admin = user,
                contactNo = contactNo,
                gender = gender,
            )
            trainer.save()
            messages.success(request, user.first_name + "  " + user.last_name + " is Successfully Added !")
    return render(request,'trainer/add_trainer.html')

def VIEW_TRAINER(request):
    trainer = Trainer.objects.all()
    context = {
        'trainer': trainer,
    }
    return render(request,'trainer/view_trainer.html', context)

def EDIT_TRAINER(request,id):
    trainer = Trainer.objects.get(id=id)
    context = {
        'trainer': trainer,
    }
    return render(request,'trainer/edit_trainer.html',context)

def UPDATE_TRAINER(request):
    if request.method == "POST":
        trainer_id = request.POST.get('trainer_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        contactNo = request.POST.get('contactNo')
        
        user = CustomUser.objects.get(id=trainer_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email
        if password !=None and password != "":
            user.set_password(password)
        if profile_pic !=None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        
        trainer = Trainer.objects.get(admin=trainer_id)
        trainer.contactNo = contactNo
        trainer.gender = gender
        
        trainer.save()
        
        messages.success(request,"Record is successfully updated!")
        return redirect('view_trainer')
    return render(request,'trainer/edit_customer.html')

def DELETE_TRAINER(request,admin):
    trainer = CustomUser.objects.get(id=admin)
    trainer.delete()
    messages.success('Record deleted successfully!')
    return redirect('view_trainer')