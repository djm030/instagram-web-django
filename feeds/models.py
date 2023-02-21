from django.db import models
from common.models import CommonModel


# caption : 게시글 내용
# contenImg : 게시글 이미지
# likesNum : 좋아요 갯수
# reviewsNum : 댓글갯수

# User


class Feed(CommonModel):
    caption = models.TextField(
        default="",
    )
    contenImg = models.URLField(
        blank=True,
    )
    likesNum = models.PositiveIntegerField(
        default=0,
    )
    reviewsNum = models.PositiveIntegerField(
        default=0,
    )
    Author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="author",
    )
