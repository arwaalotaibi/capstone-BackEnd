from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveAPIView,CreateAPIView

from .serializers import ListVote2,ListVote,ListQuestion , ListComment, ListQuestionComment, UserCreateSerializer,UserLoginSerializer
from .models import Question,Comment,Vote 
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class numberoflikes(APIView):

    def post(self, request):
         #filter user and his show comment
        y = request.data
        n = y['id']
        x = Comment.objects.get(id=n)
        data = Vote.objects.filter(comment=x).count()
        return Response(data, status=HTTP_200_OK)

class userlikes(APIView):

     # def get(self, request):
     #    # data = Vote.objects.filter(user=request.user).count()
     #    # return Response(data, status=HTTP_200_OK)

     #    data = Vote.objects.filter(user=request.user).values()
     #    serializer = ListVote(data)
     #    return Response(serializer.data, status=HTTP_200_OK)
    
    serializer_class = ListVote
    def get_queryset(self):
        user = self.request.user
        return Vote.objects.filter(user=user)       
        #return Vote.objects.filter(user=request.user) 
    # def get(self, request):
    #     # data = Question.objects.all()[:1].get()  ;)
    #     # data = Question.objects.filter(id=2)  :(
    #     # data = Question.objects.first()     ;)
    #     # data = Question.objects.filter(user=request.user).all()  :()
    #     # data = Question.objects.filter(user=request.user).first() ;)
    #     # serializer = ListQuestion(data)
    #     data = Vote.objects.filter(user=request.user).first()   # ;)))
    #     serializer = ListVote(data)
    #     return Response(serializer.data, status=HTTP_200_OK)

class LastQuestionCommentApiView(APIView):

    def get(self, request):
        data = Question.objects.last()

        serializer = ListQuestionComment(data)

        return Response(serializer.data, status=HTTP_200_OK)


     
class Postcomment(APIView):

    def post(self,request):
       
        y = request.data
       
        commenttext = y["comment"]
      
        queryset = Question.objects.last()
        Comment.objects.create(question=queryset,comment=commenttext,user=request.user)

        return Response({"msg":"success"})

class like(APIView):

    def post(self,request):
       
        y = request.data 

        commentId = y['id']
        queryset = Comment.objects.get(id=commentId)
        like ,create = Vote.objects.get_or_create(comment=queryset,user=request.user)
        if not create:
            like.delete()

        return Response({"msg":"success"})


class Deletecomment(DestroyAPIView):
   queryset = Comment.objects.all()
   lookup_field = "id"
   lookup_url_kwarg = 'comment_id'
   permission_classes = [IsAuthenticated]

class ListlikesApiView(ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = ListVote
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]

class ListQuestionCommentApiView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = ListQuestionComment
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

