from django.urls import path

from .import views
from .views import *
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('logout/',views.logout,name='logout'),
    path('UploadDataset/',views.UploadDataset,name='UploadDataset'),
    path('UploadDatasetAction', views.UploadDatasetAction, name="UploadDatasetAction"),
    path('PreprocessDataset/',views.PreprocessDataset,name='PreprocessDataset'),
    path('TrainML/',views.TrainML,name='TrainML'),
    path('FakeCurrencyDetection/',views.FakeCurrencyDetection,name='FakeCurrencyDetection'),
    path('FakeDetectionAction/', views.FakeDetectionAction, name="FakeDetectionAction"),
    path('SignupAction', views.SignupAction, name="SignupAction"),
]
