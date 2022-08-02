
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import User
from feedback.models import Feedback
from taskData import models
from django.contrib import messages
from taskData.models import TaskData
from feedback.models import Feedback
import datetime
import smtplib, ssl



#creating tasks
@login_required(login_url="/login")
def home(request):
    totaltask = TaskData.objects.all().count()
    completedtask = TaskData.objects.filter(taskstatus='Completed').count()
    pendingtask = TaskData.objects.filter(taskstatus='Pending').count()
    context = {
        "totaltask":totaltask,
        "completedtask":completedtask,
        "pendingtask":pendingtask
    }
    
    taskData = TaskData.objects.filter().exclude(taskstatus='Completed').order_by('-id')
    # return render(request, "search.html")
    return render(request, 'Dashboard.html', {"context":context, "taskData":taskData})

@login_required(login_url="/login")
def createTask(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    if request.method == "POST":
        empId = request.POST.get('empid')
        empName = request.POST.get('empname')
        empEmail = request.POST.get('empemail')
        taskName = request.POST.get('task-option')
        dueDate = request.POST.get('date')
        taskStatus = (request.POST.get('option'))
        taskSummary = request.POST.get('tasksummary')
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d")
        # print(empId, empEmail, empName, taskName, dueDate, taskStatus, taskSummary)
        if taskStatus== "completed":
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "mtrackermarlabsltd@gmail.com"
            receiver_email = empEmail
            password = "trxhkjednzzqyqmr"
            message = 'Subject: mTracker-Feedback Form \n\nYour Query has been resolved.\n Please go through this link to rate us:http://127.0.0.1:8000/feedback/'
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                
        td = TaskData(empid=empId, empname=empName, empemail=empEmail, taskname=taskName.upper(), duedate=dueDate, taskstatus=taskStatus.title(), tasksummary=taskSummary+"      "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), createdon=cur_time)
        td.save()
        return redirect('search')

        # print(empId, empName, empEmail, taskName, dueDate, taskStatus, taskSummary)
        # print('successfull')
        # return HttpResponseRedirect('/')
    return render(request,"home-create-task.html")


