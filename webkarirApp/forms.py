from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
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