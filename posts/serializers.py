from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username',read_only=True) 
    #source='author.username' 이건 이제 앞으로 author라는 외례키 필드에서 username 속성을 가져와서 "author_username"이라는 시리얼라이저 출력 필드로 보여주겠다는 뜻임
    #실제 값은 author.username, 표현이름은 author_username 이다

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_username', 'created_at', 'updated_at']
        #id는 장고가 자동으로 생성해주는 기본 PK필드
        read_only_fields = ['author', 'created_at', 'updated_at']
        #수정불가한 필드를 설정하므로서 보통 시리얼라이저에서 제어(모델과 뷰보다 여기가 안전하고 세밀하게 제어가능하기때문임) 해당 필드로 들어오는 클라이언트의 입력 요청은 무시됨
        