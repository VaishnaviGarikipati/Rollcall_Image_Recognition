from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage, default_storage
from .models import attendancerec, studentrec, attendate
from selectcourse.models import term, course, selectcourse
import pandas as pd
from django.urls import reverse
import os
import datetime as d
#import pymysql

from rollcallmodule.AttendanceNew import *

from flask import Flask, request, render_template

# Create your views here.

def CoursePopUp(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    termlist=term.objects.all()
    courselist=[]
    tid = request.session.get('termid')
    cid = request.session.get('courseid')
    date = request.session.get('date')
    context = {'termlist': termlist}
    if tid is not None:
        context['courselist']=course.objects.filter(selectcourse__term__in=[tid])
        context['tid'] = int(tid)
    if cid is not None:
        context['cid'] = int(cid)
    if date is not None:
        context['date'] = date
    return render(request, 'coursepopup.html', context)

def CoursePopUpOk(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    if request.method == "POST":
        request.session['termid'] = request.POST.get('term')
        request.session['courseid'] = request.POST.get('course')
        request.session['date'] = request.POST.get('date')
        print (request.session.items())
        return render(request, 'coursepopup.html', {'context': 'ok'})
        #return HttpResponse(status=204)

def ExtractingComparingPage(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    tid = request.session.get('termid')
    cid = request.session.get('courseid')
    date = request.session.get('date')
    if tid != '' and cid != '' and date != '':
        attdlist = attendancerec.objects.all().filter(term=tid, attdatetime=date, course=cid)
        context = {'attdlist': attdlist}
        return render(request, 'ExtractingComparing.html', context)

def MyAttendancePage(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    tid = request.session['termid']
    cid = request.session['courseid']
    attdlist = attendancerec.objects.all().filter(term=tid, course=cid)
    context = {'attdlist': attdlist}
    return render(request, 'MyAttendancePage.html', context)

def RollCallPage(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    tid = request.session.get('termid')
    cid = request.session.get('courseid')
    date = request.session.get('date')
    context = {}
    if tid!='' and cid!='':
        studlist = studentrec.objects.filter(selectcourse__term=tid, selectcourse__course=cid)
        studatt = {}
        attdlist = attendate.objects.filter(selectcourse__term=tid, selectcourse__course=cid)
        tot = len(attdlist)
        if tot != 0:
            for std in studlist:
                present = attendancerec.objects.filter(term=tid, course=cid, studetails=std, attendance=1)
                studatt[std.stunum] = round((len(present)/tot)*100, 2)
        # if date != '':
        #     attd = attendate.objects.filter(attdate=date, selectcourse__term=tid, selectcourse__course=cid)
        #     print(attd)
        #     if len(attd) != 0:
        #         attlist = attendancerec.objects.filter(term=tid, course=cid, attendetails=attd[0], studetails__in=studlist)
        #         if len(attlist) != 0:
        #             for stud in studlist:
        #                 for i in range(len(attlist)):
        #                     if attlist[i].studetails.stunum == stud.stunum:
        #                         studatt[stud.stunum] = attlist[i].attendance
        #                         break
        context = {'stdlist': studlist, 'studatt': studatt}
    return render(request, 'RollCallPage.html', context)

def EditRollCallPage(request,sid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    if request.method== "POST":
        std = studentrec.objects.get(stuid=sid)
        std.stunum = request.POST.get('txtStudentNum'+str(sid))
        std.stuname = request.POST.get('txtStudentName'+str(sid))
        std.save()
    return HttpResponseRedirect('/rollcallmodule/RollCallPage')

def DelRollCallPage(request,sid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    std1 = studentrec.objects.get(stuid=sid)
    std1.delete()
    return HttpResponseRedirect('/rollcallmodule/RollCallPage')

def ViewStudentInformation(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    return render(request, 'UploadStudentInformationPage.html')


# def ExtractData(request,attid):
#     # if request.method== "POST":
#     #     attrecord = attendancerec.objects.get(attendanceID=attid)
#     #     print(attrecord)
#     #     term1.termname=request.POST.get('txtTerm'+str(tid))
#     #     term1.save()
#     #     return HttpResponseRedirect('/sc/term')

def UploadClassStudentPhoto(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    return render(request, 'UploadClassStudentPhotoPage.html')

def upload(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    fileitems = request.FILES.getlist('filename')
    print(fileitems)
    fs = FileSystemStorage(location='rollcallmodule/StudentUplaodedImages/')
    for fileitem in fileitems:
        fs.save(fileitem.name, fileitem)
    return HttpResponseRedirect('/rollcallmodule/UploadClassStudentPhoto')

def Attendancerun(request):
    matchedIds = Run()
    #matchedIds =  {'2020A001': 63, '2020A011': 49}
    tid = request.session.get('termid')
    cid = request.session.get('courseid')
    date = request.session.get('date')
    if tid!='' and cid!='' and date!='':
        tt = term.objects.get(termid=tid)  # Comes term selection
        cc = course.objects.get(courseid=cid)  # Comes course selection
        sc = selectcourse.objects.get(term=tt, course=cc)
        ad = attendate.objects.filter(attdate=date, selectcourse=sc)  # Comes date selection
        if len(ad)==0:
            ad = attendate()
            ad.attdate = date
            ad.selectcourse = sc
            ad.save()
        else:
            ad = attendate.objects.get(attdate=date, selectcourse=sc)
        for id, perc in matchedIds.items():
            std = studentrec.objects.filter(stunum=id, selectcourse=sc)
            if len(std)!=0:
                attd = attendancerec.objects.filter(studetails=std[0], attendetails=ad, term=tt, course=cc)
                if len(attd)==0:
                    attd = attendancerec()
                    attd.studetails = std[0]
                    attd.attdatetime = date
                    attd.attendetails = ad
                    attd.attendance = True if perc > 60 else False
                    attd.matchrate = perc
                    attd.term = tt
                    attd.course = cc
                else:
                    attd = attendancerec.objects.get(studetails=std[0], attendetails=ad, term=tt, course=cc)
                    attd.attdatetime = date
                    attd.attendance = True if perc > 60 else False
                    attd.matchrate = perc
                attd.save()

        unmatched = studentrec.objects.filter(selectcourse=sc).exclude(stunum__in=matchedIds.keys())
        for ustd in unmatched:
            attd = attendancerec.objects.filter(studetails=ustd, attendetails=ad, term=tt, course=cc)
            if len(attd)==0:
                attd = attendancerec()
                attd.studetails = ustd
                attd.attdatetime = date
                attd.attendetails = ad
                attd.attendance = False
                attd.term = tt
                attd.course = cc
                attd.save()

    #cleanup files
    dir = 'rollcallmodule/StudentUplaodedImages'
    for f in os.listdir(dir):
        fpath = os.path.join(dir, f)
        os.remove(fpath)

    return HttpResponseRedirect('/rollcallmodule/ExtractingComparing')

def Udelete(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
#        return render(request, 'UploadClassStudentPhotoPage.html')
        return HttpResponseRedirect('/rollcallmodule/UploadClassStudentPhoto')

    # check if the file has been uploaded
    #if fileitem.filename:
        # strip the leading path from the file name
        #fn = os.path.basename(fileitem.filename)
        # open read and write the file into the server
        #open(fn, 'wb').write(fileitem.file.read())

    #app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# def upload(request1):
#     target = os.path.join(APP_ROOT, 'UploadedImages/')
#     print(target)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#
#     for file in request.files.getlist("file"):
#         print(file)
#         filename = file.filename
#         destination = "/".join([target, filename])
#         print(destination)
#         file.save(destination)
#         print("Upload Complete")
#     return render_template("UploadClassStudentPhotoPage.html")

#def UploadStudentInformation(request):
 #   if request.method== "POST":
 #       studentrec1 = studentrec()
 #       studentrec1.stunum=request.POST.get('stunum')
  #      studentrec1.stuname = request.POST.get('stuname')
  #      studentrec1.selectcourse = request.POST.get('scid')
  #      studentrec1.save()
   #     return HttpResponseRedirect('/rollcallmodule/StudentInformation')

def getext(filename):
    strlist=filename.split('.')
    return strlist[len(strlist)-1]

def importstu(request):
    if request.method == "POST":
        files = request.FILES.getlist('filename')
        print(files)
        for file in files:
            type_excel = getext(file.name)
            print(type_excel)
            if 'xlsx' == type_excel or 'xls'==type_excel:
                filename=pd.read_excel(file)
                rows=len(filename)
                # termid=request.session.get('termid')
                # courseid=request.session.get('courseid')
                # term1 = term.objects.get(termid=termid)
                # course1 = course.objects.get(courseid=courseid)
                # sc=selectcourse.objects.filter(scid=scid,course=course1)
                for i in range(rows):
                    stunum=filename['stunum'][i]
                    stuname=filename['stuname'][i]
                    scid1 = filename['scid'][i]
                    sc = selectcourse.objects.get(scid=scid1)
                    student = studentrec()
                    student.stunum=stunum
                    student.stuname=stuname
                    student.selectcourse=sc
                    student.save()
            else:
                fs = FileSystemStorage(location='rollcallmodule/StudentImages/')
                fs.save(file.name, file)
    return HttpResponseRedirect('/rollcallmodule/StudentInformation')

#       return HttpResponseRedirect('/rollcallmodule/StudentInformation')

    # def upload(request):
    #     fileitems = request.FILES.getlist('filename')
    #     print(fileitems)
    #     fs = FileSystemStorage(location='rollcallmodule/StudentUplaodedImages/')
    #     for fileitem in fileitems:
    #         fs.save(fileitem.name, fileitem)
    #     return HttpResponseRedirect('/rollcallmodule/UploadClassStudentPhoto')

def HistoryRec(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    tid = request.session.get('termid')
    cid = request.session.get('courseid')
    attdlist = attendancerec.objects.filter(term=tid, course=cid)
    datelist = attendate.objects.filter(selectcourse__term=tid, selectcourse__course=cid)
    context = {'attdlist': attdlist, 'datelist': datelist}
    print(attdlist)
    # maxid=context.get('attdateid')
    # statistic=attendancerec.stats(maxid)
    # context=dict(context,**statistic)
    return render(request,'History.html',context)

def EditHistory(request,aid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    if request.method== "POST":
        attdl = attendancerec.objects.get(attendanceID=aid)
        attdl.attendance = request.POST.get('txtAttendance'+str(aid))
        attdl.save()

    return HttpResponseRedirect('/rollcallmodule/history')

def hiscall(request,calldateid):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usermgnt/admin')
    tid = request.session['termid']
    context=attendancerec.atthist(tid,calldateid)

    maxid=context.get('calldateid')
    statistic=attendancerec.statics(maxid)
    context=dict(context,**statistic)
    return render(request,'History.html',context)


