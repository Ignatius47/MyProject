from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query)
        )
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
        # return render(request, 'advocates/advocate_list.html', {'advocates': advocates})

    if request.method == 'POST':
        
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data.get('bio', '')
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
        # return render(request, 'advocates/advocate_list.html', {'advocates': advocates})

@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)  
    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data.get('bio', '')
        advocate.save()

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        advocate.delete()
        return Response('user has been deleted')
    

@api_view(['GET'])
def Companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)