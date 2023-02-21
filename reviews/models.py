from django.db import models
from common.models import CommonModel

# caption : 댓글 내용


# FEED
# USER
class Review(CommonModel):

    """Review Model Definition"""

    caption = models.CharField(
        max_length=100,
        default="",
    )
    reviewer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviewer",
    )
