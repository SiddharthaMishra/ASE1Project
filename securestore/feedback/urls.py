from django.conf.urls import url
from . import views

app_name = 'feedback'

urlpatterns = [
    url(r'^$', views.feedback_index, name = 'feedback_index'),
    url(r'^submit_feedback/$', views.submit_feedback, name = 'submit_feedback'),
]
