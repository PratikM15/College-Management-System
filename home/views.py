from django.http import HttpResponse
from django.shortcuts import render
import smtplib
from home.models import Student
from home.models import Professor


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def login(request):
    return render(request,"login.html")

def contact(request):
    return render(request, "contact.html")

def feedback(request):
    return render(request,"contact.html")

def passw(request):
    return render(request, 'passw.html')

def adminlog(request):
    djangoadmin=['PratikM','pratik2000']
    myusername='Group8'
    mypassword='group8'
    username=request.POST.get('adminuser','default')
    password=request.POST.get('adminpass','default')
    def sort(lst):
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if lst[i][1] > lst[j][1]:
                    temp=lst[i]
                    lst[i]=lst[j]
                    lst[j]=temp
        return lst
    if myusername==username and password==mypassword:
        lst = []
        lst2 = []
        object1 = Professor.objects.all()
        object2 = Student.objects.all()
        flag = 1
        i = 0
        for obj in object2:
            lst.append([])
            lst[i].append(obj.name)
            lst[i].append(obj.rollid)
            lst[i].append(obj.dob)
            lst[i].append(obj.branch)
            lst[i].append(obj.year)
            lst[i].append(obj.mob)
            lst[i].append(obj.address)
            lst[i].append(obj.cgpa)
            i += 1
        i=0
        for obj in object1:
            lst2.append([])
            lst2[i].append(obj.name)
            lst2[i].append(obj.roll)
            lst2[i].append(obj.dob)
            lst2[i].append(obj.salary)
            lst2[i].append(obj.mob)
            lst2[i].append(obj.address)
            lst2[i].append(obj.post)
            i += 1
        lst=sort(lst)
        lst2=sort(lst2)
        arg = {'lst': lst, 'lst2': lst2, 'flag': flag, 'username':username}
        return render(request,'adminlog.html', arg)
    else:
        flag=6
        arg = {'flag': flag}
        return render(request, "login.html",arg)

def list(request):
    def sort(lst):
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if lst[i][1] > lst[j][1]:
                    temp=lst[i]
                    lst[i]=lst[j]
                    lst[j]=temp
        return lst
    lst = []
    lst2 = []
    object1 = Professor.objects.all()
    object2 = Student.objects.all()
    flag = 1
    i = 0
    for obj in object2:
        lst.append([])
        lst[i].append(obj.name)
        lst[i].append(obj.rollid)
        lst[i].append(obj.dob)
        lst[i].append(obj.branch)
        lst[i].append(obj.year)
        lst[i].append(obj.mob)
        lst[i].append(obj.address)
        lst[i].append(obj.cgpa)
        i += 1
    i = 0
    for obj in object1:
        lst2.append([])
        lst2[i].append(obj.name)
        lst2[i].append(obj.roll)
        lst2[i].append(obj.dob)
        lst2[i].append(obj.salary)
        lst2[i].append(obj.mob)
        lst2[i].append(obj.address)
        lst2[i].append(obj.post)
        i += 1
    lst = sort(lst)
    lst2 = sort(lst2)
    arg = {'lst': lst, 'lst2': lst2, 'flag': flag}
    return render(request, 'adminlog.html', arg)

def studentlog(request):
    username = request.POST.get('rollid', 'default')
    password = request.POST.get('studpass', 'default')
    objects = Student.objects.all()
    flag=5
    for elt in objects:
        if username==elt.rollid and password==elt.passwd:
            arg = {'name': elt.name, 'id': elt.rollid, 'dob': elt.dob, 'branch': elt.branch, 'year': elt.year, 'mob': elt.mob,
                   'address': elt.address, 'cgpa': elt.cgpa}
            flag=1
            return render(request, 'studentlog.html', arg)
    arg = {'flag': flag}
    return render(request, "login.html",arg)

def proflog(request):
    username = request.POST.get('userid', 'default')
    password = request.POST.get('passwd', 'default')
    objects = Professor.objects.all()
    flag=7
    for elt in objects:
        if username==elt.roll and password==elt.passwd:
            arg = {'name': elt.name, 'id': elt.roll, 'dob': elt.dob, 'salary': elt.salary, 'mob': elt.mob,
                   'address': elt.address, 'post': elt.post}
            flag=1
            return render(request, 'proflog.html', arg)

    arg={'flag':flag}
    return render(request, "login.html",arg)

