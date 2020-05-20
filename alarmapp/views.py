from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from tkinter import ttk
import time
import os
from tkinter import messagebox
import speech_recognition as sr
import os
import webbrowser
import pyautogui
import time
from gtts import gTTS
from . models import weblink,subjects,timetable,days,times,Users
# Record Audio
r = sr.Recognizer()
hais="hai.mp3"
tellme="tellme.mp3"
written="written.mp3"
mon="m.mp3"
tue="t.mp3"
wed="w.mp3"
thu="th.mp3"
fri="f.mp3"
ha="have.mp3"
sav="save.mp3"
make="mk.mp3"
ring="alert.mp3"
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def createaudio(p):
    tempaudio="temp.mp3"
    tts=gTTS(p,'en')
    tts.save(tempaudio)
    os.system("mpg123 "+tempaudio)
# Create your views here.
def home(request):
    if request.session.has_key('user'):
        username = request.session['user']
        return render(request, 'home.html', {"username" : username})
    else:
        return render(request, 'home.html')

def sweety(request):
    if request.session.has_key('user'):
        user = request.session['user']
        os.system("mpg123 " + hais)
        while 1==1:   
            with sr.Microphone() as source:
                audio = r.record(source, offset=0, duration = 2)
            try:
                s=r.recognize_google(audio)
                if s.find('sweety')>=0:
                    os.system("mpg123 "+tellme)
                    with sr.Microphone() as source:
                        audio = r.record(source, offset=0, duration=3)
                    st=r.recognize_google(audio)
                    if st.find('good night')>=0:
                        createaudio('goodnight, '+user)
                        break
                    elif st.find('good morning')>=0:
                        createaudio('Goodmorning, '+user)
                    elif st.find('thank you')>=0:
                        createaudio('It is my pleasure, '+user)
                    elif st.find('Monday')>=0:
                        os.system("mpg123 " + mon)
                        os.system("mpg123 " + ha)
                    elif st.find('Tuesday')>=0:
                        os.system("mpg123 "+ tue)
                        os.system("mpg123 " + ha)
                    elif st.find('Wednesday')>=0:
                        os.system("mpg123 "+ wed)
                        os.system("mpg123 " + ha)
                    elif st.find('Thursday')>=0:
                        os.system("mpg123 "+ thu)
                        os.system("mpg123 " + ha)
                    elif st.find('Friday')>=0:
                        os.system("mpg123 "+ fri)
                        os.system("mpg123 " + ha)
                    elif st.find('open')>=0:
                        tokens=st.split(" ")
                        cmd=tokens[1]
                        url=weblink.objects.filter(user=user,cmd=cmd).first()
                        webbrowser.get(chrome_path).open(str(url))
                        createaudio('Done')
                    elif st.find('write mode')>=0:
                        createaudio('I will help you while you are writing')
                        write_inst='he'
                        while write_inst != 'over':
                            with sr.Microphone() as source:
                                audio = r.record(source, offset=0, duration=3)
                            try:
                                if write_inst != 'over':
                                    write_inst=r.recognize_google(audio)
                                    pyautogui.typewrite(write_inst)
                                    pyautogui.press('enter')
                            except:
                                pass
                        createaudio('Good work sir')    
                    elif st.find('read mode')>=0:
                        createaudio('I will help you while you are reading')
                        read_inst='he'
                        while read_inst != 'over':
                            with sr.Microphone() as source:
                                audio = r.record(source, offset=0, duration=2)
                            print(read_inst)
                            try:
                                read_inst=r.recognize_google(audio)
                                if read_inst == 'top':
                                    pyautogui.scroll(400)
                                elif read_inst == 'down':
                                    pyautogui.scroll(-400)
                            except:
                                pass
                        createaudio('Good work sir')
                    elif st.find('notification')>=0:
                        pyautogui.click(1900,1728)
                    elif st.find('sleep')>=0:
                        createaudio('How much time can i sleep,sir')
                        with sr.Microphone() as source:
                            audio = r.record(source, offset=0, duration=3)
                        times=r.recognize_google(audio)
                        createaudio('I am going to sleep, sir')
                        time.sleep(int(times))
                        createaudio('I woke up ,sir')
                        os.system("mpg123 " + ring)
                    elif st.find('message')>=0:
                        file=open("message.txt","w")
                        os.system("mpg123 " + make)
                        p='hello'
                        while p!='ok':
                            with sr.Microphone() as source:
                                audio = r.record(source, offset=0, duration=5)
                            p=r.recognize_google(audio)
                            os.system("mpg123 " + written)
                            file.write(p)
                        file.close()
                        os.system("mpg123 " + sav)
                        os.system("notepad.exe "+"message.txt")
                    else:
                        webbrowser.get(chrome_path).open('https://www.google.com/search?gs_ivs=1&q='+st)
            except sr.UnknownValueError:
                temps=9
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return render(request,'home.html',{"username":user})
    else:
        return HttpResponseRedirect('/')

