# #coding=utf8
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *
from .wiget import *

class LoginForm(AuthenticationForm):
    '''Authentication form which uses boostrap CSS.'''
    username = forms.CharField(max_length=255,widget=forms.TextInput({
                                   'class': 'form-control'}))
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput({
                                   'class': 'form-control'}))


class StatusForm(forms.ModelForm):

    name = forms.CharField(label='名字', max_length=50, widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Status
        exclude = ['created_date', 'modified_date']

class TypeForm(forms.ModelForm):
    name = forms.CharField(label='名字', max_length=50, widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Type
        exclude = ['created_date', 'modified_date']

class StepForm(forms.ModelForm):
    name = forms.CharField(label='名字', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    serial = forms.IntegerField(label='顺序', widget=forms.TextInput({'class': 'form-control'}))

    class Meta:

        fields = (
            'type',
            'name',
            'serial',
                )
        model = Step
        widgets = {
            'type':TypeModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']

class MissionForm(forms.ModelForm):
    chandao_id = forms.CharField(label='禅道ID', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    version = forms.CharField(label='版本', max_length=100, widget=forms.TextInput({'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.type=kwargs.pop('type',None)
        # self.creator = kwargs.pop('creator', None)
        # self.last_modified_by = kwargs.pop('last_modified_by', None)
        self.status = kwargs.pop('status',None)

        super(MissionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(MissionForm, self).save(commit=False)
        if self.type:
            instance.type = self.type
        instance.status = self.status
        return instance.save()

    class Meta:
        fields = (
            'chandao_id',
            'version',
        )
        model = Mission
        exclude = ['created_date', 'modified_date','start_date','finish_date','last_time']
#
# class GroupForm(forms.ModelForm):
#
#     name = forms.CharField(label='名字', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
#
#     class Meta:
#         fields = (
#                     'name',
#                     'hosts',
#                 )
#         model = Group
#         widgets = {
#             'hosts':ModelSelect2MultipleWidget,
#         }
#         exclude = ['created_date', 'modified_date']
#
#
#
# class SiteForm(forms.ModelForm):
#
#     name = forms.CharField(label='域名', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
#     https = forms.BooleanField(label='是否为https',required=False)
#     class Meta:
#         fields = (
#             'name',
#             'https',
#             'group'
#         )
#         widgets = {
#             'group':GroupModelSelect2Widget,
#         }
#         model = Site
#         exclude = ['created_date', 'modified_date']
#
# class UpstreamForm(forms.ModelForm):
#     name = forms.CharField(label='组名', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
#     port = forms.CharField(label='端口', required=False,max_length=50, widget=forms.TextInput({'class': 'form-control'}))
#     direct_status = forms.BooleanField(label='是否为代理域名', required=False)
#
#     def save(self, commit=True):
#         instance = super(UpstreamForm, self).save(commit=False)
#         instance.status=Status.objects.get(name='undo')
#         instance.save()
#         # instance.save_m2m()
#         return self.save_m2m()
#
#     class Meta:
#         fields = (
#             'name',
#             'port',
#             'hosts',
#             'direct_status',
#         )
#         widgets = {
#             'hosts': UpstreamModelSelect2MultipleWidget,
#         }
#         model = Upstream
#         exclude = ['created_date', 'modified_date','status']
#
# class Site_contextForm(forms.ModelForm):
#     context = forms.CharField(label='context_path', max_length=200, widget=forms.TextInput({'class': 'form-control'}))
#
#     def save(self, commit=True):
#         instance = super(Site_contextForm, self).save(commit=False)
#         instance.status = Status.objects.get(name='undo')
#         return instance.save()
#
#     class Meta:
#         fields = (
#             'site',
#             'context',
#             'upstream',
#             'extra_parametres',
#         )
#         widgets = {
#             'site': SiteModelSelect2Widget,
#             'upstream': UpstreamSelect2Widget,
#         }
#         model = Site_context
#         exclude = ['created_date', 'modified_date', 'status']
