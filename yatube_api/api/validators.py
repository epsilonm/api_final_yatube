from rest_framework import serializers


class FollowingValidator:
    """
    Validator for checking that user can not follow himself.
    """
    def __init__(self, user='user', following='following'):
        self.user = user
        self.following = following

    def __call__(self, attrs):
        if attrs[self.user] == attrs[self.following]:
            raise serializers.ValidationError('You can not follow yourself!')
