from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Question,Comment,Vote ,Category





class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ["id","name","backgroundImage"]

class ListQuestion(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id",'question',"date","time"]



class Listuser(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ["id","username"]

class ListComment(serializers.ModelSerializer):
   user = Listuser()
   class Meta:
       model = Comment
       fields = ["id","comment","dategenerated","dategenerated2","datenow","time","n_vote","question","user"]


# class Listuser(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id"]

class ListCommentV(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id",'comment']

class ListVote(serializers.ModelSerializer):
    comment = ListCommentV()
    class Meta:
        model = Vote
        fields = ['comment','user']

class ListVote2(serializers.ModelSerializer):

    comment = serializers.SerializerMethodField()

    class Meta:
        model = Vote
        fields = ['user',"comment"]
    def get_comment(self,obj):
        return ListCommentV(obj.comment_set,many=True).data

class ListQuestionComment(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ['id',"question" , "date" ,"time" ,"comment","category_id"]
     

    def get_comment(self,obj):
        return ListComment(obj.comment_set,many=True).data
    

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password' , 'email' ,'first_name','last_name']

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username,email=email,first_name=first_name,last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class UserLoginSerializer(serializers.Serializer):   
    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination! ")

        return data


