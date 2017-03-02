from django.db import models
from django.core import serializers
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder


# Create your models here.
class Pins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title



class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)
 

# data = serializers.serialize("json", Pins.objects.all())