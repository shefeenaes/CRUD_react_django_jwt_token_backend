from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializer import ProfileSerializer
from ..models import *
from rest_framework.decorators import api_view
from ..serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showAllProducts(request):
    print(request)
    products = Products.objects.all()
    serilizer = ProductSerializer(products, many=True)
    
    return Response(serilizer.data)


@api_view(['POST'])

@permission_classes([IsAuthenticated])
def addProduct(request):
    serilizer = ProductSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)


@api_view(['PUT'])

@permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    product = Products.objects.get(id=pk)
    serilizer = ProductSerializer(instance=product, data=request.data)

    if serilizer.is_valid():
        serilizer.save()

    return Response(serilizer.data)


@api_view(['DELETE'])

@permission_classes([IsAuthenticated])
def deleteProduct(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')


@api_view(['GET'])

@permission_classes([IsAuthenticated])
def showProduct(request, pk):

    student = Products.objects.get(id=pk)
    serilizer = ProductSerializer(student, many=False)
    return Response(serilizer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        
         

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def logout_view(request):
    print("here")
    Token.objects.filter(user=request.user).delete()  # Delete the token associated with the user
    logout(request)  # Logout the user
    return Response({"detail": "Successfully logged out."})


    