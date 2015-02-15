# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout
from users.models import User

class NuncBaseView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, self.template_name, {'user':user})

class LoginView(TemplateView):
    template_name = 'session.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')        
        facebook_id = request.POST.get('id')
        name = request.POST.get('name')        

        user, created = User.objects.get_or_create(email=email, first_name=first_name, last_name=last_name,
                                          facebook_id=facebook_id, username=name)

        user.backend = 'django.contrib.auth.backends.ModelBackend'

        login(request, user)
        return redirect('/')
        
    # def post(self, request, *args, **kwargs):
    #     form = UserValidationForm(request.POST)
    #     if form.is_valid():
    #         user_id = form.cleaned_data['user_id']
    #         password = form.cleaned_data['password']

    #         user = authenticate(user_id=user_id, password=password)
    #         if user is not None:
    #             if user.check_password(password):
    #                 login(request, user)
    #                 return HttpResponseRedirect('/cooperation/')
    #     return render(request, self.template_name, data)


class CardView(TemplateView):
    template_name = 'card.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def get_video(request):
    if 'query' not in request.POST:
        return HttpResponse("bad request")
    else:
        search_string = request.POST['query']
        return HttpResponse(youtube.search(unicode(search_string)))

def get_music_list(request):
    if 'query' not in request.POST:
        return HttpResponse("bad request")
    else:
        list_id = request.POST['query']
        music_list = Playlist.objects.get(id=int(list_id)).music_set.all()
        data = {}
        music_infos = []
        for i in music_list:
            data_set = []
            data_set.append(i.id)
            data_set.append(i.name)
            music_infos.append(data_set)

        data['title'] = Playlist.objects.get(id=int(list_id)).name
        data['music_infos'] = music_infos
        return HttpResponse(json.dumps(data))

def update_music(request):
    if 'query' not in request.POST:
        return HttpResponse("bad request")
    else:
        if 'update_value' not in request.POST:
            return HttpResponse("bad request")
        else:
            if 'status' not in request.POST:
                return HttpResponse("bad request")
            else:
                if request.POST['status'] == 'update':
                    music_id = request.POST['query']
                    music = Music.objects.get(id=music_id)
                    music.name = request.POST['update_value']
                    music.save()
                    return HttpResponse(music.name)
                elif request.POST['status'] == 'add':
                    playlist_id = request.POST['query']
                    playlist = Playlist.objects.get(id=playlist_id)
                    added_music = playlist.music_set.create(name=request.POST['update_value']);
                    added_music.save()
                    data = {}
                    data['id'] = added_music.id
                    data['name'] = added_music.name
                    return HttpResponse(json.dumps(data))
                else:
                    return HttpResponse('bas request')

def delete_music(request):
    if 'query' not in request.POST:
        return HttpResponse("bad request")
    else:
        music = Music.objects.get(id=request.POST['query'])
        music.delete()
        return HttpResponse("success")

def update_playlist(request):
    if 'playlist_id' not in request.POST:
        return HttpResponse("bad request")
    else:
        if 'update_value' not in request.POST:
            return HttpResponse("bad request")
        else:
            playlist_id = request.POST['playlist_id']
            playlist = Playlist.objects.get(id=playlist_id)
            update_value = request.POST['update_value']
            playlist.name = update_value
            playlist.save()
            return HttpResponse(playlist.name)

def add_playlist(request):
    if 'name' not in request.POST:
        return HttpResponse("bad request")
    else:
        playlist_name = request.POST['name']
        playlist = Playlist.objects.create(name=playlist_name)
        playlist.save()
        data = {'id':playlist.id, 'name':playlist.name}
        return HttpResponse(json.dumps(data))

def delete_playlist(request):
    if 'playlist_id' not in request.POST:
        return HttpResponse("bad request")
    else:
        playlist_id = request.POST['playlist_id']
        playlist = Playlist.objects.get(id=playlist_id)
        playlist.delete()
        data = "success"
        return HttpResponse(data)


def search_playlist(request):
    if 'name' not in request.POST:
        return HttpResponse("bad request")
    else:
        name = request.POST['name']
        lists = Playlist.objects.all().filter(name__contains=name)
        data_set = []
        for i in lists:
            data = {}
            data['name'] = i.name
            data['id'] = i.id
            data_set.append(data)
        return HttpResponse(json.dumps(data_set))

def playlist(request):
    response = HttpResponse(content_type='application/json')
    response.status = 403
    result = dict(success=False, message='잘못된 접근')
    
    playlists = Playlist.objects.all()

    datum = json.loads(serializers.serialize('json', playlists))

    result['data'] = datum
    result['message'] = '요청 성공'
    result['success'] = True
    response.status = 200

    response.content = json.dumps(result)
    return response

def playlist_detail(request, list_id):
    response = HttpResponse(content_type='application/json')
    response.status = 403
    result = dict(success=False, message='잘못된 접근')
    
    musics = Playlist.objects.get(id=list_id).music_set.all()

    datum = json.loads(serializers.serialize('json', musics))

    result['data'] = datum
    result['message'] = '요청 성공'
    result['success'] = True
    response.status = 200

    response.content = json.dumps(result)
    return response
        
