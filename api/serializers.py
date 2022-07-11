from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'body', 'completed')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email','password','created_at')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class LoginView(serializers.ModelSerializer):
    class Meta:

        def login(self, request):
            email = request.data['email']
            password = request.data['password']

            user = CustomUser.objects.filter(email=email).first()

            if user is None:
                # raise AuthenticationFailed('Credentials not found')
                return JsonResponse({"error":"Email Mismatch"}, status=401)
            
            if not user.check_password(password):
                # raise AuthenticationFailed('Incorrect Password')
                return JsonResponse({"error":"Incorrect passoword"}, status=401)
            
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=7200),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret',algorithm='HS256')
            


            response =  Response()

            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data= {
                'jwt' : token
            }

            return response

