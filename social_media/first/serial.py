from rest_framework import serializers
from first.models import account



class data_serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    age=serializers.IntegerField()
class account_serializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True)

    class Meta:
        model=account
        fields=['email','username','password','password2']
    def save(self):
        acc=account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError({'password':'not matching'})
        acc.set_password(password)
        acc.save()
        return acc