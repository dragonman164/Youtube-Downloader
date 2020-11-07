from django.shortcuts import render,redirect
import pafy
from django.http import FileResponse,HttpResponse


def index(request):
    return render(request,'index.html')

def download(request):
    try:
        url = request.GET.get('url')
        video = pafy.new(url)
        ele = {}
        for elem in video.streams:
            ele[elem.quality]=elem.url
        print(ele)
        params = {'Title':video.title,'Thumbnail_Url':video.thumb,'views':video.viewcount,'resolution':ele,'duration':video.duration,'author':video.author}
        return render(request,'download.html',params)
    except:
        return render(request,'error.html')

def about(request):
    return render(request,'about.html')


def terms(request):
    return render(request,'terms.html')

