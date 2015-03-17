from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from cards.models import Card, Video
from apiclient.discovery import build
from optparse import OptionParser

DEVELOPER_KEY = "AIzaSyCNqDHPcknvtKkae693fAdNmJfoDjZsKxQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class CardView(TemplateView):
    template_name = 'card.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        cards = user.card_set.all()
        selected_card = user.card_set.first()
        return render(request, self.template_name, {'cards':cards, 'user':user, 'selectd_card':selected_card})

    def post(self, request, *args, **kwargs):
        card_title = request.POST.get('card_title')
        card_desc = request.POST.get('card_desc')
        is_public = request.POST.get('is_public')

        user = request.user
        user.card_set.create(name=card_title, is_public=is_public, desc=card_desc)
        selected_card = user.card_set.first()
        return render(request, self.template_name, {'cards':user.card_set.all(), 'selected_card':selected_card})

class VideoView(TemplateView):
    template_name = 'video.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        card_id = kwargs['card_id']
        card = Card.objects.get(id=card_id)
        videos = card.video_set.all()
        selected_card = user.card_set.first()
        return render(request, self.template_name, {'user':user, 'videos':videos, 'card':card, 'selected_card':selected_card})

    def post(self, request, *args, **kwargs):
        user = request.user
        query = request.POST.get('query')
        card = Card.objects.get(id=int(kwargs['card_id']))
        videos = card.video_set.all()

        searched_data = search(query)
        card, created = card.video_set.get_or_create(query=query, title=searched_data['title'], key=searched_data['video_id'], image_url=searched_data['image_url'], image_url_medium=searched_data['image_url_medium'], image_url_high=searched_data['image_url_high'])
        selected_card = user.card_set.first()
        return render(request, self.template_name, {'user':user, 'videos':videos, 'card':card, 'selected_card':selected_card})



def search(search_string):
    parser = OptionParser()
    parser.add_option('--q', dest='q', help='Search term',
                      default = search_string)
    parser.add_option('--max-results', dest='maxResults',
                      help='Max results', default=1)
    (options, args) = parser.parse_args()

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=options.q,
        part='id,snippet',
        maxResults=options.maxResults
    ).execute()

    video_id = None
    title = None
    image_url = None
    image_url_medium = None
    image_url_high = None

    for search_result in search_response.get('items', []):
        if search_result["id"]["kind"] == "youtube#video":
            video_id = search_result["id"]["videoId"]
            title = search_result["snippet"]["title"]
            image_url = search_result['snippet']['thumbnails']['default']['url']
            image_url_medium = search_result['snippet']['thumbnails']['medium']['url']
            image_url_high = search_result['snippet']['thumbnails']['high']['url']

    return dict(video_id=video_id, title=title, image_url=image_url, image_url_medium=image_url_medium, image_url_high=image_url_high)


def profile(requests):
    user = requests.user
    if user.is_authenticated:
        desc = requests.POST.get('desc')
        id = requests.POST.get('id')
        card = Card.objects.get(id=id)
        card.desc = desc
        card.save()
        return redirect('/card/' + id)
    
