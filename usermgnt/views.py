from django.shortcuts import render,HttpResponseRedirect
from usermgnt.models import User
from selectcourse.models import selectcourse, course
from rollcallmodule.models import studentrec, attendancerec

def AdminLogin(request):
    return render(request,'AdminLoginPage.html')

def StudLogin(request):
    return render(request,'StudentLoginPage.html')

def SLoginAction(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password)
        if len(user) > 0:
            request.session['username'] = user[0].username
            request.session['userid'] = user[0].userid
            stud = studentrec.objects.filter(stunum=user[0].username)
            attd = attendancerec.objects.filter(studetails__in=stud)
            context = {'studlist': stud, 'attdlist': attd}
            return render(request, 'MyAttendancePage.html', context)
        else:
            return HttpResponseRedirect('/usermgnt/student')

def Slogout(request):
    del request.session['username']
    del request.session['userid']
    return HttpResponseRedirect('/usermgnt/student')

def ALoginAction(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password)
        if len(user) > 0:
            request.session['username'] = user[0].username
            request.session['userid'] = user[0].userid
            return render(request, 'RollCall.html')
        else:
            return HttpResponseRedirect('/usermgnt/admin')


def Alogout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return HttpResponseRedirect('/usermgnt/admin')

def RollCall(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    return render(request, 'RollCall.html')

def StudAttGet(request):
    if request.method == "GET":
        stunum = request.session.get('username')
        cid = int(request.GET.get('cid'))
        dt = request.GET.get('dt')
        stud = studentrec.objects.filter(stunum=stunum)
        attd = attendancerec.objects.filter(studetails__in=stud)
        if cid is not None and cid != 0:
            attd = attendancerec.objects.filter(studetails__in=stud, course_id=cid)
        elif dt is not None and dt != "":
            attd = attendancerec.objects.filter(studetails__in=stud, attdatetime=dt)
        if cid != 0 and dt != "":
            attd = attendancerec.objects.filter(studetails__in=stud, course_id=cid, attdatetime=dt)

        context = {'studlist': stud, 'attdlist': attd}
        return render(request, 'MyAttendancePage.html', context)


