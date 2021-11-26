from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify

# Create your models here.
JOB_TYPE=(("FT","Full Time"),("PT","Part Time"))

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

def upload(instance , filename):
    name,ext= filename.split(".")
    import time
    milliseconds = str(int(round(time.time() * 1000)))
    return f"jobs/{instance.id}/{milliseconds+'.'+ ext}"
def ApplyUpload(instance , filename):
    name,ext= filename.split(".")
    import time
    milliseconds = str(int(round(time.time() * 1000)))
    return f"apply/{instance.id}/{milliseconds+'.'+ ext}"

class Job(models.Model):
    title=models.CharField(max_length=120)
    #locattion
    job_type=models.CharField(max_length=2,choices=JOB_TYPE,default="FT")
    description=models.TextField(max_length=1500,default="write job description")
    published_at=models.DateTimeField(auto_now=True)
    vacances=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    image=models.ImageField(upload_to=upload,default=1)
    category=models.ForeignKey('Category',on_delete= CASCADE,default=1)
    experience=models.IntegerField(default=1)
    slug = models.SlugField(max_length=120 ,blank=True,null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        self.slug=slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

class Apply(models.Model):
    job=models.ForeignKey('Job',related_name="Apply_Job",on_delete=CASCADE,default=1)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=120)
    website=models.URLField()
    cv=models.FileField(upload_to=ApplyUpload)
    cover_latter=models.TextField(max_length=500)
    create_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    