from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.core import validators
from .models import *

class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	# captcha = ReCaptchaField(
	#  		public_key='6LeOf6gZAAAAAEhF_mpSKjhzja5AhMKzRkA6juaN',
 #    		private_key='6LeOf6gZAAAAAJ1oZhZ5dR7zrV_neiHJ2Fh2dp5R',
 #    		widget=ReCaptchaV2Checkbox
	#  	)
	
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password1",
			"password2"
		]

class ProfilForm(forms.ModelForm):
	no_ktp = forms.CharField(min_length=15, max_length=16)
	no_hp = forms.CharField(min_length=11, max_length=15)

	class Meta:
		model = Profil
		fields = [
			"no_ktp",
			"no_hp"
		]

class Captcha(forms.Form):
	captcha = ReCaptchaField(
	 		public_key='6LeOf6gZAAAAAEhF_mpSKjhzja5AhMKzRkA6juaN',
    		private_key='6LeOf6gZAAAAAJ1oZhZ5dR7zrV_neiHJ2Fh2dp5R',
    		widget=ReCaptchaV2Checkbox
	 	)

class MagangForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	no_hp = forms.CharField(min_length=11, max_length=15)

	class Meta:
		model = Magang
		fields = [
			"nama",
			"sekolah",
			"email",
			"no_hp",
			"periode",
			"surat"
		]

class LamaranForm(forms.ModelForm):
	CHOICES = [('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')]
	jenis_kelamin = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
	email = forms.EmailField(required=True)
	
	class Meta:
		model = Lamaran
		fields = [
			"foto",
			"nama",
			"email",
			"no_hp",
			"tempat_lahir",
			"tanggal_lahir",
			"jenis_kelamin",
			"alamat",
			"transkrip",
			"ijazah",
			"cv"
		]