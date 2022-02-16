from django.shortcuts import render
from .signals import new_subscriber
from django.db import transaction

# Create your views here.

from .models import *

def get_jobs(request):
    """
    function to get all jobs from the database
    """
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})



def get_single_job(request,id):
    """
    function to get single jobs from the database
    """
    job = Job.objects.get(id = id)
    return render(request,"single_job.html",{'job' : job})


    
def subscribe(request, id):
    """
    Function to subscribe to a job and sending customised signal 
    """
    if request.method == "POST":
            with transaction.atomic():                  # Context manager (If error occurs, all transaction will get roll backed i.e. previous state of database data will be restored..)
                job = Job.objects.get(pk=id)
                data = Subscriber.objects.filter(email=request.POST['email'])  # To check user already exists or not, id does not exist then only create new i.e. save()
                if data.exists():
                    sub = data[0]
                else:
                    sub = Subscriber(email=request.POST['email'])
                    sub.save()
                subscription = Subscription(user=sub, job=job)
                subscription.save()
                new_subscriber.send(sender=Subscription, job=job, subscriber=sub)      # sending customised signal  
                
                payload = {
                    'job': job,
                    'email': request.POST['email']
                }
                return render(request, 'subscribed.html', {'payload': payload})


                