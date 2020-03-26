from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('success/',views.success,name='success'),

]
