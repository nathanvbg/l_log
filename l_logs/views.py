from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'l_logs/index.html')

def topics(request):
    """Page that lists all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'l_logs/topics.html', context)

def topic(request, topic_id):
    """individual page for a topic and shows its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return(render(request, 'l_logs/topic.html', context))

def topicsno(request):
    return(render(request, 'l_logs/topicsno.html', context))