from django.urls import path

from .views import (TextList,TextsListByCategory,
texts_categories_partial

                    )

urlpatterns = [
    path('texts', TextList.as_view()),
    # path('photos/search', SearchProductsView.as_view()),
    path('texts/<int:pk>', TextsListByCategory.as_view()),
    # # path('phtos/<productId>/<name>', product_detail),
    path('texts_categories_partial', texts_categories_partial, name='texts_categories_partial'),
]
