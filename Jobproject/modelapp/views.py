from django.shortcuts import render
# Create your views here.
from modelapp.models import HydJobs,BngJobs,PuneJobs
def homepage_view(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list=HydJobs.objects.all()
    return render(request,'testapp/hyd.html',{'jobs_list':jobs_list})

def bngjobs_view(request):
    jobs_list=BngJobs.objects.all()
    return render(request,'testapp/bng.html',{'jobs_list':jobs_list})

def punejobs_view(request):
    jobs_list=PuneJobs.objects.all()
    return render(request,'testapp/pune.html',{'jobs_list':jobs_list})

