from django.contrib import admin
from django.urls import path
from products.views import CategoryList, ProductsList, ProductClass, DeleteProductClass,AuthorsClass,BooksClass,BooksClassUpdateDelete


urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('products/', ProductsList.as_view()),
    path('products/', ProductClass.as_view()),
    path('deleteProduct/<int:pk>', DeleteProductClass.as_view()),
    path('authors/',AuthorsClass.as_view()),
    path('books/',BooksClass.as_view()),
    path('updateDeleteBooks/<int:pk>',BooksClassUpdateDelete.as_view()),

    # path('addproduct/',ProductCreateClass.as_view())
]
