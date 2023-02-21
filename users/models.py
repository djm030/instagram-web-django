from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# username : 유저이름 => 기존 어드민에 이미 포함
# profileIntroduce :소개글
# profileImg : 프로필 이미지
# followerNum : 유저 팔로워수
class User(AbstractUser):
    """User Model definition"""

    profileImg = models.URLField(
        blank=True,
    )
    profileIntroduce = models.CharField(
        max_length=150,
        default="",
    )
    followerNum = models.PositiveBigIntegerField(
        default=0,
    )
