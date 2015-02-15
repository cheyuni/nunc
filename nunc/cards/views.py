from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

class CardView(TemplateView):
    template_name = 'card.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        cards = user.card_set.all()
        return render(request, self.template_name, {'cards':cards, 'user':user})
    
    def post(self, request, *args, **kwargs):
        card_title = request.POST.get('card_title')
        card_desc = request.POST.get('card_desc')
        is_public = request.POST.get('is_public')

        user = request.user
        user.card_set.create(name=card_title, is_public=is_public, desc=card_desc)
        
        return render(request, self.template_name, {'cards':user.card_set.all()})
    
class VidoeView(TemplateView):
    template_name = 'video.html'

    def get(self, request, *args, **kwargs):
        # user = request.user
        # videos = user.card_set.all()
        return render(request, self.template_name)
