from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from app.models import Employee,User
from .serializers import EmployeeSerializer,EmployeeDeSerializer,UserDeSerializer,UserSerializer



class EmployeeAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # 获取路径传参
        user_id = kwargs.get("pk")
        if user_id:
            #查单个
          try:
             emp = Employee.objects.get(pk=user_id)
                #查单个无法直接序列化，使用序列化器
                # .data将序列化器的数据打包成字典
             emp_ser = EmployeeSerializer(emp).data
             return Response({
                 "status": 200,
                 "message": "查询单个用户",
                 "results": emp_ser,
              })
          except:
              return Response({
                  "status": 200,
                  "message": "查询不到数据，失败了",
              })

        else:
            #查所有
            #员工对象不能直接序列化，返回到前段页面
             ems = Employee.objects.all()

              #多个员工的序列化  需要many=ture
             emp_sers = EmployeeSerializer(ems,many=True).data
             return Response({
                "status": 200,
                "message": "查寻所有用户",
                "results": emp_sers,
              })

    def post(self, request, *args, **kwargs):
        '''
        新增一个对象
        '''
        user_data = request.data
        #检验前台数据
        if not isinstance(user_data,dict) or user_data == {}:
            return Response({
                "status":501,
                'msg':'数据有误',
            })
        #使用序列化器对前台的数据进行反序列化
        #在反序列化时需要指定关键字参数
        see = EmployeeDeSerializer(data = user_data)
        if see.is_valid():
            # 调用save()去保存对象  必须重写create()方法
            # create() 方法保存成功后会返回 员工实例
            emp = see.save()
            # 将创建成功的用户实例返回到前端
            return Response({
                "status": 200,
                'msg': '添加成功',
                "results": EmployeeSerializer(emp).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                # 验证失败后错误信息包含在 .errors中
                "results": see.errors
            })



class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # 获取路径传参
        user_id = kwargs.get("pk")
        if user_id:
            #查单个
          try:
             emp = User.objects.get(pk=user_id)
                #查单个无法直接序列化，使用序列化器
                # .data将序列化器的数据打包成字典
             emp_ser = UserSerializer(emp).data
             return Response({
                 "status": 200,
                 "message": "查询单个用户",
                 "results": emp_ser,
              })
          except:
              return Response({
                  "status": 200,
                  "message": "查询不到数据，失败了",
              })

        else:
            #查所有
            #用户对象不能直接序列化，返回到前段页面
             ems = User.objects.all()

              #多个用户的序列化  需要many=ture
             emp_sers = UserSerializer(ems,many=True).data
             return Response({
                "status": 200,
                "message": "查寻所有用户",
                "results": emp_sers,
              })

    def post(self, request, *args, **kwargs):
        '''
        新增一个对象
        '''
        user_data = request.data
        #检验前台数据
        if not isinstance(user_data,dict) or user_data == {}:
            return Response({
                "status":501,
                'msg':'数据有误',
            })
        #使用序列化器对前台的数据进行反序列化
        #在反序列化时需要指定关键字参数
        see = UserDeSerializer(data = user_data)
        if see.is_valid():
            # 调用save()去保存对象  必须重写create()方法
            # create() 方法保存成功后会返回 用户实例
            emp = see.save()
            # 将创建成功的用户实例返回到前端
            return Response({
                "status": 200,
                'msg': '添加成功',
                "results": UserSerializer(emp).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                # 验证失败后错误信息包含在 .errors中
                "results": see.errors
            })