def search(request):
    sk=request.POST.get('searchkey','Nothing')
    lst=[]
    lst2=[]
    object1 = Professor.objects.all()
    object2 = Student.objects.all()
    flag = 1
    i=0
    for obj in object2:
        if sk.lower() in obj.name.lower() or sk.lower() in obj.rollid or sk.lower() in obj.branch.lower() or sk.lower() in obj.mob.lower() or sk.lower() in obj.year.lower() or sk.lower() in obj.address.lower() or sk.lower() in obj.dob.lower() or sk.lower() in obj.cgpa.lower():
            lst.append([])
            lst[i].append(obj.name)
            lst[i].append(obj.rollid)
            lst[i].append(obj.dob)
            lst[i].append(obj.branch)
            lst[i].append(obj.year)
            lst[i].append(obj.mob)
            lst[i].append(obj.address)
            lst[i].append(obj.cgpa)
            i+=1
            flag=0
    i = 0
    for obj in object1:
        if sk.lower() in obj.name.lower() or sk.lower() in obj.roll or sk.lower() in obj.post.lower() or sk.lower() in obj.mob.lower() or sk.lower() in obj.salary.lower() or sk.lower() in obj.address.lower() or sk.lower() in obj.dob.lower():
            lst2.append([])
            lst2[i].append(obj.name)
            lst2[i].append(obj.roll)
            lst2[i].append(obj.dob)
            lst2[i].append(obj.salary)
            lst2[i].append(obj.mob)
            lst2[i].append(obj.address)
            lst2[i].append(obj.post)
            i+=1
            flag=0
    arg={'lst':lst,'lst2':lst2, 'flag':flag, 'sk':sk}
    return render(request,'search.html',arg)

def profsign(request):
    name = request.POST.get('name', 'default')
    roll_id = request.POST.get('id', 'default')
    mob = request.POST.get('mob', 'default')
    address = request.POST.get('address', 'default')
    post = request.POST.get('post', 'default')
    salary = request.POST.get('salary', 'default')
    dob = request.POST.get('dob', 'default')
    psw = request.POST.get('psw', 'default')
    obj = Professor(name=name, roll=roll_id, mob=mob, address=address, passwd=psw, post=post, salary=salary, dob=dob)
    obj.save()
    return render(request, "success.html")

def studsign(request):
    name = request.POST.get('name', 'default')
    roll_id = request.POST.get('id', 'default')
    mob = request.POST.get('mob', 'default')
    address = request.POST.get('address', 'default')
    branch = request.POST.get('branch', 'default')
    year = request.POST.get('year', 'default')
    dob = request.POST.get('dob', 'default')
    psw = request.POST.get('psw', 'default')
    cgpa = request.POST.get('cgpa', 'default')
    obj = Student(name=name, rollid=roll_id, mob=mob, address=address, passwd=psw, branch=branch, year=year, dob=dob, cgpa=cgpa)
    obj.save()
    return render(request, "success.html")

def addprof(request):
    return render(request,"addprof.html")

def addstud(request):
    return render(request,"addstud.html")

def delete(request):
    return render(request,"delete.html")

def delobj(request):
    name = request.POST.get('name', 'default')
    roll_id = request.POST.get('id', 'default')
    object1 = Professor.objects.all()
    object2 = Student.objects.all()
    flag=0
    for obj in object1:
        if obj.name==name and obj.roll==roll_id:
            obj.delete()
            flag=1
            break
    for obj in object2:
        if obj.name==name and obj.rollid==roll_id:
            obj.delete()
            flag=1
            break
    arg={'flag':flag}
    return render(request,'delete.html',arg)

def check(request):
    name = request.POST.get('name', 'default')
    roll_id = request.POST.get('id', 'default')
    object1 = Professor.objects.all()
    object2 = Student.objects.all()
    lst=[]
    lst2=[]
    flag=0
    search=0
    i=0
    for obj in object1:
        if obj.name == name and obj.roll == roll_id:
            lst2.append(obj.name)
            lst2.append(obj.roll)
            lst2.append(obj.dob)
            lst2.append(obj.salary)
            lst2.append(obj.mob)
            lst2.append(obj.address)
            lst2.append(obj.post)
            flag = 1
            search=1
            break
    for obj in object2:
        if obj.name == name and obj.rollid == roll_id:
            lst.append(obj.name)
            lst.append(obj.rollid)
            lst.append(obj.dob)
            lst.append(obj.branch)
            lst.append(obj.year)
            lst.append(obj.mob)
            lst.append(obj.address)
            lst.append(obj.cgpa)
            flag = 2
            search=1
            break
    if search==1:
        arg = {'flag': flag, 'lst': lst, 'lst2': lst2}
        return render(request, 'check.html', arg)
    else:
        var=4
        arg={'flag':var}
        return render(request, 'check.html',arg)

def changep(request):
    name = request.POST.get('name', 'default')
    roll_id = request.POST.get('id', 'default')
    password = request.POST.get('password','default')
    object1 = Professor.objects.all()
    object2 = Student.objects.all()
    flag = 0
    for obj in object1:
        if obj.name == name and obj.roll == roll_id:
            objt=Professor.objects.get(name=name)
            objt.passwd=password
            objt.save()
            flag = 1
            break
    for obj in object2:
        if obj.name == name and obj.rollid == roll_id:
            objt = Student.objects.get(name=name)
            objt.passwd = password
            objt.save()
            flag = 1
            break
    arg = {'flag': flag}
    if flag==1:
        return render(request,"success1.html")
    else:
        return render(request,"passw.html",arg)