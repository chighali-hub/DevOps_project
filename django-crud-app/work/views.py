from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from work.models import *
from .forms import Memberform
from django.conf import settings
import os

# Create your views here.
def home(request):
    countmember = Members.objects.values('id').count()
    countcourses = Courses.objects.values('id').count()
    countblogs = Blogs.objects.values('id').count()
    countcategory = Category.objects.values('id').count()
    context = {'title': 'Welcome in HomePage',
               'totalMembers':countmember,
               'totalCourses':countcourses,
               'totalBlogs':countblogs,
               'totalCategory':countcategory,
               }
    return render(request, 'index.html', context)

def blog(request):
     return HttpResponse("<h1>Blog Page</h1>")


def members(request):
    members=Members.objects.all()
    context = {'title': 'Members Page',
               'data':members,               
               }
    return render(request, 'viewmembers.html', context)

def addmembers(request):
    if request.method == 'POST':
        form = Memberform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/members') 
    else:
        form = Memberform()
    
    return render(request, 'addmember.html', {'form': form})
   
def deletemember(request,member_id):
    member = get_object_or_404(Members, id=member_id)
    member.delete()
    return redirect('/members')  # or your members list page name
      

def editmember(request,member_id):
    member = get_object_or_404(Members, id=member_id)

    if request.method == 'POST':
        form = Memberform(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/members')  # Or your list view name
    else:
        form = Memberform(instance=member)
    return render(request, 'editmember.html', {'form': form, 'member': member})