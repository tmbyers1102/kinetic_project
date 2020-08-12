from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Session(models.Model):
    uid = models.CharField(max_length=50)
    cid = models.CharField(max_length=50)  # switched from eid
    qid = models.CharField(max_length=50)
    aid = models.CharField(max_length=50)
    session_date = models.DateTimeField(auto_now_add=True)

    def qid_plus_aid(self):
        return '{}_{}'.format(self.qid, self.aid)

    def __str__(self):
        return self.uid

    def get_absolute_url(self):
        return reverse('session-detail', kwargs={'pk': self.pk})
