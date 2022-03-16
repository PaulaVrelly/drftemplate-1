from os import stat
from webbrowser import get
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from crud.models import Person,Rol,User

from crud.serializers import PersonSerializer

class RetrievePersonsAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        person_list = Person.objects.all()
        serializer = PersonSerializer(person_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreatePersonAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDeletePersonAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, person_id):
        person_obj = get_object_or_404(Person, pk=person_id)
        serializer = PersonSerializer(person_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, person_id):
        person_obj = get_object_or_404(Person, pk=person_id)
        serializer = PersonSerializer(instance=person_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, person_id):
        person_obj = get_object_or_404(Person, pk=person_id)
        person_obj.status = False
        person_obj.save()
        return Response({'message':'Elininado'}, status=status.HTTP_204_NO_CONTENT)
    
class RetrieveRols(APIView):
    permission_clases = (AllowAny,)
    
    def get(self, request):
        roles_list = Rol.objects.all().values()
        return Response(roles_list, status=status.HTTP_200_OK)
    
class CreateRols(APIView):
    permission_clases = (AllowAny,)
    
    def post(self, request):
        roles_obj = Rol.objects.create(
        name = request.data.get('name',''),
        applicant = request.data.get('applicant',''),
        employer = request.data.get('employer',''))                             
        return Response({'mensage':'Creado'}, status=status.HTTP_201_CREATED)
        
    
class RetrieveUsers(APIView):
    permission_clases = (AllowAny,)
    
    def get(self, request):
        user_list = User.objects.all().values()
        return Response(user_list)
    
class CreateUsers(APIView):
    permission_clases = (AllowAny,)
    
    def post(self, request):
        user_obj = User.objects.create(
        email = request.data.get('email',''),
        password = request.data.get('password',''),
        rol_id = request.data.get('rol',''))
        return Response({'mensage':'Creado'}, status=status.HTTP_201_CREATED)
    
