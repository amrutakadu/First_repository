from django.db import models

# Create your models here.

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from jobs_board_main.signals import new_subscriber
from jobs_board_main.models import Job, Subscriber, Subscription

from django.core.mail import send_mail
from django.conf import settings


@receiver(new_subscriber, sender=Subscription)
def handle_new_subscription(sender, **kwargs):
    """
    Function to recieve signal when new subscriber has subscribed to a job
    """
    print("\nIn handle_new_subscription...\n")

    subscriber = kwargs['subscriber']
    job = kwargs['job']

    msg = "User {} has just subscribed to the Job {} of {} company".format(subscriber.email, job.title,job.company)
    print(msg)

    # send_mail(f"New Subscription for {job.title}", message=msg, 
    #             from_email="kaduamruta88@gmail.com", recipient_list=[job.company_email,"amrutakadu99@gmail.com"], fail_silently = False)

    send_mail(f"New Subscription for {job.title}", message=msg, 
                from_email=settings.EMAIL_HOST_USER, recipient_list=["amrutakadu99@gmail.com"], fail_silently = False)           # recipient_list=[job.company_email,"amrutakadu99@gmail.com"]


    """
    OUTPUT :
    In handle_new_subscription...

    User rohit_1@gmail.com has just subscribed to the Job Java Developer of TCS company
    Content-Type: text/plain; charset="utf-8"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Subject: New Subscription for Java Developer
    From: kaduamruta88@gmail.com
    To: hr@tcs.com, amrutakadu99@gmail.com
    Date: Sun, 13 Feb 2022 19:24:36 -0000
    Message-ID: <164478027678.3752.8581425702188598014@hp-PC>

    User rohit_1@gmail.com has just subscribed to the Job Java Developer of TCS company
    -------------------------------------------------------------------------------
    """



@receiver(pre_delete, sender=Job)
def handle_deleted_job_posting(**kwargs):
    """
    Function to recieve signal before a job is deleted to convey subscribed users that the job is no more avialable
    """
    print("\nIn handle_deleted_job_posting...\n")

    job = kwargs['instance']                # instace/object of Job

    subscribers = Subscription.objects.filter(job = job)          # filter to find the subscribers list

    for subscriber in subscribers:
        msg = "Dear {}, the job posting {} by {} has been taken down".format(subscriber.user.email, job.title, job.company)
        print(msg,"\n")

    """
    OUTPUT :
    In handle_deleted_job_posting...

    Dear amruta@gmail.com, the job posting sdv by sefdasd has been taken down
    """