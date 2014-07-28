from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    ts = models.IntegerField()
    txt = models.TextField()
    sender = models.TextField()

    class Meta:
        ordering = ('id',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.ManySlugRelatedField(
        slug_field='codename',
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')