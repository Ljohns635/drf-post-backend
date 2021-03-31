from rest_framework.serializers import ModelSerializer
from ghostpost.models import GhostPost

class GhostPostSerializer(ModelSerializer):

    class Meta:
        model = GhostPost
        fields = (
            "id",
            "post_type",
            "post",
            "upvote",
            "downvote",
            "created_at",
            # "total_votes"
        )