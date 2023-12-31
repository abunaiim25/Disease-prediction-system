from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from .models import *
from store.models import SavePredict
from django.contrib.auth.decorators import login_required #login must

# Create your views here.

def home(request):
    return render(request, 'store/index.html')


def support(request):
    return render(request, 'store/support.html')

def about_disease(request):
    return render(request, 'store/about_disease.html')

@login_required(login_url='login')
def saved(request):
    predict = SavePredict.objects.filter(user=request.user).order_by('-created_at')#descending
    context = {'predict':predict}
    return render(request, 'store/saved.html', context)


@login_required(login_url='login')
def save_prediction(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            save_predict = SavePredict()
            save_predict.user = request.user
            save_predict.symptoms_input = request.POST.get('symptoms_input')
            save_predict.symptoms_result = request.POST.get('symptoms_result')
            save_predict.save()
            messages.success(request, "Saved Successfully")
        else:
            return JsonResponse({'status': "Login to Continue"})
            

    return redirect('/predict-saved')