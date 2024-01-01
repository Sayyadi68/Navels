from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout, login,authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
from django.http import JsonResponse


from story.forms import StoryForm,ChapterForm
from story.models import Chapters,Storys

from .forms import LoginForm, OtpForm, Ticketform
from .models import account,ticet
from django.views import generic

import random
import requests
import threading



def is_ajax(request):
    """
    :param request: get post request
    :return: True if it was ajax request and False for not ajax
    """
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def login_(request):
    if is_ajax(request) and request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            phone_number = form.data['phone_number']

            otp_generate = random.randint(10000, 99999)
            username_generate = random.randint(100000, 9999999)
            username_phone_number = str(phone_number)

            if username_phone_number.startswith('+98'):
                username_phone_number.replace('+98', '0')

            elif username_phone_number.startswith('9'):
                username_phone_number = '0' + username_phone_number

            try:
                user = account.objects.get(phone_number=phone_number)
                user.otp = otp_generate
                user.save()

            except account.DoesNotExist:
                account.objects.create(phone_number=phone_number,username=phone_number, UserID=username_generate, otp=otp_generate)

            threading.Thread(print(otp_generate),args=(phone_number, otp_generate)).start()

            request.session['phone_number'] = str(phone_number)
            request.session['username_phone_number'] = str(username_phone_number)

            return JsonResponse({"success": 'ok'}, safe=False, status=200)

        else:
            return JsonResponse({"error": "شماره تلفن نا معتبر!"}, safe=False, status=400)

    return JsonResponse({"error": "خطایی رخ داده است!"}, safe=False, status=400)
def verify_login(request):
    if is_ajax(request) and request.method == "POST":
        form = OtpForm(request.POST)

        if form.is_valid():
            otp = form.data['otp']
            phone_number = request.session['phone_number']
            username_phone_number = request.session['username_phone_number']

            if user := authenticate(request, phone_number=phone_number, otp=otp, username=username_phone_number):
                login(request=request, user=user, backend='account.backends.OtpBackend')

                messages.success(request, 'با موفقیت وارد شدید.')

                return JsonResponse({"success": 'ok', "success_message": 'با موفقیت وارد شدید.'}, safe=False,
                                    status=200)

            else:
                return JsonResponse({"error": "کد نا معتبر!"}, safe=False, status=400)

    return JsonResponse({"error": "خطایی رخ داده است!"}, safe=False, status=400)

def auth_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, ("شما با موفقیت از حساب خود خارج شدید ..."))

    return redirect('profile')

def Profile(request,pk=-1):

    storys = Storys.objects.all()
    tickets = ticet.objects.all()

    try:
        if pk == -1:
            StoryTitel = Storys.objects.all().first()
            sender = ticet.objects.all().first()

        else:
            StoryTitel = Storys.objects.get(pk=pk)
            sender = ticet.objects.get(pk=pk)
        summery = Storys.objects.filter(StoryTitel=StoryTitel)
        return render(request, 'account/accountuserpanel.html',
                      context={'Storys': storys, 'StoryTitel': StoryTitel, 'summery': summery ,'Tickets': tickets, 'sender': sender})
    except Storys.DoesNotExist:
        pass


def connect(request):
 
    if is_ajax(request) and request.method == "POST":

        form3 = Ticketform(request.POST)
        ticetreson = form3.data['ticetreson']

        if form3.is_valid():
            sender = request.user
            ticet_text = form3.data['ticet_text']

            ticet.objects.create(sender=sender, ticetreson=ticetreson, ticet_text=ticet_text )
            messages.success(request, 'تیکت با موفقیت ارسال شد.')
            return redirect('connect')
    return render(request, 'account/ticket.html' )

def settings(request):
    return render(request, 'account/setting.html' )

def saves(request):
    return render(request, 'account/saves.html' )

def newstory(request):

    if is_ajax(request) and request.method == "POST":
        form1 = StoryForm(request.POST)
        StoryTitel = form1.data['StoryTitel']

        if form1.is_valid():

            Writer = request.user
            ganer = form1.data['ganer']
            summary = form1.data['summary']

            request.session['StoryTitel'] = StoryTitel

            Storys.objects.create(Writer=Writer, StoryTitel=StoryTitel, ganer=ganer, summary=summary)

            messages.success(request, 'داستان نوشته شد.')
            return redirect('newstory')

    return render(request, 'account/craetestory.html' )

