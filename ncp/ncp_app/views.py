from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        # Filter events based on whether they are upcoming or past
        upcoming_events = Event.objects.filter(is_upcoming=True).order_by('date')
        past_events = Event.objects.filter(is_upcoming=False).order_by('-date')
        
        return {
            'upcoming_events': upcoming_events,
            'past_events': past_events,
        }

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

def event_detail(request, pk):
    event = all(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})