#method to show completed and pending tasks and search
@login_required(login_url="/login")
def search(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    totaltask = TaskData.objects.all().count()
    completedtask = TaskData.objects.filter(taskstatus='Completed').count()
    pendingtask = TaskData.objects.filter(taskstatus='Pending').count()
    
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        empid = request.POST.get('empid')
        task = request.POST.get('task')
        # searchData = TaskData.objects.raw(f"SELECT * FROM taskData_taskdata WHERE duedate BETWEEN '{fromdate}' AND '{todate}' AND empid={empid} AND taskname={task.upper()}")
        if fromdate =="" and todate =="":
            fromdate='1990-12-31'
            todate=datetime.datetime.now().strftime('%Y-%m-%d')
        searchData = TaskData.objects.filter(createdon__range=[fromdate, todate], empid__icontains=empid, taskname__icontains=task.upper()).order_by('-id')
        totaltaskdata = searchData.filter().count()
        totaltaskdata1 = searchData.filter()
        totaltaskcompleteddata = searchData.filter(taskstatus='Completed').count()
        totaltaskcompleteddata2 = searchData.filter(taskstatus='Completed')
        tottaltaskpendingdata = searchData.filter(taskstatus='Pending').count()
        tottaltaskpendingdata3 = searchData.filter(taskstatus='Pending')
        # print(totaltaskdata1,totaltaskcompleteddata2,tottaltaskpendingdata3)
        context = {
        "totaltask":totaltaskdata,
        "completedtask":totaltaskcompleteddata,
        "pendingtask":tottaltaskpendingdata,
        "taskData":searchData,
        'totaltaskdata1':totaltaskdata1,
        'totaltaskcompleteddata2':totaltaskcompleteddata2,
        'tottaltaskpendingdata3':tottaltaskpendingdata3
        }
        return render(request, "search.html", context=context)
    taskData = TaskData.objects.filter()
    totaltaskcompleteddata2 = taskData.filter(taskstatus='Completed')
    tottaltaskpendingdata3 = taskData.filter(taskstatus='Pending')
    
    context = {
        "totaltask":totaltask,
        "completedtask":completedtask,
        "pendingtask":pendingtask,
        "taskData":taskData,
        'totaltaskdata1':taskData,
        'totaltaskcompleteddata2':totaltaskcompleteddata2,
        'tottaltaskpendingdata3':tottaltaskpendingdata3
        }
    return render(request, "search.html", context=context)

def searchResult(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    searchData = TaskData.objects.all()
    return render(request, 'searchresult.html',{'searchData':searchData})


def searchCompletedTask(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    searchData = TaskData.objects.filter(taskstatus='Completed')
    return render(request, 'completedtask.html', {'searchData':searchData})


def searchPendingTask(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    searchData = TaskData.objects.filter(taskstatus='Pending')
    return render(request, 'pendingtask.html', {'searchData':searchData})


@login_required(login_url="/login")
def updateTask(request, id):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    getData = models.TaskData.objects.get(pk=id)
    # print(getData)
    if request.method == 'POST':
        getData = models.TaskData.objects.get(pk=id)
        getData.empname = request.POST.get('emp-name')
        getData.empemail = request.POST.get('emp-email')
        getData.taskname = request.POST.get('task-option').upper()
        getData.duedate = request.POST.get('due-date')
        getData.taskstatus = request.POST.get('task-status').title()
        getData.tasksummary = request.POST.get('task-summary')
        cur_time = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        getData.tasksummary = getData.tasksummary+"      "+cur_time
        getData.save()
        if getData.taskstatus=="Completed":
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "mtrackermarlabsltd@gmail.com"
            receiver_email = getData.empemail
            password = "trxhkjednzzqyqmr"
            message = 'Subject: mTracker-Feedback Form \n\nYour Query has been resolved.\n Please go through this link to rate us:http://127.0.0.1:8000/feedback/'
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

        messages.success(request, 'You successfully updated your data!')
        return redirect('search')

    return render(request, "updatetask.html", {'getData':getData})

@login_required(login_url="/login")
def deleteTask(request, id):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    if request.method == "POST":
        getData = models.TaskData.objects.get(pk=id)
        # print(getDeletedData)
        getData.delete()
        # messages.success(request, 'You successfully deleted')
        return redirect('search')
    return HttpResponse('404 no page found!')
    # return render(request, "search.html", {"getData":getData})


@login_required(login_url="/login")
def profileData(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    totaltask = TaskData.objects.all().count()
    completedtask = TaskData.objects.filter(taskstatus='Completed').count()
    pendingtask = TaskData.objects.filter(taskstatus='Pending').count()

    excellent = Feedback.objects.filter(rating='4').count()
    good = Feedback.objects.filter(rating='3').count()
    average = Feedback.objects.filter(rating='2').count()
    sad = Feedback.objects.filter(rating='1').count()
    very_sad = Feedback.objects.filter(rating='0').count()

    allData = Feedback.objects.all().order_by('-id')

    context = {
        "totaltask":totaltask,
        "completedtask":completedtask,
        "pendingtask":pendingtask,
        'excellent':excellent, 
        'good':good, 
        'average':average,
        'sad':sad,
        'very_sad':very_sad,
        'allData': allData
    }
    return render(request, "hr-profile.html", context=context)

def feedbackData(request):
    """Created by Sachin (ASE DATA ENGINEER) """

    if request.method == 'POST':
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')
        print(rating, feedback)

        fb = Feedback(rating=rating, feedback=feedback)
        fb.save()
        return HttpResponse("Feedback Successfully Submitted")
    return render(request, "feedback-rating-form.html")

# HR user registration 
def user_registration(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    if request.user.is_authenticated:
        return redirect('search')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            empid = request.POST.get('employeeid')
            email = request.POST.get('email')
            designation = request.POST.get('designation')
            location = request.POST.get('location')
            password = request.POST.get('password')
            conf_emp_password = request.POST.get('conf_password')

            # print(first_name, empid, email, password, conf_emp_password, designation, location)

            if password == conf_emp_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Employee email already registered...")
                    return redirect(user_registration)
                else:
                    user = User.objects.create_user(email=email, password=password, empid=empid, first_name=first_name, last_name=last_name, designation=designation, location=location)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request, "Both password are not matching...")
                return redirect(user_registration)
        return render(request, 'register.html')

#HR user login
def userLogin(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    if request.user.is_authenticated:
        return redirect('search')

    if request.method == "POST":
        username = request.POST.get('emp-id')
        password = request.POST.get('password')

        print(username, password)
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid username or password...")
            return redirect('login')

    return render(request, 'login.html')


def userLogout(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    logout(request)
    return redirect('login')