def timetables(request):
    if request.session.has_key('user'):
        user = request.session['user']
        d1=days()
        d1.name='Monday'
        d2=days()
        d2.name='Tuesday'
        d3=days()
        d3.name='Wednesday'
        d4=days()
        d4.name='Thursday'
        d5=days()
        d5.name='Friday'
        alldays=[d1,d2,d3,d4,d5]
        t1=times()
        t1.timeing='eight_to_nine'
        t1.timenum='8 to 9'
        t2=times()
        t2.timeing='nine_to_ten'
        t2.timenum='9 to 10'
        t3=times()
        t3.timeing='ten_to_eleven'
        t3.timenum='10 to 11'
        t4=times()
        t4.timeing='eleven_to_twelve'
        t4.timenum='11 to 12'
        t5=times()
        t5.timeing='twelve_to_one'
        t5.timenum='12 to 1'
        t6=times()
        t6.timeing='two_to_three'
        t6.timenum='2 to 3'
        t7=times()
        t7.timeing='three_to_four'
        t7.timenum='3 to 4'
        t8=times()
        t8.timeing='four_to_five'
        t8.timenum='4 to 5'
        alltimes=[t1,t2,t3,t4,t5,t6,t7,t8]
        allsubjects=subjects.objects.filter(user=user)
        timetable_list=timetable.objects.filter(user=user)
        return render(request,"timetable.html",{'allsubjects':allsubjects,'alltimes':alltimes,'alldays':alldays,'timetable_list':timetable_list})
    else:
        return HttpResponseRedirect('/')
def modify_timetable(request):
    if request.session.has_key('user'):
        user = request.session['user']
        u_day_name=request.GET["day_name"]
        eight_to_nine=request.GET["eight_to_nine"]
        nine_to_ten=request.GET["nine_to_ten"]
        ten_to_eleven=request.GET["ten_to_eleven"]
        eleven_to_twelve=request.GET["eleven_to_twelve"]
        twelve_to_one=request.GET["twelve_to_one"]
        two_to_three=request.GET["two_to_three"]
        three_to_four=request.GET["three_to_four"]
        four_to_five=request.GET["four_to_five"]
        time_table=timetable.objects.filter(user=user,day_name=u_day_name)
        if not time_table :
            timetable.objects.create(user=user,day_name=u_day_name,eight_to_nine=eight_to_nine,nine_to_ten=nine_to_ten,ten_to_eleven=ten_to_eleven,eleven_to_twelve=eleven_to_twelve,twelve_to_one=twelve_to_one,two_to_three=two_to_three,three_to_four=three_to_four,four_to_five=four_to_five)
        else:
            timetable.objects.filter(user=user,day_name=u_day_name).update(eight_to_nine=eight_to_nine,nine_to_ten=nine_to_ten,ten_to_eleven=ten_to_eleven,eleven_to_twelve=eleven_to_twelve,twelve_to_one=twelve_to_one,two_to_three=two_to_three,three_to_four=three_to_four,four_to_five=four_to_five)
        audio_string=" "
        if eight_to_nine!='None':
            audio_string+="8 to 9"+eight_to_nine
        if nine_to_ten!='None':
            audio_string+="9 to 10"+nine_to_ten
        if ten_to_eleven!='None':
            audio_string+="10 to 11"+ten_to_eleven
        if eleven_to_twelve!='None':
            audio_string+="11 to 12"+eleven_to_twelve
        if twelve_to_one!='None':
            audio_string+="12 to 1"+twelve_to_one
        if two_to_three!='None':
            audio_string+="2 to 3"+two_to_three
        if three_to_four!='None':
            audio_string+="3 to 4"+three_to_four
        if four_to_five!='None':
            audio_string+="4 to 5"+four_to_five
        tts=gTTS(audio_string,'en')
        if u_day_name=='Monday':
            tts.save(mon)
            os.system("mpg123 "+mon)
        if u_day_name=='Tuesday':
            tts.save(tue)
            os.system("mpg123 "+tue)
        if u_day_name=='Wednesday':
            tts.save(wed)
            os.system("mpg123 "+wed)
        if u_day_name=='Thursday':
            tts.save(thu)
            os.system("mpg123 "+thu)
        if u_day_name=='Friday':
            tts.save(fri)
            os.system("mpg123 "+fri)
        return HttpResponse("<script>alert('Updated');</script>")
    else:
        return HttpResponseRedirect('/')
