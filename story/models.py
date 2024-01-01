from django.db import models

from account.models import account
from django.utils.translation import gettext as _
import datetime
import pytz

class Storys(models.Model):
    Writer = models.ForeignKey(account, on_delete=models.CASCADE)
    StoryTitel = models.TextField(unique=True)
    ganer = models.CharField(max_length=20,choices=(('actions','actions'),('deram','deram'),('harror','harror'),('fantesy','fantesy')))
    summary = models.TextField()
    status = models.BooleanField(default=True)
    CreatedTime = models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=True)
    is_papular = models.BooleanField(default=False)
    is_papular_counter = models.PositiveIntegerField(default=0)
    is_editors_love = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.StoryTitel}'

    def PeopleLike(self,is_papular_counter,is_papular):
        if int(is_papular_counter) == self.is_papular_counter:
            if is_papular == self.is_papular :
                if (self.is_papular_counter) >= 100:
                        self.is_papular = True
                        self.save()
                        return True
        return False

    def IsNew(self,is_new):
        if is_new == self.is_new :
            if (datetime.datetime.now().astimezone(pytz.utc).month - self.CreatedTime.month) >= 1:
                self.is_new = False
                self.save()
                return True
        return False


class Chapters(models.Model):
    writer = models.ForeignKey(account,on_delete=models.CASCADE )
    ForStory = models.ForeignKey(Storys,on_delete=models.CASCADE )
    ChapterTitel = models.TextField(unique=True)
    Section = models.TextField()
    PublishDateTime = models.DateTimeField(auto_now=True)
    CreatedTime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.ChapterTitel}'

