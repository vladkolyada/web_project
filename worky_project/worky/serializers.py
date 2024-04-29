import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import ClientRestFramework
from rest_framework import serializers


# class ClientModel:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


class ClientSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ClientRestFramework
        fields = "__all__"

# class ClientSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=60)
#     email = serializers.EmailField(max_length=100)
#
#     def create(self, validated_data):
#         return Client.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.email = validated_data.get("email", instance.email)
#         instance.save()
#         return instance

# def encode():
#     model = ClientModel("Brad Pit", "bpit228@gmail.com")
#     model_sr = ClientSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"Brad Pit", "email":"Email: bpit228@gmail.com"}')
#     data = JSONParser().parse(stream)
#     serializer = ClientSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

