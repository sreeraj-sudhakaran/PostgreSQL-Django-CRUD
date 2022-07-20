from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_data, name='show-data'),
    path('add/', views.add_data, name='add-data'),
    path('show/', views.show_data, name='show-data'),
    path('update/<int:pk>', views.update_data, name='update-data'),
    path('delete/<int:pk>', views.delete_data, name='delete-data'),
    path('top5/', views.top5_data, name='top5-data'),
    path('bottom5/', views.bottom5_data, name='bottom5-data'),
    path('male/', views.StudentMale_data, name='StudentMale-data'),
    path('female/', views.StudentFemale_data, name='StudentFemale-data'),
    path('other/', views.StudentOther_data, name='StudentOther-data'),
    path('dummydata/', views.dummy_data, name='dummy-data'),
    path('deleteall/', views.delete_all, name='delete-all'),
]