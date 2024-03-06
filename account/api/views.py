from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer, CustomUserRegisterSerializer, CustomUserLoginSerializer
# for token authentication
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
import json



class GetRoutes(APIView):
    def get(self, request, format=None):
        routes = [
            'GET /api/v1/users/',
            'GET /api/v1/users/:id/',

            'GET /api/v1/profiles/',
            'GET /api/v1/profiles/:id/',

            'GET /api-token-auth/',

            'GET /api/v1/event/',
            'GET /api/v1/event/:id/',
            
            'GET /api/v1/donate/',
            'GET /api/v1/donate/:id/',
            'GET /api/v1/crimevideo/<int:pk>',
            'GET /api/v1/crimevideo',
            'GET /api/v1/crimevideocomment/<int:video_id>',
            'GET /api/v1/entertainmentvideo/<int:pk>',
            'GET /api/v1/entertainmentvideo',
            'GET /api/v1/entertainmentvideocomment/<int:video_id>',
            
        ]
        context = {
            'routes': routes
        }
        return Response(context)

class CustomUserListCreateAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        crimesection_admin = request.data.get('crimesection_admin')
        entertainment_admin = request.data.get('entertainment_admin')
        phone = request.data.get('phone')
        try:
            user = CustomUser.objects.create_user(username=username, crimesection_admin=crimesection_admin,
                                                entertainment_admin=entertainment_admin, phone=phone, password=password)
            user.save()
            return Response({'success': 'successfully created'}, status=status.HTTP_201_CREATED)
        except:
            pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login view
class CustomUserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'message': 'Login successful.',
            'user_details': {
                'id': user.id,
                'username': user.username,
                'crimesection_admin': user.crimesection_admin,
                'entertainment_admin': user.entertainment_admin,
                'phone': user.phone,
                'is_active': user.is_active,
                'is_staff': user.is_staff
            }
        }, status=status.HTTP_200_OK)
class CustomUserRetrieveUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserRegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileRetrieveUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Comment