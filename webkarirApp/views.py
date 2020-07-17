from django.shortcuts import render, Http404, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.views import View


# Create your views here.
def index(request):
    template_name = "index.html"
    return render(request, template_name)

def getKarir(request):
	lowongan = Lowongan.objects.all()
	keahlian = Keahlian.objects.all()
	tersedia = []
	for obj in lowongan:
		tersedia.append(obj.keahlian.nama)

	context = {
		"lowongan": lowongan,
		"keahlian": keahlian,
		"tersedia": tersedia
	}

	return render(request, "karir.html", context)

class getDetail(View):
	def get(self, request, id):
		if request.user.is_authenticated:
			lowongan = get_object_or_404(Lowongan, id=id)
			context = {
				"lowongan": lowongan
			}

			return render(request, "detail.html", context)

		else:
			return redirect('web:login')


class getLamaran(View):
	def get(self, request, id):
		if request.user.is_authenticated:
			user = get_object_or_404(User, id=request.user.id)
			profil = get_object_or_404(Profil, user_id=user.id)
			lowongan = get_object_or_404(Lowongan, id=id)
			form = LamaranForm
			print(LamaranForm)

			try:
			    lamaran = Lamaran.objects.filter(lowongan=lowongan, pelamar=profil).latest("id")
			except Lamaran.DoesNotExist:
			    lamaran = None

			context = {
				"profil": profil,
				"form": form,
				"lowongan": lowongan,
				"lamaran": lamaran
			}

			return render(request, "lamaran.html", context)

		else:
			return redirect('web:login')

	def post(self, request, id):
		if request.user.is_authenticated:
			user = get_object_or_404(User, id=request.user.id)
			profil = get_object_or_404(Profil, user_id=user.id)
			lowongan = get_object_or_404(Lowongan, id=id)
			form = LamaranForm(request.POST, request.FILES)

			if form.is_valid():
				formulir = form.save(commit=False)
				formulir.lowongan = lowongan
				formulir.pelamar = profil
				formulir.save()

				try:
				    lamaran = Lamaran.objects.filter(lowongan=lowongan, pelamar=profil).latest("id")
				except Lamaran.DoesNotExist:
				    lamaran = None

				context = {
					"profil": profil,
					"form": form,
					"lowongan": lowongan,
					"lamaran": lamaran,
					"successful_submit": True
				}

				return render(request, "lamaran.html", context)

			else:
				messages.add_message(request, messages.ERROR, '<h4 class="text-danger">* Data yang anda masukkan tidak sesuai</h4>')
				return redirect('web:lamaran', id=lowongan.id)

def getMagang(request):
	jurusan = Jurusan.objects.all()
	context = {
		"jurusan": jurusan
	}
	return render(request, "magang.html", context)

class getFormulir(View):
	def get(self, request, nama):
		if request.user.is_authenticated:
			user = get_object_or_404(User, id=request.user.id)
			profil = get_object_or_404(Profil, user_id=user.id)
			jurusan = get_object_or_404(Jurusan, nama=nama)
			form = MagangForm
			try:
			    formulir = Magang.objects.filter(jurusan=jurusan, pemohon=profil).latest("id")
			except Magang.DoesNotExist:
			    formulir = None

			context = {
				"jurusan": jurusan,
				"form": form,
				"formulir": formulir
			}

			return render(request, "formulir.html", context)

		else:
			return redirect('web:login')

	def post(self, request, nama):
		if request.user.is_authenticated:
			user = get_object_or_404(User, id=request.user.id)
			profil = get_object_or_404(Profil, user_id=user.id)
			jurusan = get_object_or_404(Jurusan, nama=nama)
			form = MagangForm(request.POST or None, request.FILES or None)

			if form.is_valid():
				formulir = form.save(commit=False)
				formulir.pemohon = profil
				formulir.jurusan = jurusan
				formulir.save()

				try:
				    formulir = Magang.objects.filter(jurusan=jurusan, pemohon=profil).latest("id")
				except Magang.DoesNotExist:
				    formulir = None

				context = {
					"jurusan": jurusan,
					"form": form,
					"formulir": formulir,
					"successful_submit": True
				}

				return render(request, "formulir.html", context)

class getLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('web:index')
        else:
            return render(request, "login.html", {'capt': Captcha()})

    def post(self, request):
        user = request.POST.get('user')
        password = request.POST.get('pass')
        capt = Captcha(request.POST)
        auth = authenticate(request, username=user, password=password)
        if capt.is_valid():
	        if auth is not None:
	            login(request, auth)
	            return render(request, 'login.html', { "successful_submit":True })
	        else:
	            messages.add_message(request, messages.ERROR, 'Username atau Password Salah')
	            return redirect('web:login')
        else :
        	messages.add_message(request, messages.ERROR, 'Klik CAPTCHA terlebih dahulu')
        	return redirect('web:login')

def getLogout(request):
    logout(request)
    return redirect('web:login')

def getRegister(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		profil_form = ProfilForm(request.POST)
		capt = Captcha(request.POST)

		if capt.is_valid():
			if form.is_valid() and profil_form.is_valid():
				user = form.save()
				profil = profil_form.save(commit=False)
				profil.user = user
				profil.save()

				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=password)
				login(request, user)
				form = UserForm()
				profil_form = ProfilForm()
				capt = Captcha()

				context = {
					"form": form,
					"profil_form": profil_form,
					"capt": capt,
					"successful_submit": True
				}

				return render(request, 'register.html', context)
				# return redirect('web:index')

		else:
			messages.add_message(request, messages.ERROR, 'Klik CAPTCHA terlebih dahulu')
			# return redirect('web:register')

	else:
		form = UserForm()
		profil_form = ProfilForm()
		capt = Captcha()

	context = {
		"form": form,
		"profil_form": profil_form,
		"capt": capt
	}

	return render(request, 'register.html', context)