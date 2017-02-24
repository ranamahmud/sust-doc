from django.db import models
from django.utils import timezone


class LibraryFine(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='library_fines')
    date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1,choices = G_CHOICES,default=1)
    book_count = models.IntegerField(default=1)
    amount_fined = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title