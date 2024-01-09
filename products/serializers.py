from rest_framework import serializers
from products.models import Category, Products, Authors, Books


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    categoryId=CategorySerializer()
    class Meta:
        model = Products
        fields = "__all__"


class ProductsSerializerCreate(serializers.ModelSerializer):
    # categoryId=CategorySerializer()
    class Meta:
        model = Products
        fields = "__all__"
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"

class AuthorsSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model=Authors
        fields="__all__"
        

class BooksSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer(many=True)
    class Meta:
        model = Books
        fields = "__all__"

    def create(self, validated_data):
        
        author_ids = validated_data.pop("author", [])
        book_instance = Books.objects.create(**validated_data)
        print(book_instance.author)
        book_instance.author.set(author_ids)
        return book_instance
    
    def update(self, instance, validated_data):
        author_ids = validated_data.pop("author", [])
        existing_ids=list(instance.author.values_list('id',flat=True))
        print(author_ids)
        print(existing_ids)
        combined_ids=author_ids+existing_ids
        instance.bookName=validated_data.get('bookName',instance.bookName)
        instance.publishedYear=validated_data.get('publishedYear',instance.publishedYear)
        instance.save()
        instance.author.set(combined_ids)
        instance.save()
        return instance