from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


def myfirst(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context,request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    # mydata = Member.objects.values_list('firstname')
    # mydata = Member.objects.all()
    # mydata = Member.objects.filter(firstname='Emil').values()
    # mydata = Member.objects.filter(firstname='Emil').values()|Member.objects.filter(firstname='yassmine').values()
    # mydata = Member.objects.filter(Q(firstname='Emil')|Q(firstname='yassmine')).values()
    # mydata = Member.objects.filter(firstname__startswith='e').values()
    mydata = Member.objects.all().order_by('id').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context,request))


