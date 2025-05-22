from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher, Student, Assignment
from .serializer import TeacherSerializer, StudentSerializer, AssignmentSerializer

# ------------------- TEACHER -------------------

@api_view(['GET'])
def get_teacher(request):
    teachers = Teacher.objects.all()
    serialized_data = TeacherSerializer(teachers, many=True).data
    return Response(serialized_data)

@api_view(['POST'])
def create_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        teacher.delete()
        return Response({"message": "Teacher deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

# ------------------- STUDENT -------------------

@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    serialized_data = StudentSerializer(students, many=True).data
    return Response(serialized_data)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response({"message": "Student deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


# ------------------- Assignment -------------------

@api_view(['GET'])
def get_assignments(request):
    assignments = Assignment.objects.all()
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_assignment(request):
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def assignment_detail(request, pk):
    try:
        assignment = Assignment.objects.get(pk=pk)
    except Assignment.DoesNotExist:
        return Response({"error": "Assignment not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        assignment.delete()
        return Response({"message": "Assignment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
