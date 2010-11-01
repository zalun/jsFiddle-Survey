from django.db import models

class Result(models.Model):
    xhr_duration = models.FloatField()
    spinner_delay_a = models.FloatField()
    spinner_delay_b = models.FloatField()
    faster = models.CharField(max_length=1) #'a,b,-'
    broken = models.BooleanField(default=False)

    os_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

