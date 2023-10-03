from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .models import term
from .models import course
from .models import selectcourse
from datetime import datetime

# Create your views here.

def TermList(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    termlist1 =term.objects.all()
    print(termlist1)
    context = {'termlist': termlist1}
    return render(request, 'TermPage.html', context)

def CreateTerm(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    if request.method== "POST":
        term1 = term()
        term1.termname=request.POST.get('termname')
        term1.save()
    return HttpResponseRedirect('/sc/term')

def EditTerm(request,tid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    if request.method== "POST":
        term1 = term.objects.get(termid=tid)
        term1.termname=request.POST.get('txtTerm'+str(tid))
        term1.save()
    return HttpResponseRedirect('/sc/term')

def delTerm(request,tid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    term1=term.objects.get(termid=tid)
    term1.delete()
    return HttpResponseRedirect('/sc/term')

def CourseList(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    courselist1=course.objects.all()
    print(courselist1)
    context = {'courselist': courselist1}
    return render(request, 'CoursePage.html', context)

def CreateCourse(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    if request.method== "POST":
        course1 = course()
        course1.coursename=request.POST.get('coursename')
        print(request.POST.get('coursename'))
        course1.save()
    return HttpResponseRedirect('/sc/course')

def EditCourse(request,cid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    if request.method== "POST":
        course1 = course.objects.get(courseid=cid)
        course1.coursename=request.POST.get('txtCourse'+str(cid))
        course1.save()
    return HttpResponseRedirect('/sc/course')

def delCourse(request,cid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    course1=course.objects.get(courseid=cid)
    course1.delete()
    return HttpResponseRedirect('/sc/course')

def SelectCourseList(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    selectcourselist = selectcourse.objects.all()
    termlist =term.objects.all()
    courselist = course.objects.all()
    context = {'selectcourselist': selectcourselist,'termlist':termlist, 'courselist':courselist}
    return render(request, 'CourseSelectionPage.html',context)

def EditSelectCourse(request,scid1):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    if request.method == "POST":
        selectcourse1 = selectcourse.objects.get(scid=scid1)
        print(selectcourse1)
        selectcourse1.term.termname=request.POST.get('txtTerm'+str(scid1))
        selectcourse1.course.coursename = request.POST.get('txtCourse' + str(scid1))
        selectcourse1.startdate = datetime.strptime(request.POST.get('txtStartDate' + str(scid1)), "%Y-%m-%d")
        selectcourse1.enddate = datetime.strptime(request.POST.get('txtEndDate' + str(scid1)), "%Y-%m-%d")
        selectcourse1.save()
    return HttpResponseRedirect('/sc/selectcourse')

def delSelectCourse(request,scid1):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    selectcourse1=selectcourse.objects.get(scid=scid1)
    selectcourse1.delete()
    return HttpResponseRedirect('/sc/selectcourse')

def GetTerm(requests,termid1):
    termm = term.objects.get(termid=termid1)
    print(termid1)
    return HttpResponse(termm.termname, content_type="text/plain")

def LoadCourse(request,termid1):
    sclist=list(selectcourse.objects.filter(term=termid1))
    courselist={}
    for sc in sclist:
        courselist[sc.course.courseid]=sc.course.coursename
    print(courselist)
    return JsonResponse(courselist,safe=False)

def CreateSelectCourse(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')

    if request.method== "POST":
        selectcourse1 = selectcourse()
        selectcourse1.term_id=request.POST.get('selectTerm')
        selectcourse1.course_id = request.POST.get('selectCourse')
        selectcourse1.save()
    return HttpResponseRedirect('/sc/selectcourse')
