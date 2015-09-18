from django.db import models

class Gamers(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.FirstName, self.LastName)

