from django.db import models

class Result(models.Model):
    xhr_duration = models.FloatField()
    spinner_delay_a = models.FloatField()
    spinner_delay_b = models.FloatField()
    faster = models.CharField(max_length=1) #'a,b,-'
    broken = models.BooleanField(default=False)

    os_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def csv(self):
        return "%s, %s, %s, %s, %s, %s" % (
                str(self.xhr_duration),
                str(self.spinner_delay_a),
                str(self.spinner_delay_b),
                self.faster,
                1 if self.broken else 0,
                self.created_at.strftime("%Y-%m-%d %H:%M"))
