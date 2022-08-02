from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class FollowingValidator:
    """
    Validator for checking that user can not follow himself.
    """
    message = _('The field {field_name} must be unique.')
    missing_message = _('This field is required.')
    requires_context = True

    def __init__(self, fields, message=None):
        self.fields = fields
        self.message = message or self.message

    def enforce_required_fields(self, attrs, serializer):
        """
        The `FollowingValidator` always forces an implied 'required'
        state on the fields it applies to.
        """
        if serializer.instance is not None:
            return

        missing_items = {
            field_name: self.missing_message
            for field_name in self.fields
            if serializer.fields[field_name].source not in attrs
        }
        if missing_items:
            raise serializers.ValidationError(missing_items, code='required')

    def __call__(self, attrs, serializer):
        self.enforce_required_fields(attrs, serializer)
        for field, value in attrs.items():
            if list(attrs.values()).count(value) > 1:
                message = self.message.format(field_name=field)
                raise serializers.ValidationError(message)
