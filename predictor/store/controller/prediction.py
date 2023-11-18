from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse

from django.contrib.auth.decorators import login_required #login must
from joblib import load



@login_required(login_url='login')
def index(request):
    return render(request, "store/prediction/index.html") 


#----------------------------Heart--------------------------
model_heart = load('./machine_deep_models/heart_disease_model.joblib')

def heart(request):
    if request.method == 'POST':
        
        HighBP = int(request.POST.get('HighBP'))
        HighChol = int(request.POST.get('HighChol'))
        CholCheck = int(request.POST.get('CholCheck'))
        BMI = float(request.POST.get('BMI'))
        Smoker = int(request.POST.get('Smoker'))
        Stroke = int(request.POST.get('Stroke'))
        Diabetes = int(request.POST.get('Diabetes'))
        PhysActivity = int(request.POST.get('PhysActivity'))
        Fruits = int(request.POST.get('Fruits'))
        Veggies = int(request.POST.get('Veggies'))
        HvyAlcoholConsump = int(request.POST.get('HvyAlcoholConsump'))
        AnyHealthcare = int(request.POST.get('AnyHealthcare'))
        NoDocbcCost = int(request.POST.get('NoDocbcCost'))
        GenHlth = int(request.POST.get('GenHlth'))
        MentHlth = int(request.POST.get('MentHlth'))
        PhysHlth = int(request.POST.get('PhysHlth'))
        DiffWalk = int(request.POST.get('DiffWalk'))
        Sex = int(request.POST.get('Sex'))
        Age = int(request.POST.get('Age'))
        Education = int(request.POST.get('Education'))
        
        y_pred = model_heart.predict([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Diabetes, PhysActivity, Fruits, Veggies,
                                 HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education]])
        
        if HighBP == 1:
            p_HighBP = 'High Blood Pressure'
        elif HighBP ==0:
            p_HighBP = 'Not High Blood Pressure'
            
        if HighChol == 1:
            p_HighChol = 'High Cholesterol'
        elif HighChol ==0:
            p_HighChol = 'Not High Cholesterol'
            
        if CholCheck == 1:
            p_CholCheck = 'Check Cholesterol'
        elif CholCheck ==0:
            p_CholCheck = 'No Check Cholesterol'
            
        p_BMI = "BMI:" + str(BMI)
        
        if Smoker == 1:
            p_Smoker = 'Smoking'
        elif Smoker ==0:
            p_Smoker = 'No Smoking'
            
        if Stroke == 1:
            p_Stroke = 'Stroke'
        elif Stroke ==0:
            p_Stroke = 'No Stroke'
            
        if Diabetes == 1:
            p_Diabetes = 'Prediabetes'
        elif Diabetes ==0:
            p_Diabetes = 'No Diabetes'
        elif Diabetes ==2:
            p_Diabetes = 'Diabetes'
            
        if PhysActivity == 1:
            p_PhysActivity = 'Physical Activity'
        elif PhysActivity ==0:
            p_PhysActivity = 'No Physical Activity'

        if Fruits == 1:
            p_Fruits = 'Fruits'
        elif Fruits ==0:
            p_Fruits = 'No Fruits'
            
        if Veggies == 1:
            p_Veggies = 'Fruits'
        elif Veggies ==0:
            p_Veggies = 'No Fruits'
            
        if HvyAlcoholConsump == 1:
            p_HvyAlcoholConsump = 'Heavy Alcohol Consum'
        elif HvyAlcoholConsump ==0:
            p_HvyAlcoholConsump = 'No Heavy Alcohol Consum' 
            
        if AnyHealthcare == 1:
            p_AnyHealthcare = 'Health Care'
        elif AnyHealthcare ==0:
            p_AnyHealthcare = 'No Health Care'
            
        if NoDocbcCost == 1:
            p_NoDocbcCost = 'NoDocbcCost Yes'
        elif NoDocbcCost ==0:
            p_NoDocbcCost = 'NoDocbcCost No'
            
        if GenHlth == 1:
            p_GenHlth = 'Health Excellent'
        elif GenHlth ==2:
            p_GenHlth= 'Health Very good' 
        elif GenHlth ==3:
            p_GenHlth = 'Health Good'
        elif GenHlth ==4:
            p_GenHlth = 'Health Fair'
        elif GenHlth ==5:
            p_GenHlth = 'Health Poor' 
            
        p_MentHlth = "Mental Health Bad:" + str(MentHlth) +" Days"
        
        p_PhysHlth = "Physical Health Bad:" + str(PhysHlth)  +" Days"
        
        if DiffWalk == 1:
            p_DiffWalk = 'Difficulty Walking'
        elif DiffWalk ==0:
            p_DiffWalk = 'No Difficulty Walking'  
            
        if Sex == 1:
            p_Sex = 'Male'
        elif Sex ==0:
            p_Sex = 'Female' 
             
        if Age == 1:
            p_Age = 'Age:18-24'
        elif Age ==2:
            p_Age= 'Age:25-29' 
        elif Age ==3:
            p_Age = 'Age:30-34'
        elif Age ==4:
            p_Age = 'Age:35-39'
        elif Age ==5:
            p_Age = 'Age:40-44'
        elif Age ==6:
            p_Age= 'Age:45-49' 
        elif Age ==7:
            p_Age = 'Age:50-54'
        elif Age ==8:
            p_Age = 'Age:55-59'
        elif Age ==9:
            p_Age = 'Age:60-64'
        elif Age ==10:
            p_Age= 'Age:65-69' 
        elif Age ==11:
            p_Age = 'Age:70-74'
        elif Age ==12:
            p_Age = 'Age:75-79'
        elif Age ==13:
            p_Age = 'Age:80 or older'
            
        if Education == 1:
            p_Education = 'Never Attended School or Only Kindergarten'
        elif Education ==2:
            p_Education= 'Grades 1-8 (Elementary)' 
        elif Education ==3:
            p_Education = 'Grades 9-11 (Some High School)'
        elif Education ==4:
            p_Education = 'Grade 12 or GED (High School Graduate)'
        elif Education ==5:
            p_Education = 'College 1 Year To 3 Years (Some College or Ttechnical School)'
        elif Education ==6:
            p_Education= 'College 4 Years or More (College Graduate)'                       
            
        psymptoms = [p_HighBP, p_HighChol, p_CholCheck, p_BMI, p_Smoker, p_Stroke, p_Diabetes, p_PhysActivity, p_Fruits, p_Veggies,
                    p_HvyAlcoholConsump, p_AnyHealthcare, p_NoDocbcCost, p_GenHlth, p_MentHlth, p_PhysHlth, p_DiffWalk, p_Sex, p_Age, p_Education]
        
        if y_pred[0] == 0:
            y_pred = 'Low risk of Heart Disease'
        elif y_pred[0] == 1:
           #y_pred = 'High Risk Of Heart Disease'
           y_pred = 'Heart Disease'
        else:
            y_pred = 'Not Predicted! Something was wrong.'
        return render(request, "store/prediction/diseases/heart/result.html", {'result' : y_pred, 'psymptoms':psymptoms})
    return render(request, "store/prediction/diseases/heart/form.html") 






