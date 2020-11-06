from django.shortcuts import render,redirect
from pytube import YouTube
from django.http import FileResponse,HttpResponse


def index(request):
    return render(request,'index.html')

def download(request):
    try:
        url = request.GET.get('url')
        yt = YouTube(url)
        ele = set()
        for elem in yt.streams:
            if elem.resolution != None:
                ele.add(elem.resolution)     
        params = {'Title':yt.title,'Thumbnail_Url':yt.thumbnail_url,'views':yt.views,'resolution':ele,'url':url}
        return render(request,'download.html',params)
    except:
        return render(request,'error.html')

def start_download(request):
    try:
        url = request.GET.get('url')
        quality = request.GET.get('quality')
        yt = YouTube(url)
        print(quality)
        ys = yt.streams.get_by_resolution(quality)
        response = redirect(ys.url)
        return response
    except :
        return render(request,'error.html')

def about(request):
    return render(request,'about.html')


def terms(request):
    return render(request,'terms.html')

