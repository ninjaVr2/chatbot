
from django.db.models import Q
from rest_framework import serializers
from chat.models.users.main import UserChatModel


class UserChatWriteSerializer(serializers.Serializer):
    name = serializers.CharField(label='Name', write_only=True,
                                     style={'input_type': 'text'}, trim_whitespace=False
                                     )
    def to_representation(self, instance):
        instance = super(UserChatWriteSerializer,
                     self).to_representation(instance)
        return instance

    def to_internal_value(self, data):
        # print({"to_internal_value-data": data})

        return super().to_internal_value(data)

    def validate(self, attrs):
        return super().validate(attrs)
        
    def validate_empty_values(self, data):
        # print({"validate_empty_values-data": data})
        return super().validate_empty_values(data)
    
    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = UserChatModel
        fields = model.MetaDb.fields
        # read_only_fields = fields