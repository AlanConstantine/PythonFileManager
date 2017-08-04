from django.shortcuts import render
from scratch.models import Crawler
from datetime import datetime
from django import forms
from django.views.decorators import csrf
from django.http import HttpResponse
import random
# Create your views here.
import os
import json
import datetime


def home(request):
    post_list = Crawler.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def show(request, id):
    try:
        post_list = []
        post = Crawler.objects.get(id=str(id))
        if request.method == 'GET':
            file_path = os.path.abspath(
                os.curdir)+'\\'+'scratch'+'\\'+'upload'+'\\'+str(post.crawlerfile)
            with open(file_path, 'r', encoding='utf8') as f:
                contents = f.readlines()
            content = ''.join(contents)
            filename = str(post.crawlerfile)
            return render(request, 'show.html', {'post': post, 'content': json.dumps(content), 'filename': filename})
    except Crawler.DoesNotExist as e:
        raise Http404("Page does not exist")


def delete(request, id):
    try:
        dele = Crawler.objects.get(id=str(id))
        file_path = os.path.abspath(
            os.curdir)+'\\'+'scratch'+'\\'+'upload'+'\\'+str(dele.crawlerfile)
        os.remove(file_path)
        dele.delete()
    except Crawler.DoesNotExist as e:
        raise Http404("Page does not exist")
    post_list = Crawler.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def new(request):
    return render(request, 'new.html')


def edit(request, id):
    try:
        post_list = []
        post = Crawler.objects.get(id=str(id))
        if request.method == 'GET':
            file_path = os.path.abspath(
                os.curdir)+'\\'+'scratch'+'\\'+'upload'+'\\'+str(post.crawlerfile)
            with open(file_path, 'r', encoding='utf8') as f:
                contents = f.readlines()
            content = ''.join(contents)
            filename = str(post.crawlerfile)
            return render(request, 'edit.html', {'post': post, 'content': json.dumps(content), 'filename': filename})
    except Crawler.DoesNotExist as e:
        raise Http404("Page does not exist")


def create(request):
    postinfo = {}
    if request.method == 'POST':
        file_obj = request.FILES.get('crawlerfile', None)
        if file_obj == None:
            return HttpResponse('file not existing in the request')
        file_name = str(file_obj)
        file_path = os.path.abspath(
            os.curdir)+'\\'+'scratch'+'\\'+'upload'+'\\'+file_name
        with open(file_path, 'wb+') as f:
            f.write(file_obj.read())
        postinfo['name'] = request.POST['projectname']
        postinfo['developer'] = request.POST['developer']
        postinfo['description'] = request.POST['description']
        postinfo['crawlerfile'] = str(file_obj)
        Crawler.objects.create(**postinfo)
    post_list = Crawler.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def update(request, id):
    putinfo = {}
    content = ''
    if request.method == 'POST':
        post = Crawler.objects.get(id=str(id))
        putinfo['name'] = request.POST['projectname']
        putinfo['developer'] = request.POST['developer']
        putinfo['description'] = request.POST['description']
        putinfo['crawlerfile'] = request.POST['crawlerfile']
        putinfo['created_at'] = datetime.datetime.now(
        ).strftime('%Y-%m-%d %H:%M:%S.%f')
        file_path = os.path.abspath(
            os.curdir)+'\\'+'scratch'+'\\'+'upload'
        old_name = file_path+'\\'+str(post.crawlerfile)
        new_name = file_path+'\\'+str(putinfo['crawlerfile'])
        os.rename(old_name, new_name)
        content = str(request.POST['content']).replace('\r', '')
        with open(new_name, 'wt', encoding='utf8') as f:
            f.write(content)
        Crawler.objects.filter(id=str(id)).update(**putinfo)
        post = Crawler.objects.get(id=str(id))
        return render(request, 'show.html', {'post': post, 'content': json.dumps(content), 'filename': putinfo['crawlerfile']})
    else:
        return HttpResponse('Page does not exist')
