from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import logging
from base.serializer import ProfileSerializer
from ..models import *
from ..serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed

logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showAllProducts(request):
    try:
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.exception("An error occurred in showAllProducts: %s", str(e))
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProduct(request):
    try:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception("An error occurred in addProduct: %s", str(e))
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    try:
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Products.DoesNotExist:
        return Response("Product not found.", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception("An error occurred in updateProduct: %s", str(e))
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProduct(request, pk):
    try:
        product = Products.objects.get(id=pk)
        product.delete()
        return Response('Item deleted successfully!')
    except Products.DoesNotExist:
        return Response("Product not found.", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception("An error occurred in deleteProduct: %s", str(e))
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showProduct(request, pk):
    try:
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Products.DoesNotExist:
        return Response("Product not found.", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception("An error occurred in showProduct: %s", str(e))
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    try:
        user = request.user
        profile = user.profile
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)
    except Exception as e:
        logger.exception("An error occurred in get_profile: %s", str(e))
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def logout_view(request):
    try:
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response({"detail": "Successfully logged out."})
    except Exception as e:
        logger.exception("An error occurred in logout_view: %s", str(e))
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
