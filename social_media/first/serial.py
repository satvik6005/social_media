from rest_framework import serializers

class data_serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    age=serializers.IntegerField()