from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Comment, Follow, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username'
                                          )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image',
                  'group', 'pub_date')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username',
                                        default=CurrentUserDefault())
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field='username',
                                             )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following')
        )
        ]

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError('You can not follow yourself!')
        return value
