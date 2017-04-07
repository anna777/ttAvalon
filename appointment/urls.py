from django.conf.urls import patterns, include, url
from django.contrib import admin
from appointments.views import EventCreateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appointment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^start_page/$', 'appointments.views.start_page', name='start_page'),
    url(r'^start_page/(?P<pk>\d+)/$', 'appointments.views.appointment_page', name='appointment_page'),
    url(r'^start_page/save/$', 'appointments.views.event_member_add', name='event_member_add'),
    url(r'^home/$', EventCreateView.as_view(), name='home'),
    url(r'^login/$', 'appointments.views.login', name='login'),
    url(r'^logout/$', 'appointments.views.logout', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
