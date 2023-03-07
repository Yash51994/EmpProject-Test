from django.urls import path
from app1.views import *


urlpatterns = [
    path('show-data/', show_data, name='show_data'),

]

