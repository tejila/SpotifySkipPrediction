from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')
def result(request):
    model=joblib.load('LGB Model new1.sav')
    input=[]
    input.append(request.GET['context_switch'])
    input.append(request.GET['session_length'])
    input.append(request.GET['session_position'])
    input.append(request.GET['no_pause_before_play'])
    input.append(request.GET['hist_user_behavior_is_shuffle'])
    input.append(request.GET['hist_user_behavior_n_seekfwd'])
    input.append(request.GET['hist_user_behavior_n_seekback'])
    input.append(request.GET['hour_of_day'])
    input.append(request.GET['released_year'])
    input.append(request.GET['context_type'])
    input.append(request.GET['premium'])
    input.append(request.GET['hist_user_behavior_reason_start'])
    input.append(request.GET['hist_user_behavior_reason_end'])


    print(input)

    result=model.predict([input])
    print('result is ',result)
    return render(request,'result.html',{'result':result})