#！coding=utf-8
from __future__ import unicode_literals

from django.db import models

from abstract.models import CommonModel,PUBLISH_BASE,ADMIN_BASE
# Create your models here.

class Status(CommonModel,ADMIN_BASE):
    name=models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    @staticmethod
    def verbose():
        return u'状态'

class Type(CommonModel,ADMIN_BASE):
    name=models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    @staticmethod
    def verbose():
        return u'类型'

class Step(CommonModel,ADMIN_BASE):
    type=models.ForeignKey(Type)
    name=models.CharField(max_length=50)
    serial=models.IntegerField()

    def __unicode__(self):
        return self.name

    @staticmethod
    def verbose():
        return u'步骤'


class Mission(CommonModel,PUBLISH_BASE):
    chandao_id=models.CharField(max_length=50)
    version=models.CharField(max_length=100)
    type=models.ForeignKey(Type)
    start_date = models.DateTimeField(blank=True,null=True)
    finish_date = models.DateTimeField(blank=True,null=True)
    last_time = models.IntegerField(blank=True,null=True)
    status=models.ForeignKey(Status)

    def __unicode__(self):
        if self.type=='publish':
            name=self.chandao_id
        else:
            name=self.chandao_id
        return name


    @staticmethod
    def verbose():
        return u'任务'

class Progress(CommonModel,PUBLISH_BASE):
    mission=models.ForeignKey(Mission)
    step=models.ForeignKey(Step)
    serial=models.IntegerField()
    status=models.ForeignKey(Status)
    finish_date = models.DateTimeField(blank=True,null=True)
    last_time = models.IntegerField(blank=True,null=True)
    remark=models.TextField(blank=True)

    @staticmethod
    def verbose():
        return u'任务明细'
    class Meta:
        ordering=['serial']