from django.shortcuts import render
from datetime import datetime

def show_equipments(request):
    current_time = datetime.now()
    exit_rate = int(request.user.manual_exit_rate)
    if exit_rate == 100:
        reservation_avaliable_time = datetime(current_time.year, current_time.month, current_time.day, 12)
    else:
        reservation_avaliable_time = datetime(current_time.year, current_time.month, current_time.day, 12,10 - (exit_rate // 10))