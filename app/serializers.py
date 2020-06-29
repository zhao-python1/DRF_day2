from rest_framework import serializers

# 定义序列化器类 跟模型moles对应的

#首先，给一个序列化器
from app.models import Employee
from app.models import User
from new_DRF import settings


class EmployeeSerializer(serializers.Serializer):
    '''
    需要为model单独配置一个序列化器
    和字段名相匹配--序列化
    '''
    username = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.IntegerField()
    pic = serializers.ImageField()
    phone = serializers.CharField()


    #自定义字段
    salt = serializers.SerializerMethodField()
    #自定义字段的属性名都行，但是提供值得方法名必须是get_字段名
    def get_salt(self,obj):
        return "salt"
    # 自定义性别的返回值
    gender = serializers.SerializerMethodField()
    # self 是当前序列化对象，obj是当前对象
    def get_gender(self,obj):
        # if obj.gender == 0:
        #   return '男'
        # elif obj.gender ==1:
        #   return '女'
        # else:
        #     return '未知'

        # 性别是choices类型  get_字段名_display()直接访问值
        return obj.get_gender_display()

    # 自定义图片的返回值
    pic = serializers.SerializerMethodField()
    #自定义图片的全路径
    def get_pic(self, obj):
        return "%s%s%s" % ('http://127.0.0.1:8000',settings.MEDIA_URL,str(obj.pic))


# 反序列化器
class EmployeeDeSerializer(serializers.Serializer):
    '''
    反序列化:前台提交数据，然后保存入库
    1.前台提供那些字段
    2.对字段进行安全校验
    3.那些字段需要额外效验
    '''
    #添加反序列化效验规则
    username= serializers.CharField(

        max_length=10,
        min_length=4,
        error_messages={
            "max_length":"长度太长了",
            "min_length":"长度太长了",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()
    #重现天写create（）方法
    def create(self, validated_data):
        #方法中完成添加新增
      return Employee.objects.create(**validated_data)



class UserSerializer(serializers.Serializer):
    '''
    需要为model单独配置一个序列化器
    和字段名相匹配--序列化
    '''
    username = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.IntegerField()
    pic = serializers.ImageField()
    phone = serializers.CharField()


    #自定义字段
    salt = serializers.SerializerMethodField()
    #自定义字段的属性名都行，但是提供值得方法名必须是get_字段名
    def get_salt(self,obj):
        return "salt"
    # 自定义性别的返回值
    gender = serializers.SerializerMethodField()
    # self 是当前序列化对象，obj是当前对象
    def get_gender(self,obj):
        # if obj.gender == 0:
        #   return '男'
        # elif obj.gender ==1:
        #   return '女'
        # else:
        #     return '未知'

        # 性别是choices类型  get_字段名_display()直接访问值
        return obj.get_gender_display()

    # 自定义图片的返回值
    pic = serializers.SerializerMethodField()
    #自定义图片的全路径
    def get_pic(self, obj):
        return "%s%s%s" % ('http://127.0.0.1:8000',settings.MEDIA_URL,str(obj.pic))


# 反序列化器
class UserDeSerializer(serializers.Serializer):
    '''
    反序列化:前台提交数据，然后保存入库
    1.前台提供那些字段
    2.对字段进行安全校验
    3.那些字段需要额外效验
    '''
    #添加反序列化效验规则
    username= serializers.CharField(

        max_length=10,
        min_length=4,
        error_messages={
            "max_length":"长度太长了",
            "min_length":"长度太长了",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()
    #重现天写create（）方法
    def create(self, validated_data):
        #方法中完成添加新增
      return User.objects.create(**validated_data)