#----------------------------Diabetes--------------------------
model_diabetes = load('./machine_deep_models/diabetes_disease_model.joblib')

def diabetes(request):
    if request.method == 'POST':
  
        gender =  int(request.POST.get('gender'))
        age = float(request.POST.get('age'))
        hypertension = int(request.POST.get('hypertension'))
        heart_disease = int(request.POST.get('heart_disease'))
        smoking_history = int(request.POST.get('smoking_history'))
        bmi = float(request.POST.get('bmi'))
        HbA1c_level =  float(request.POST.get('HbA1c_level'))
        blood_glucose_level = int(request.POST.get('blood_glucose_level'))
                                
        y_pred = model_diabetes.predict([[gender, age, hypertension, heart_disease, smoking_history, bmi, 
                                 HbA1c_level, blood_glucose_level]])

        #Gender
        if gender == 1:
            p_gender = 'Male'
        elif gender ==0:
            p_gender = 'Female'
        else:
            p_gender = 'Others'
            
        p_age = "Age:" + str(age)
        
        #hypertension
        if hypertension == 1:
            p_hypertension = 'Hypertension'
        elif hypertension ==0:
            p_hypertension = 'No Hypertension'

        #heart_disease
        if heart_disease == 1:
            p_heart_disease = 'Heart Disease'
        elif heart_disease ==0:
            p_heart_disease = 'No Heart Disease'
        
        #smoking_history
        if smoking_history == 0:
            p_smoking_history = 'Smoking No Info'
        elif smoking_history ==1:
            p_smoking_history = 'Smoking Current'
        elif smoking_history ==2:
            p_smoking_history = 'Smoking Ever'
        elif smoking_history ==3:
            p_smoking_history = 'Smoking Former'
        elif smoking_history ==4:
            p_smoking_history = 'Smoking Never'
        elif smoking_history ==5:
            p_smoking_history = 'Smoking Not current'
            
        p_bmi = "BMI:" + str(bmi)
        
        p_HbA1c_level = "HbA1c Level:" + str(HbA1c_level)
        
        p_blood_glucose_level = "Blood Glucose Level:" + str(blood_glucose_level)
            
              
        psymptoms = [p_gender, p_age, p_hypertension, p_heart_disease, p_smoking_history, p_bmi,  p_HbA1c_level, p_blood_glucose_level]

                                        
        if y_pred[0] == 0:
            y_pred = 'Low risk of Diabetics'
        elif y_pred[0] == 1:
           y_pred = 'Diabetics'
        else:
            y_pred = 'Not Predicted! Something was wrong.'
        return render(request, "store/prediction/diseases/diabetes/result.html", {'result':y_pred, 'psymptoms':psymptoms})
    return render(request, "store/prediction/diseases/diabetes/form.html") 



