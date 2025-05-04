from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Teacher, Student
from .serializer import TeacherSerializer, StudentSerializer

@api_view(['GET'])
def get_teacher(request):
    category = Teacher.objects.all()
    serializedData = TeacherSerializer(category, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_teacher(request):
    data = request.data
    serializer = TeacherSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def teacher_detail(request, pk):
    try:
        category = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({"error":"Category now found."}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        category.delete()
        return Response({"message":"Category deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def get_student(request):
    category = Student.objects.all()
    serializedData = StudentSerializer(category, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        category = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error":"Category now found."}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        category.delete()
        return Response({"message":"Category deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT)