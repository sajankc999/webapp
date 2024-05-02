from rest_framework import serializers
from .models import *
user_obj=get_user_model()
class PostSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default = serializers.CurrentUserDefault())
    author_id = serializers.StringRelatedField()
    like_count = serializers.IntegerField(default=0)
    comment_count = serializers.IntegerField(default=0)
    caption = serializers.CharField(default='')
    class Meta:
        model = Post
        fields = '__all__'
        # exclude =['date_created',]

class InteractionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    # comment = serializers.CharField(default='')
    class Meta:
        model = Interaction
        fields ="__all__"

    # def validate_comment(self,value):
    #     if value.isspace():
    #         return serializers.ValidationError('comment cannot be empty string')

