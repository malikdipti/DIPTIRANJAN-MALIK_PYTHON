from rest_framework import serializers
from Sap_app.models import Type_of_Router,Router_Details

class Type_of_Router_serializers(serializers.ModelSerializer):
    class Meta:
        model=Type_of_Router
        fields="__all__"

class Router_Details_serializers(serializers.ModelSerializer):
    class Meta:
        model=Router_Details
        fields = "__all__"
