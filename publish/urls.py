from django.conf.urls import include, url
# from django.contrib import admin
from publish import views
from publish.forms import LoginForm
# from info_api.models import List
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$',views.index,name='index'),
    ### status
    url(r'^status/$',login_required(views.Status_ListViewSet.as_view()),name='status-list'),
    url(r'^status/update/(?P<pk>\d+)/$',login_required(views.Status_UpdateViewSet.as_view()),name='status-update'),
    url(r'^status/create/$',login_required(views.Status_CreateViewSet.as_view()),name='status-create'),

    # ### type
    url(r'^type/$', login_required(views.Type_ListViewSet.as_view()), name='type-list'),
    url(r'^type/update/(?P<pk>\d+)/$', login_required(views.Type_UpdateViewSet.as_view()), name='type-update'),
    url(r'^type/create/$', login_required(views.Type_CreateViewSet.as_view()), name='type-create'),
    #
    # ### step
    url(r'^step/$', login_required(views.Step_ListViewSet.as_view()), name='step-list'),
    url(r'^step/update/(?P<pk>\d+)/$', login_required(views.Step_UpdateViewSet.as_view()), name='step-update'),
    url(r'^step/create/$', login_required(views.Step_CreateViewSet.as_view()), name='step-create'),
    #
    # ### mission
    url(r'^mission/$', login_required(views.Mission_ListViewSet.as_view()), name='mission-list'),
    url(r'^mission/update/(?P<pk>\d+)/$', login_required(views.Mission_UpdateViewSet.as_view()), name='mission-update'),
    url(r'^publish/mission/create/$', login_required(views.Publish_Mission_CreateViewSet.as_view()), name='publish-mission-create'),
    #
    url(r'^mission/done/(?P<mission_id>\d+)/$', login_required(views.Mission_done), name='mission-done'),
    url(r'^mission/failed/(?P<mission_id>\d+)/$', login_required(views.Mission_failed), name='mission-failed'),
    #
    # ### mission
    url(r'^progress/done/(?P<progress_id>\d+)/$', login_required(views.Progress_done), name='progress-done'),
    url(r'^progress/failed/(?P<progress_id>\d+)/$', login_required(views.Progress_failed), name='progress-failed'),
    url(r'^progress/create/(?P<mission_id>\d+)/$', login_required(views.Generate_progress), name='progress-create'),
    url(r'^progress/$', login_required(views.Progress_ListViewSet.as_view()), name='progress-list'),
    #
    # ### project
    # url(r'^site/$', login_required(views.Site_ListViewSet.as_view()), name='site-list'),
    # url(r'^site/update/(?P<pk>\d+)/$', login_required(views.Site_UpdateViewSet.as_view()), name='site-update'),
    # url(r'^site/create/$', login_required(views.Site_CreateViewSet.as_view()), name='site-create'),
    # url(r'^site/delete/(?P<pk>\d+)/$', login_required(views.Site_DeleteViewSet.as_view()), name='site-delete'),
    #
    # ### upstream
    # url(r'^upstream/$', login_required(views.Upstream_ListViewSet.as_view()), name='upstream-list'),
    # url(r'^upstream/update/(?P<pk>\d+)/$', login_required(views.Upstream_UpdateViewSet.as_view()), name='upstream-update'),
    # url(r'^upstream/create/$', login_required(views.Upstream_CreateViewSet.as_view()), name='upstream-create'),
    # url(r'^upstream/delete/(?P<pk>\d+)/$', login_required(views.Upstream_DeleteViewSet.as_view()), name='upstream-delete'),
    #
    # ### context
    # url(r'^context/$', login_required(views.Site_context_ListViewSet.as_view()), name='context-list'),
    # url(r'^context/update/(?P<pk>\d+)/$', login_required(views.Site_context_UpdateViewSet.as_view()),
    #     name='context-update'),
    # url(r'^context/create/$', login_required(views.Site_context_CreateViewSet.as_view()), name='context-create'),
    # url(r'^context/delete/(?P<pk>\d+)/$', login_required(views.Site_context_DeleteViewSet.as_view()),
    #     name='context-delete'),
    #
    # # ### publish
    # url(r'^fun/$', login_required(views.Fun_queryView), name='fun-query'),
    # url(r'^mission/$', login_required(views.Tran_missionViewSet.as_view()), name='mission-list'),
    # url(r'^create-mission/(?P<site_id>\d+)/$', login_required(views.Create_tran_mission), name='create-mission'),
    # #
    # # ### version
    # # url(r'^version/$', login_required(views.Version_historyViewSet.as_view()), name='version-list'),
    # # url(r'^progress/$', login_required(views.Progress_ViewSet.as_view()), name='progress-list'),
    # # #
    # url(r'^detail/(?P<site_id>\d+)/$', login_required(views.Get_detail), name='get-detail'),
    #
    # url(r'^conf/(?P<site_id>\d+)/$', login_required(views.Generate_conf), name='get-conf'),
    #
    # url(r'^check-conf/(?P<site_id>\d+)/$', login_required(views.Conf_check), name='check-conf'),
    # url(r'^run/(?P<mission_id>\d+)/$', login_required(views.Run_mission), name='run-mission'),
    # # #
    # # url(r'^reset/(?P<job_id>\d+)/$', login_required(views.reset_job), name='reset-job'),

    url(r'^login/$',
        login,
        {
            'template_name': 'webui/login.html',
            'authentication_form': LoginForm,

        },
        name='login',),

    # Django Select2
    url(r'^select2/', include('django_select2.urls')),

    url(r'^logout/$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),]
