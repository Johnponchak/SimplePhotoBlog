from django.db import models

# Create your models here.
class Archive(models.Model):
	name = models.CharField(max_length=200,unique=True)
	thumbnail = models.ImageField(upload_to='static/',blank="True")
	description = models.CharField(max_length=1000,blank="True")
	displayname = models.CharField(max_length=200)

	def __str__(self):
		return self.displayname

class Gallery(models.Model):
	archive = models.ForeignKey(Archive, on_delete=models.CASCADE, default="buildings")
	name = models.CharField(max_length=200)
	displayname = models.CharField(max_length=200)
	thumbnail = models.ImageField(upload_to='static/',blank="True")

	def __str__(self):
		return self.displayname

class GalleryImage(models.Model):
	gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='static/',blank="True")
	caption = models.CharField(max_length=500)

	def __str__(self):
		return self.caption

