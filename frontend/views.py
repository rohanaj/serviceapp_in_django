from django.shortcuts import render,redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from app.models import *
from django.db.models import Prefetch
from .forms import *
from django.contrib.auth import authenticate

def loginui(request):
    if request.method == "GET":
        u = UserLoginForm()
        return render(request,"login.html",{"form":u})
@csrf_exempt
def logout(request):
    u = UserLoginForm()

    del request.session


    return render(request,"login.html",{"form":u})
@csrf_exempt
def login(request):
    u = UserLoginForm()
    email = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(email=email,password=password)
    if user is not None:
        user1 =User.objects.get(email=email)
        request.session["email1"] = email
        url1 = "http://127.0.0.1:8000/requesttype/"
        r1 = requests.get(url=url1)
        r1 = r1.json()
        print(r1)
        request.session["requesttypeno"] = len(r1)
        url2 = "http://127.0.0.1:8000/state/"
        r2 = requests.get(url=url2)
        r2 = r2.json()
        print(r2)
        url3 = "http://127.0.0.1:8000/api/auth/jwt/create"
        json = {"email":email,"password":password}
        r = requests.post(url=url3,json=json)
        r = r.json()
        print(r)
        request.session["access_token"] = r["access"]
        request.session["refresh_token"] = r["refresh"]
        print(user1.is_staff)
        if user1.is_staff == True:
            return redirect('updaterequestform')
        else:
            return render(request, "newrequest.html", {"listtype": r1, "liststate": r2, "user": user1})
    else:
        return render(request,"login.html",{"Alert":"No user matches the above credentials","form":u})
    #url = "http://127.0.0.1:8000/api/auth/jwt/create"
    #json = {"email":email,"password":password}
    #r = requests.post(url=url,json=json)
    #r = r.json()
    #print(r)
    #request.session["access_token"] = r["access"]
    #request.session["refresh_token"] = r["refresh"]

def newrequestform(request):
    user = User.objects.get(email=request.session["email1"])
    url = "http://127.0.0.1:8000/requesttype/"
    r = requests.get(url=url)
    r = r.json()
    print(r)
    request.session["requesttypeno"] = len(r)
    url = "http://127.0.0.1:8000/state/"
    r2 = requests.get(url=url)
    r2 = r2.json()
    print(r2)
    return render(request,"newrequest.html",{"listtype":r,"liststate":r2,"user":user})

@csrf_exempt
def processnewrequest(request):
        #try:
        url = "http://127.0.0.1:8000/requesttype/"
        r = requests.get(url=url)
        r = r.json()
        print(r)
        notype = len(r)
        listnotype = []
        for i in range(1,notype+1):
            try:
                listnotype.append(request.POST[str(i)])
            except Exception as e:
                print(e)
        print(listnotype)
        requesttype = ','.join(listnotype)
        requestdesc = request.POST.get("requestdesc")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        countrycode = request.POST.get("countrycode")
        number = request.POST.get("number")
        headers = {"Authorization":"JWT {}".format(request.session.get("access_token"))}
        user = User.objects.get(email=request.session.get("email1"))
        print(user)
        requesttypelist = []
        for j in listnotype:
            requesttypelist.append(RequestType.objects.get(requesttype=str(j)).pk)
        statepk = State.objects.get(state=str(state)).pk
        status = Status.objects.get(status="Pending").pk
        json = { "user": user.pk,
            "requesttype": requesttypelist,
            "requestdesc": requestdesc,
            "city": city,
            "state": statepk,
            "pincode": pincode,
            "countrycode": countrycode,
            "phone_number": number,
                 "status":status
            }
        url = "http://127.0.0.1:8000/newrequest/"
        r3 = requests.post(url=url,json=json,headers=headers)
        r3 = r3.json()
        try:
            if r3.get("code") == "token_not_valid":

                json = {
                    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5ODA5MTIyNSwianRpIjoiNmNkODk0NDgyNGNjNDQ0YmE4YjhjNzZkYWJlOTI3OTUiLCJ1c2VyX2lkIjozfQ.OQ9qPsNi1OAnaPu6MeYNC6owWff-KttRL7I6c7wdrus"}
                url = "http://127.0.0.1:8000/api/auth/jwt/refresh"
                r1 = requests.post(url=url, json=json)
                print(r1.json())
                r1 = r1.json()
                request.session["access_token"] = r1["access"]
                processnewrequest(request)
        except Exception as e:
            print('e',e)
        else:
            request.session['message'] = r3.get("Success")
            return redirect(updaterequestform)

        #except:
        #print(e)
def updaterequestform(request):

    #rl = RequestList.objects.all()


    user = User.objects.get(email=request.session["email1"])

    r1 = []
    if user.is_staff == True:
        r1 = RequestList.objects.all()
    else:
        r1 = RequestList.objects.filter(user=user)



    return render(request,"updaterequestform.html",{"r1":r1,"user":user})

@csrf_exempt
def updaterequestsingle(request,id):
    print(id)
    #print(RequestList.objects.filter(pk=id))
    r1 = []
    context = {}
    context['id'] = request.POST["id"]
    context['updatedby'] = User.objects.get(email=request.POST.get("updatedby"))
    context['requesttype'] = request.POST["requesttype"]
    context['requestdesc'] = request.POST["requestdesc"]
    context['city'] = request.POST["city"]
    context['state'] = request.POST["state"]
    context['countrycode'] = request.POST["countrycode"]
    context['phone_number'] = request.POST["phone_number"]
    context['status'] = request.POST["status"]
    context['remarks'] = request.POST["remarks"]
    context['pincode'] =request.POST["pincode"]
    st1 = []
    st1 = Status.objects.all()
    context["st1"] = st1
    return render(request,"updaterequestsingle.html",context)



@csrf_exempt
def processupdaterequest(request,id):
    status = request.POST["status"]
    remarks = request.POST["remarks"]
    user = User.objects.get(email=request.session.get("email1"))
    updated_by = user.pk
    statuspk = Status.objects.get(status=status).pk

    json2 = {"status": statuspk, "remarks":remarks , "updated_by": updated_by}
    headers = {"Authorization":"JWT {}".format(request.session.get("access_token"))}
    url = "http://127.0.0.1:8000/updaterequest/{}".format(id)
    r = requests.put(url=url, json=json2,headers=headers)
    r = r.json()
    print(r)
    try:
        if r.get("code") == "token_not_valid":

            json = {
                "refresh": request.session["refresh_token"]}
            url = "http://127.0.0.1:8000/api/auth/jwt/refresh"
            r1 = requests.post(url=url, json=json)
            print(r1.json())
            r1 = r1.json()
            request.session["access_token"] = r1["access"]
            processupdaterequest(request,id)
    except Exception as e:
        print(e)
    request.session["Success"] = r
    return redirect('updaterequestform')
def register(request):

    return render(request,"register.html")

@csrf_exempt
def processregister(request):
    u = UserLoginForm()
    phone = request.POST["phone"]
    email = request.POST["email"]
    password = request.POST["password"]
    password2 =request.POST["password2"]
    if password != password2:
        return render(request,"register.html",{"error":"passwords dont match"})
    username = request.POST.get("username")
    url = "http://127.0.0.1:8000/api/auth/users/"
    r = requests.post(url=url,json={"username":username,"phone_number":phone,"email":email,"password":password})
    r = r.json()
    if r.get("email") == email:
        return render(request,"login.html",{"form":u,"error":"User Created Success"})
    else:
        return render(request,"register.html",{"error":r})