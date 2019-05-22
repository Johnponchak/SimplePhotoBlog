from django.shortcuts import render
from django.views import generic
from .models import Archive, Gallery, GalleryImage


# Create your views here.

def archives(response):
	arc=Archive.objects.all()
	if response.user_agent.is_mobile == True:
		return render(response, "photogallery/archivelist_mobile.html", {"archive":arc})
	else:
		return render(response, "photogallery/archivelist_pc.html", {"archive":arc})

def gallerys(response, arc):
	gal = Gallery.objects.filter(archive__name=arc)
	arc = Archive.objects.get(name=arc)
	if response.user_agent.is_mobile == True:
		return render(response, "photogallery/gallerylist_mobile.html", {"gallery":gal, "archive":arc})
	else:
		return render(response, "photogallery/gallerylist_pc.html", {"gallery":gal, "archive":arc})

def galleryimages(response, gal):
	img = GalleryImage.objects.filter(gallery__name=gal)
	gal = Gallery.objects.get(name=gal)
	if response.user_agent.is_mobile == True:
		return render(response, "photogallery/gallery_mobile.html", {"gallery":gal, "archive":arc})
	else:
		return render(response, "photogallery/gallery_pc.html", {"gallery":gal, "galleryimage":img})