from django.urls import path

from .views import (
                    TextListAPI,TextCategoryListAPI,
                    GetByCategory,
                    )

urlpatterns = [
    # Api-Urls
    path('texts',TextListAPI.as_view()),
    path('categories',TextCategoryListAPI.as_view()),
    path('texts/<int:pk>',GetByCategory.as_view()),
]
