from django.shortcuts import render, redirect
from .models import Student
import random


# Create your views here.

# postgresql front page
def show_data(request):
    students = Student.objects.all()
    return render(request, 'Postgresql-frontpage.html', {'students': students})


def add_data(request):
    if request.method == "POST":
        StudentName = request.POST['StudentName']
        StudentGender = request.POST['StudentGender']
        StudentEmail = request.POST['StudentEmail']
        StudentScore = int(request.POST['StudentScore'])
        data = Student(StudentName=StudentName, StudentGender=StudentGender, StudentEmail=StudentEmail,
                       StudentScore=StudentScore)
        data.save()

        return redirect('/show/')
    else:
        return render(request, 'Postgresql-addpage.html')


def top5_data(request):
    students = Student.objects.all()
    count = Student.objects.all().count()
    if count != 0:
        if count > 5:
            students = Student.objects.all().order_by(("-StudentScore"))[:5]
        else:
            students = Student.objects.all().order_by(("-StudentScore"))[:count]
    else:
        students = Student.objects.all()
    return render(request, 'Postgresql-frontpage.html', {'students': students})


def bottom5_data(request):
    count = Student.objects.all().count()
    if count != 0:
        if count > 5:
            students = Student.objects.all().order_by(("StudentScore"))[:5]
        else:
            students = Student.objects.all().order_by(("StudentScore"))[:count]
    else:
        students = Student.objects.all()
    return render(request, 'Postgresql-frontpage.html', {'students': students})


def StudentMale_data(request):
    students = Student.objects.all().filter(StudentGender="Male")
    return render(request, 'Postgresql-frontpage.html', {'students': students})


def StudentFemale_data(request):
    students = Student.objects.all().filter(StudentGender="Female")
    return render(request, 'Postgresql-frontpage.html', {'students': students})



def StudentOther_data(request):
    students = Student.objects.all().filter(StudentGender="Other")
    return render(request, 'Postgresql-frontpage.html', {'students': students})


def delete_data(request, pk):
    students = Student.objects.get(id=pk)
    if request.method == 'POST':
        students.delete()
        return redirect('/show/')
    context = {
        'student': students,
    }
    return render(request, 'Postgresql-deletepage.html', context)


def update_data(request, pk):
    students = Student.objects.get(id=pk)
    if request.method == 'POST':
        students.delete()
        StudentName = request.POST['StudentName']
        StudentGender = request.POST['StudentGender']
        StudentEmail = request.POST['StudentEmail']
        StudentScore = int(request.POST['StudentScore'])
        data = Student(StudentName=StudentName, StudentGender=StudentGender, StudentEmail=StudentEmail,
                       StudentScore=StudentScore)
        data.save()

        return redirect('/show/')

    context = {'students': students}

    return render(request, 'Postgresql-updatepage.html', context)


def dummy_data(request):
    gender_list=["Male", "Female", "Other"]
    for i in range(0,10):
        StudentName = "Student"+str(random.randint(0,1000))
        StudentGender = gender_list[random.randint(0,2)]
        StudentEmail = str(StudentName)+"@xyz.com"
        StudentScore = random.randint(0,99)
        data = Student(StudentName=StudentName, StudentGender=StudentGender, StudentEmail=StudentEmail,
                       StudentScore=StudentScore)
        data.save()
    return redirect('/show/')


def delete_all(request):
    if request.method == 'POST':
        students = Student.objects.all()
        students.delete()
        return redirect('/show/')
    return render(request, 'Postgresql_deleteallpage.html')


