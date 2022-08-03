from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class UniqueFieldValidator:
    """
    Validator for checking that all fields contain unique information.
    """
    missing_message = _('This field is required.')
    requires_context = True

    def __init__(self, fields):
        self.fields = fields

    def enforce_required_fields(self, attrs, serializer):
        """
        The `UniqueFieldValidator` always forces an implied 'required'
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
        fields_values = {attrs[key] for key in attrs if key in self.fields}
        if len(self.fields) != len(fields_values):
            raise serializers.ValidationError('Fields must be unique!')
