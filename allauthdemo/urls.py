"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
  1. Add an import:  from my_app import views
  2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
  1. Add an import:  from other_app.views import Home
  2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
  1. Import the include() function: from django.conf.urls import url, include
  2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from .auth.views import account_profile
from .views import member_index, member_action
from demo import views 
urlpatterns = [
    # Landing page area
    url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),
    
    #Library fine area
    url(r'^library/new/$', views.library_fine_new, name='library_fine_new'),
    url(r'^library-fine/(?P<pk>\d+)/$', views.library_fine_print, name='library_fine_print'),
    # Download pdf of library fine
    url(r'^library-fine/(?P<pk>\d+)/pdf/$', views.library_fine_pdf, name='download_library_fine_pdf'),

    #Shahparan Hall
    url(r'^hall/new/$', views.shahparan_hall_new, name='shahparan_hall_new'),
    url(r'^shahparan-hall/(?P<pk>\d+)/$', views.shahparan_hall_print, name='shahparan_hall_print'),
    url(r'^shahparan-hall/(?P<pk>\d+)/pdf/$', views.library_fine_pdf, name='download_shahparan_pdf'),

   #Transcript
    url(r'^transcript/new/$', views.transcript_new, name='transcript_new'),
    url(r'^transcript/(?P<pk>\d+)/$', views.transcript_print, name='transcript_print'),
    url(r'^transcript/(?P<pk>\d+)/pdf/$', views.transcript_pdf, name='download_transcript_pdf'),

    #Gradesheet
    url(r'^gradesheet/new/$',views.gradesheet_new, name='gradesheet_new'),
    url(r'^gradesheet/(?P<pk>\d+)/$', views.gradesheet_print, name='gradesheet_print'),
    url(r'^gradesheet/(?P<pk>\d+)/pdf/$', views.gradesheet_pdf, name='download_gradesheet_pdf'),

    #Cash
    url(r'^cashmemo/new/$', views.cash_memo_new, name='cash_memo_new'),
    url(r'^cashmemo/(?P<pk>\d+)/$', views.cashmemo_print, name='cashmemo_print'),
    url(r'^cashmemo/(?P<pk>\d+)/pdf/$', views.cashmemo_pdf, name='download_cashmemo_pdf'),

    #STD 2
    url(r'^s2/new/$', views.S_2_new, name='s_2_new'),
    url(r'^s2/(?P<pk>\d+)/$', views.s2_print, name='s2_print'),
    url(r'^s2/(?P<pk>\d+)/pdf/$', views.s2_pdf, name='download_s_2_pdf'),

    #STD 6
    url(r'^std6/new/$', views.STD_6_new, name='std_6_new'),
    url(r'^std6/(?P<pk>\d+)/$', views.std6_print, name='std6_print'),
    url(r'^std6/(?P<pk>\d+)/pdf/$', views.std6_pdf, name='download_std_6_pdf'),
   
    # Account management is done by allauth
    url(r'^accounts/', include('allauth.urls')),

    # Account profile and member info done locally
    url(r'^accounts/profile/$', account_profile, name='account_profile'),
    url(r'^member/$', member_index, name='user_home'),
    url(r'^member/action$', member_action, name='user_action'),

    # Usual Django admin
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
