from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    is_upcoming = models.BooleanField(default=True)  # Flag to indicate if the event is upcoming or past

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='event_photos/')

    def __str__(self):
        return f'Photo for {self.event.title}'

class EventVideo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField()

    def __str__(self):
        return f'Video for {self.event.title}'
