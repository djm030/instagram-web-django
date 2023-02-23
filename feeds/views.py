from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FeedSerializer
from .models import Feed
from users.models import User


# Create your views here.
class FeedsView(APIView):
    def get(self, request):
        all_feed = Feed.objects.all()
        serializer = FeedSerializer(all_feed, many=True)
        return Response(serializer.data)


class oneUserFeedsView(APIView):
    def get_objects(self, username):
        user = User.objects.get(username=username)
        return Feed.objects.filter(user=user)

    def get(self, request, username):
        username_feeds = self.get_objects(username)
        serializer = FeedSerializer(username_feeds, many=True)
        return Response(serializer.data)
