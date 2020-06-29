from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from rest_framework import settings
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from app.models import User

'''
Django视图的两种：
1 函数视图 定义函数的逻辑视图  
2. 类视图 定义类的视图
'''
@csrf_exempt   #为视图免除csrf认证
# @csrf_protect  全局禁用csrf 为某个视图添加csrf认证
def user(request):
    if request.method == "GET":
        username = request.GET.get("username")
        return HttpResponse('GET_这是第一个')

    elif request.method == "POST":
        username = request.POST.get("username")
        print("POST_这是第一个")
        return HttpResponse('POST_这是第一个')

    elif request.method == "PUT":
        username = request.POST.get("username")
        print("PUT_这是第一个")
        return HttpResponse('PUT_这是第一个')

    elif request.method == "DELETE":
        username = request.POST.get("username")
        print("DELETE_这是第一个")
        return HttpResponse('DELETE_这是第一个')

# 类定义的视图
@method_decorator(csrf_exempt,name = "dispatch")  #类视图免除csrf 认证
# @method_decorator(csrf_protect,name = "dispatch")  #类视图免除csrf 认证
class UserView(View):
    '''
    通过内部请求匹配内部函数
    '''
    def get(self,request,*args,**kwargs):
        user_id = kwargs.get("id")
        if user_id:
            #查到返回到前段页面

          # user_val = User.objects.filter(pk=user_id).values("username","password","gender").first()
          user_val = User.objects.get(pk = user_id)
          if user_val :
              return JsonResponse({
                  "status":200,
                  "message":"查询单个用户",
                  "results":user_val,
              })

        else:
            #如果没查到 查询所有
           user_list = User.objects.all().values("username","password","gender")
           if user_list:
               return JsonResponse({
                   "status": 200,
                   "message": "查询单个用户成功",
                   "results": list(user_list),
               })
        return JsonResponse({
            "status": 500,
            "message": "查询单个用户失败",
        })

    def post(self, request, *args, **kwargs):
        """
        新增单个用户
        """
        # print(request.POST)
        # return HttpResponse("POST")
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        print(username,password,gender)
        # return HttpResponse("POST")
        try:
            user_obj = User.objects.create(username=username, password=password,gender=gender)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username":username, "gender":gender,"password":password}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })

    def put(self,request,*args,**kwargs):
        print("PUT_这是第一个")
        return HttpResponse('PUT_这是第一个')

    def delete(self,request,*args,**kwargs):
        print("DELETE_这是第一个")
        return HttpResponse('DELETE_这是第一个')

# drf的视图
class UserAPIView(APIView):

    #局部优先
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        # request：<rest_framework.request.Request>
        # get(self, request, *args, **kwargs):
        print(request._request.GET)
        print(request.GET)
        print(request.query_params)

        # 获取路径传参
        user_id = kwargs.get("pk")
        return Response("aaa")
#
    def post(self, request, *args, **kwargs):
        print(request._request.POST)  # Django 原生的request对象
        print(request.POST)  # DRF 封装后的request对象

        print(request.data)
        return Response("POST GET SUCCESS")

# 局部使用解析器
class StudentAPIView(APIView):

    # 局部使用解析器
    # parser_classes = [MultiPartParser]
    parser_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        print("POST方法")

        # print(request.POST)
        print(request.data)

        return Response("POST方法访问成功")