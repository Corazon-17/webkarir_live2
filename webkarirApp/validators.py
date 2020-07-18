from django.core.exceptions import ValidationError

def pdf_valid(value):
	file_name = value.name
	if '.pdf' not in file_name:
		raise ValidationError("Format File Dokumen Tidak Sesuai (.pdf)")
	else: 
		return True

def max_pdf_size(value):
	file_size = value.size
	if file_size > 1048576:
		raise ValidationError("Ukuran File Dokumen Maksimal 1 MB")
	else: 
		return True

def jpeg_valid(value):
	file_name = value.name
	if '.jpeg' not in file_name:
		raise ValidationError("Format File Gambar Tidak Sesuai (.jpeg)")
	else: 
		return True

def max_photo_size(value):
	file_size = value.size
	if file_size > 512000:
		raise ValidationError("Ukuran File Gambar Maksimal 500 KB")
	else: 
		return True

def hp_numeric(value):
	val = value
	if not val.isnumeric():
		raise ValidationError("Nomor HP Tidak Valid")
	else: 
		return True

def ktp_numeric(value):
	val = value
	if not val.isnumeric():
		raise ValidationError("Nomor KTP Tidak Valid")
	else: 
		return True

def email_valid(value):
	val = value
	if '@' not in val or '.' not in val or len(val) < 8:
		raise ValidationError("Alamat Email Tidak Valid")
	else: 
		return True