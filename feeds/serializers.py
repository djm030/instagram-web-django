from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import UserSerializer
from reviews.serializers import ReviewSerializer


class FeedSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Feed
        fields = "__all__"
