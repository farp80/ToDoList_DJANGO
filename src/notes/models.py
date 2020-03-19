from django.db import models
from django.urls import reverse

# Create your models here.


class Notes(models.Model):
    LABEL_CHOICES = (
        ('P', 'primary'),
        ('SE', 'secondary'),
        ('W', 'warning'),
        ('S', 'success'),
        ('I', 'info'),
        ('D', 'dark'),
        ('L', 'light'),
        ('DA', 'danger'))

    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_finished_item_url(self):
        return (reverse("finished_item", kwargs={'id': self.id}))

    def get_recover_item_url(self):
        return (reverse("recover_item", kwargs={'id': self.id}))

    def get_delete_item_url(self):
        return (reverse("delete_item", kwargs={'id': self.id}))
