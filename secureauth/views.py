from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse
from .forms import SignUpForm
from .models import Profile
#import pdb, requests
from django.conf import settings
from datetime import datetime 
import hashlib
from django.conf import settings
import os
from PIL import Image
import random, string

def img_auth(request):

  if request.user.is_authenticated:

      ids = request.user.id
      Files_all = Filess.objects.filter(userid=ids)       
      return render(request, "viewfile.html", {'main': Files_all} )       

  else:

     return redirect('/login')

def divimg(request):

    if request.method == 'GET':

        parts = request.GET.get("parts", None) 
        username = request.GET.get("username", None)
        password = request.GET.get("password", None)
        filename = request.GET.get("filename", None)
        user_id = request.GET.get("user_id", None)   
        
        extend = filename.split('.') 
        first_extension = extend[0]
        extension = extend[1]
        file_path = os.path.join(settings.BASE_DIR, 'secureauth\\static\\static_files', filename)
        file_path_parts = os.path.join(settings.BASE_DIR, 'secureauth\\static\\static_files')
      
        if parts == '4' :

           img = Image.open(file_path) 
           width, height = img.size 

           area1 = (0, 0, width/2, height/2) 
           img1 = img.crop(area1)
           random_str1 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename1 = first_extension+"_"+random_str1+"."+extension
           save_file1 = file_path_parts+"\\"+filename1
           img1.save(save_file1) 

           area2 = (width/2, 0, width, height/2) 
           img2 = img.crop(area2) 
           random_str2 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename2 = first_extension+"_"+random_str2+"."+extension
           save_file2 = file_path_parts+"\\"+filename2                   
           img2.save(save_file2)
        
           area3 = (0, height/2, width/2, height) 
           img3 = img.crop(area3)      
           random_str3 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename3 = first_extension+"_"+random_str3+"."+extension
           save_file3 = file_path_parts+"\\"+filename3   
           img3.save(save_file3)

           area4 = (width/2, height/2, width, height) 
           img4 = img.crop(area4)
           random_str4 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename4 = first_extension+"_"+random_str4+"."+extension
           save_file4 = file_path_parts+"\\"+filename4                     
           img4.save(save_file4) 

           upd_str = filename1+"-"+filename2+"-"+filename3+"-"+filename4

           profile_obj = Profile.objects.get(user_id=user_id)
           profile_obj.identify_file = upd_str 
           profile_obj.status_file = "yes"
           profile_obj.save()

           data = {
             'file1': filename1,
             'file2': filename2,
             'file3': filename3,
             'file4': filename4,
             'username': username,
             'password': password,
             'parts': parts
           }

        elif parts == '9' :   

           img = Image.open(file_path) 
           width, height = img.size 

           area1 = (0, 0, width/3, height/3) 
           img1 = img.crop(area1)
           random_str1 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename1 = first_extension+"_"+random_str1+"."+extension
           save_file1 = file_path_parts+"\\"+filename1
           img1.save(save_file1) 

           area2 = (width/3, 0, width*(2/3), height/3) 
           img2 = img.crop(area2) 
           random_str2 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename2 = first_extension+"_"+random_str2+"."+extension
           save_file2 = file_path_parts+"\\"+filename2                   
           img2.save(save_file2)
        
           area3 = (width*(2/3), 0, width, height/3) 
           img3 = img.crop(area3)      
           random_str3 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename3 = first_extension+"_"+random_str3+"."+extension
           save_file3 = file_path_parts+"\\"+filename3   
           img3.save(save_file3)

           area4 = (0, height/3, width/3, height*(2/3)) 
           img4 = img.crop(area4)
           random_str4 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename4 = first_extension+"_"+random_str4+"."+extension
           save_file4 = file_path_parts+"\\"+filename4                     
           img4.save(save_file4) 

           area5 = (width/3, height/3, width*(2/3), height*(2/3)) 
           img5 = img.crop(area5)
           random_str5 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename5 = first_extension+"_"+random_str5+"."+extension
           save_file5 = file_path_parts+"\\"+filename5                     
           img5.save(save_file5)

           area6 = (width*(2/3), height/3, width, height*(2/3)) 
           img6 = img.crop(area6)
           random_str6 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename6 = first_extension+"_"+random_str6+"."+extension
           save_file6 = file_path_parts+"\\"+filename6                    
           img6.save(save_file6)

           area7 = (0, height*(2/3), width/3, height) 
           img7 = img.crop(area7)
           random_str7 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename7 = first_extension+"_"+random_str7+"."+extension
           save_file7 = file_path_parts+"\\"+filename7                    
           img7.save(save_file7)

           area8 = (width/3, height*(2/3), width*(2/3), height) 
           img8 = img.crop(area8)
           random_str8 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename8 = first_extension+"_"+random_str8+"."+extension
           save_file8 = file_path_parts+"\\"+filename8                    
           img8.save(save_file8)

           area9 = (width*(2/3), height*(2/3), width, height) 
           img9 = img.crop(area9)
           random_str9 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
           filename9 = first_extension+"_"+random_str9+"."+extension
           save_file9 = file_path_parts+"\\"+filename9                   
           img9.save(save_file9)

           upd_str = filename1+"-"+filename2+"-"+filename3+"-"+filename4+"-"+filename5+"-"+filename6+"-"+filename7+"-"+filename8+"-"+filename9

           profile_obj = Profile.objects.get(user_id=user_id)
           profile_obj.identify_file = upd_str 
           profile_obj.status_file = "yes"
           profile_obj.save()

           data = {
             'file1': filename1,
             'file2': filename2,
             'file3': filename3,
             'file4': filename4,
             'file5': filename5,
             'file6': filename6,
             'file7': filename7,
             'file8': filename8,
             'file9': filename9,
             'username': username,
             'password': password,
             'parts': parts
           }          

        return JsonResponse(data)

