from django.db import models

# Create your models here.
JOB_TYPE=(("FT","Full Time"),("PT","Part Time"))
class Job(models.Model):
    title=models.CharField(max_length=120)
    #locattion
    job_type=models.CharField(max_length=2,choices=JOB_TYPE,default="FT")
    description=models.TextField(max_length=1500,default="write job description")
    published_at=models.DateTimeField(auto_now=True)
    vacances=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    #category
    experience=models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title