from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Reqi_holy
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
global r1,r2
r1="0"
r2="0"
def pm1(request):
	global r1,r2
	r2=Reqi_holy.objects.filter(see='جديد')
	e2=Reqi_holy.objects.filter(see='قديم',signing=str(request.user))
	r1=len(e2)
	#print(len(e))
	return render(request,'pm1.html',{"num":len(r2),"im":r1})
def login1(request):
	global r1,r2
	if request.method=='POST':
		emal=request.POST.get("gmail1")
		pas=request.POST.get("p2")
		if emal=='' or pas=='':
			messages.info(request,"خطا في تسجيل الدخول")
			return redirect("/")
		user = authenticate(request, username=emal, password=pas)
		if user is not None:
			login(request, user)
			messages.info(request,"تم تسجيل الدخول")
			return redirect("/")
		else:
			messages.info(request,"خطاء في كلمة المرور او اسم المستخدم")
			return redirect("/")
def logout1(request):
	
	logout(request)
	messages.info(request,"تم تسجبل الخروج")
	return redirect("/")

def req_holy(request):
	global r1,r2
	e=Reqi_holy.objects.filter(see='جديد')
	if request.method=='POST': #and request.is_ajax():
		sir=request.POST['to_sir']
		typ=request.POST['typ_ho']
		res=request.POST['reso']
		num=request.POST['num_day']
		date_s=request.POST['date_st']
		adre=request.POST['adress']
		name_f=request.POST['name_full']
		dgre=request.POST['dgree']
		sig=request.POST['sign']
		form_tab=Reqi_holy(name_sir=sir,typ_holy=typ,reson=res,num_day=num,date_start=date_s,address=adre,full_name=name_f,order=dgre,signing=sig)
		form_tab.save()
		JsonResponse({"num": len(r2),"um":"تم ارسال الطلب بنجاح"})
		#JsonResponse({"num": len(r2),"im":r1}, status=200)
	return render(request,'reqired_holy.html',{"num":len(r2),"im":r1})
def show_req(request):
	global r1,r2
	e=Reqi_holy.objects.filter(see='جديد')
	if str(request.user)=="admin":
		sh1=Reqi_holy.objects.filter(see="جديد")
		sh2=Reqi_holy.objects.filter(see="قديم")
		return render(request,'show_reqs.html',{"num":len(r2),"sh1":sh1,"sh2":sh2,"im":r1})
	else:
		messages.info(request,"ليس لديك الصلاحيات الازمة")
		return redirect("/")
def show_msg(request,pro_name):
	global r1,r2
	#g={'pro':get_object_or_404(Reqi_holy,pk=int(pro_name))}
	g={'pro':Reqi_holy.objects.get(pk=(pro_name)),"num":len(r2),"im":r1}
	return render(request,'dony_gree.html',g)
def don_prim(request):
	global r1,r2
	if request.method=='POST':
		check=request.POST['ch']
		id_req=(request.POST['sig'])
		if str(check)=='yes':
			Reqi_holy.objects.filter(pk=(id_req)).update(agree='قبول',see='قديم')
		else:
			Reqi_holy.objects.filter(pk=(id_req)).update(agree='رفض',see='قديم')
		messages.info(request,"تم ارسال الطلب")
	return redirect("show_req")
			
def acceptes(request):
	
	global r1,r2
	e=Reqi_holy.objects.filter(see='قديم',signing=str(request.user))
	r1=len(e)
	#for w in e:
		#if str(request.user)==w.signing:
			#r='ok'
		#else:
			#r='no'
	return 	render(request,'accepts.html',{"im":r1,"num":len(r2),"sho_ac":e})	
def jes(request):
	global r1,r2
	r2=Reqi_holy.objects.filter(see='جديد')
	e2=Reqi_holy.objects.filter(see='قديم',signing=str(request.user))
	r1=len(e2)
	if request.is_ajax():
		return JsonResponse({"num": len(r2),"im":r1}, status=200)
def show_fil(request,pro_id):
	#g={'pro':get_object_or_404(Reqi_holy,pk=int(pro_name))}
	g={'fil':Reqi_holy.objects.get(pk=(pro_id)),"num":len(r2),"im":r1}
	return render(request,'show_fils.html',g)
def dele(request,pro_del):
	Reqi_holy.objects.filter(pk=(pro_del)).delete()
	messages.info(request,"تم الحذف")
	return redirect("acceptes")
				
