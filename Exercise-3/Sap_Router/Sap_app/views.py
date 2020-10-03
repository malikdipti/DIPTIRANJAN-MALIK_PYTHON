from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from Sap_app.serializers import Type_of_Router_serializers,Router_Details_serializers
from Sap_app.models import Type_of_Router,Router_Details



class TypeofRouter(ModelViewSet):
    queryset = Type_of_Router.objects.all()
    serializer_class = Type_of_Router_serializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]



class RouterDetails(ModelViewSet):
    queryset =Router_Details.objects.all()
    serializer_class = Router_Details_serializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAdminUser,]






