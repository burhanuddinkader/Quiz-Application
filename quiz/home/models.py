import uuid
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name=models.CharField(max_length=100)

class Question(BaseModel):
    category=models.ForeignKey(Category, related_name='category',on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)

class Answere(BaseModel):
    question_answere=models.ForeignKey(Question, related_name='question_answere',on_delete=models.CASCADE)
    answere=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)
