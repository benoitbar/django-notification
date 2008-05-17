import datetime

from django.db import models

from django.contrib.auth.models import User

class NoticeType(models.Model):
    
    label = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.label
    
    class Admin:
        pass


class Notice(models.Model):
    
    user = models.ForeignKey(User)
    message = models.TextField()
    notice_type = models.ForeignKey(NoticeType)
    added = models.DateTimeField(default=datetime.datetime.now)
    
    class Admin:
        pass


def create_notice_type(label):
    notice_type, created = NoticeType.objects.get_or_create(label=label)
    if created:
        print "Created %s NoticeType" % label


def create(user, notice_type_label, message):
    notice_type = NoticeType.objects.get(label=notice_type_label)
    notice = Notice(user=user, message=message, notice_type=notice_type)
    notice.save()
    return notice
    