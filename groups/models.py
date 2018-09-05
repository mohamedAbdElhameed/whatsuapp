from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='groups/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.URLField(max_length=500)
    details = models.TextField(null=True, blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.image is None:
            s = str(self.link)
            ss = s.split('invite')
            if len(ss) == 1:
                ss = s.split('.com/')
                if len(ss) == 1:
                    self.image = s
                else:
                    ss.insert(1, '.com/invite/icon/')
                    s = ss[0] + ss[1] + ss[2]
            else :
                ss.insert(1, 'invite/icon')
                s = ss[0] + ss[1] + ss[2]
            self.image = s
            super(Link, self).save()
        else:
            super(Link, self).save()
    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True