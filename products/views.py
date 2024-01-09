from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from products.models import Category, Products,Authors,Books
from products.serializers import CategorySerializer, ProductsSerializer, ProductsSerializerCreate, AuthorsSerializer,BooksSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

# Create your views here.


class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


class CategoryList(APIView):

    def get(self, request):
        data = Category.objects.all()
        category = CategorySerializer(data, many=True)
        return Response(category.data)

    def post(self, request):
        data = request.data
        newCategory = CategorySerializer(data=data)
        print(newCategory)
        if newCategory.is_valid():
            newCategory.save()
            return Response(newCategory.data)
        return Response(newCategory.errors)


class ProductsList(APIView):

    def get(self, request):
        data = Products.objects.all()
        newProduct = ProductsSerializer(data, many=True)
        return Response(newProduct.data)

    def post(self, request):
        data = request.data
        print(data)
        newProduct = ProductsSerializer(data=data)
        if (newProduct.is_valid()):
            newProduct.save()
            return Response(newProduct.data)
        return Response(newProduct.errors)


class ProductClass(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_map = {
        'GET': ProductsSerializer,
        'POST': ProductsSerializerCreate,
    }


class DeleteProductClass(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
#class AuthorsClass(generics.ListCreateAPIView):
class AuthorsClass(generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

    def get(self, request, *args, **kwargs):
        authors = self.queryset.all()
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data)

class BooksClass(generics.ListCreateAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer

class BooksClassUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer
