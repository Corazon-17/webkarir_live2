from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    no_ktp = models.CharField(max_length=16, unique=True)
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Keahlian(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Lowongan(models.Model):
    keahlian = models.ForeignKey(Keahlian, on_delete=models.CASCADE)
    detail = models.TextField()

    def __str__(self):
        return self.keahlian.nama

    def get_detail(self):
        return reverse('web:detail', kwargs={"id": self.id})

class Lamaran(models.Model):
    lowongan = models.ForeignKey(Lowongan, on_delete=models.CASCADE)
    pelamar = models.ForeignKey(Profil, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='foto/')
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=15)
    alamat = models.CharField(max_length=200)
    transkrip = models.FileField(upload_to='transkrip/')
    ijazah = models.FileField(upload_to='ijazah/')
    cv = models.FileField(upload_to='cv/')

    def __str__(self):
        return self.lowongan.keahlian.nama

class Jurusan(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Magang(models.Model):
	pemohon = models.ForeignKey(Profil, on_delete=models.CASCADE)
	jurusan = models.CharField(max_length=20)
	nama = models.CharField(max_length=300)
	sekolah = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	no_hp = models.CharField(max_length=15)
	periode = models.CharField(max_length=30)
	surat = models.FileField(upload_to='surat/')

	def __str__(self):
		return self.jurusan