def checklogin(request):

    if request.method == 'GET':

        src = request.GET.get("src", None) 

        userid = request.GET.get("userid", None)
        
        try:
           profile_obj = Profile.objects.get(user_id=userid,identify_file=src)
           user_obj = User.objects.get(id=userid)
           print(user_obj)
           firstname = user_obj.first_name
           lastname = user_obj.last_name
           email = user_obj.username

           data = {
             'check': 'yes',
             'firstname': firstname,
             'lastname': lastname,
             'email': email
           }

        except Profile.DoesNotExist:   
           data = {
             'check': 'no'
           }

        return JsonResponse(data)           


def register(request):
   return render(request, "signup.html")

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        print(form) 
        if form.is_valid():
            print('here2')
            user = form.save()    
            #pdb.set_trace()
            user.refresh_from_db()  # load the profile instance created by the signal
            filename = form.cleaned_data.get('myfile')
            user.profile.myfile = form.cleaned_data.get('myfile')
            filename = filename.name
            user.profile.identify_file = 'no'
            user.profile.status_file = 'no'
            user.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            data = {}

            data['username'] = username
            data['password'] = password
            data['filename'] = filename

            return render(request, 'signup_img_auth.html', {'main': data})

        else :
          print('here3')
          return render(request, 'signup.html')    
    else:
        
        return render(request, 'signup.html') 

def logins(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
               user_id = User.objects.get(username=username).id
               data_profile = Profile.objects.get(user_id=user_id)
               status = data_profile.status_file
               filename = data_profile.myfile
               status = data_profile.status_file
               identify_file = data_profile.identify_file
               data = {}
               data['username'] = username
               data['password'] = password
               data['filename'] = filename
               data['user_id'] = user_id

               if status == 'no' :
                
                  return render(request, 'signup_img_auth.html', {'main': data})

               else : 

                  arr_files = []
                  arr_file = identify_file.split('-')
                  arr_len = len(arr_file)
                  random.shuffle(arr_file)
                  data['lenths'] = arr_len
                  data['arr_file'] = arr_file
                  return render(request, 'signup_img_auths.html', {'main': data})
               
               #login(request, user)
               #return redirect('/')  
            else:
               return redirect('/login/')   
    else:
         return render(request, 'login.html') 

def logouts(request):
    logout(request)
    return redirect('/login/')

def profile(request):
   
    if request.method == 'GET':
        data = {}

        firstname = request.GET.get("firstname", None) 
        lastname = request.GET.get("lastname", None) 
        email = request.GET.get("email", None) 
        data['firstname'] = firstname
        data['lastname'] = lastname
        data['email'] = email
        
        return render(request, 'profile.html', {'main': data})
