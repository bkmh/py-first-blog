from django.db import models
from django.conf import settings
from django.utils import timezone
# from 또는 import 로 시작하는 부분은 다른 파일에 있는 것을 추가


# 모델 = 객체(Object)
# Class 객체 정의
class Post(models.Model):

    # ForeignKey
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # models.CharField : 글자수가 제한된 텍스트를 정의할 때 사용
    title = models.CharField(max_length=200)

    # models.TextField : 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