def subject(request):
    if request.session.has_key('user'):
        user = request.session['user']
        allsubjects=subjects.objects.filter(user=user)
        return render(request,"subjects.html",{'allsubjects':allsubjects})
    else:
        return HttpResponseRedirect('/')
def add_subject(request):
    if request.session.has_key('user'):
        user = request.session['user']
        allsubjects=subjects.objects.filter(user=user)
        subject_name=request.GET["subject_name"]
        subjects.objects.create(user=user,subject=subject_name)
        return HttpResponseRedirect('/subject')
    else:
        return HttpResponseRedirect('/')
def delete_subject(request):
    if request.session.has_key('user'):
        user = request.session['user']
        subject_name=request.GET["subject_name"]
        subjects.objects.filter(user=user,subject=subject_name).delete()
        return HttpResponseRedirect('/subject')
    else:
        return HttpResponseRedirect('/')
def show_urls(request):
    if request.session.has_key('user'):
        user = request.session['user']
        weblink_list=weblink.objects.filter(user=user)
        return render(request,"urls.html",{'weblink_list':weblink_list})
    else:
        return HttpResponseRedirect('/')
def add_url(request):
    if request.session.has_key('user'):
        new_cmd=request.GET["new_cmd"]
        new_url=request.GET["new_url"]
        user = request.session['user']
        weblink.objects.create(user=user,cmd=new_cmd,url=new_url)
        return HttpResponseRedirect('/show_urls')
    else:
        return HttpResponseRedirect('/')
def delete_url(request):
    if request.session.has_key('user'):
        user = request.session['user']
        cmd_name=request.GET["cmd_name"]
        weblink.objects.filter(user=user,cmd=cmd_name).delete()
        return HttpResponseRedirect('/show_urls')
    else:
        return HttpResponseRedirect('/')
def register(request):
    if request.method == 'POST':
        username=request.POST["username"]
        pwd=request.POST["pwd"]
        user=User.objects.filter(username=username)
        if user is not None:
            messages.info(request,'User Already Exisits')
            return HttpResponseRedirect('/register')
        else:
            user=User.objects.create_user(username=username,password=pwd)
            user.save()
            return  HttpResponseRedirect('/login')

    else:
        return  render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username=request.POST["username"]
        pwd=request.POST["pwd"]
        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            request.session['user'] = username
            auth.login(request,user)
            createaudio('Hi '+username)
            return HttpResponseRedirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return  HttpResponseRedirect('/login')
    else:
        return render(request,"login.html")
def logout(request):
    try:
        del request.session['user']
    except:
        pass
    auth.logout(request)
    createaudio('I miss you sir')
    return  HttpResponseRedirect('/')