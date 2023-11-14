from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User  
from .models import Todo
from .serializers import UserSerializer  
from django.shortcuts import render,redirect
from django.http import JsonResponse
import json

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})

@api_view(['GET'])
def get_data(request):
    data = User.objects.all()  
    serializer = UserSerializer(data, many=True)  # Use your model's serializer
    return Response(serializer.data)



def addNewToDo(request):
    if request.method =="POST":
        try:
            # data=json.loads(request.body)
            todo_name=request.POST.get('name')
            todo_description=request.POST.get('description')
            # print(data)
            newdata=Todo(name=todo_name,description=todo_description)
            newdata.save()
            return redirect('../show/')
        except Exception as e:
            print(e)
            return JsonResponse({"message":"something went wrong"},status=400)
    else:
        return JsonResponse({"message":"Bad request"},status=405)

def showTodoList(request):
    if request.method=="GET":
        todos = Todo.objects.all()
        return render(request, "todolist.html", {'todos': todos})
    else:
        return JsonResponse({"message":"Bad Request"},status=400)


def delTodo(request,todo_id):
    if request.method=="GET":
        try:
            newData=Todo.objects.get(id=todo_id)
            newData.delete()
            return redirect('../../show/')
        except Todo.DoesNotExist:
            return JsonResponse({"message": "ToDo item not found"}, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({"message":"Bad Request"},status=400)    
        
    else:
        return JsonResponse({"message":"Bad Request"},status=400)