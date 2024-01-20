from django.urls import path
from . import views
from store.controller import authview, prediction, prediction_symptoms

urlpatterns = [
     path('', views.home, name = 'home'),
     path('support', views.support, name="help_support"),
     path('about-disease', views.about_disease, name="about_disease"),
     path('predict-saved', views.saved, name="saved"),
     path('save_prediction', views.save_prediction, name="save_prediction"),
     path('tips', views.tips, name="tips"),
     

     #auth
     path('register', authview.register, name="register"),
     path('login/', authview.loginpage, name="login"),
     path('logout', authview.logoutpage, name="logout"),
     path('my-profile', authview.my_profile, name="my_profile"),
     path('profile_update', authview.profile_update, name="profile_update"),
     
     
     #predict
     path('prediction', prediction.index, name="prediction_items"),
     #path('prediction/heart', views.heart, name="prediction_heart"),
     path('prediction/heart', prediction.heart, name="heart_prediction"),
     path('prediction/diabetes', prediction.diabetes, name="diabetes_prediction"),
     #path('prediction/brain-tumor', prediction.brain_tumor, name="brain_tumor_prediction"),
     path('prediction/symptoms-to-find-disease', prediction_symptoms.symptoms, name="symptoms_to_prediction"),
     path('prediction/symptoms-predict', prediction_symptoms.predictdisease, name="predictdisease"),
]
    