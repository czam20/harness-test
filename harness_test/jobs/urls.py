from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ListJob.as_view(), name='list_job'),
    path('create/', CreateJob.as_view(), name='create_job'),
    path('<int:pk>/', RetrieveJob.as_view(), name='retrieve_job'),
    path('skills/', CreateSkill.as_view(), name='create_skill'),
    path('skills/count', Skills.as_view(), name='skills'),
]