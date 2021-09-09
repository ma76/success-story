from django.shortcuts import render
import itertools
from django.views.generic import ListView
from .text_model import TextModel,TextCategoryModel
from django.http import Http404


# Create your views here.

class TextList(ListView):
    template_name = 'texts/list_view.html'
    paginate_by = 6
    def get_queryset(self):
        # print(PhotoCategory.title)
        return TextModel.objects.get_is_not_gold_texts()


class TextsListByCategory(ListView):
    template_name = 'texts/list_view.html'
    paginate_by = 6

    def get_queryset(self):
        # print(self.kwargs)
        pk = self.kwargs['pk']
        category = TextCategoryModel.objects.filter(id__exact=pk).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return TextModel.objects.get_texts_by_category(pk)


# def my_grouper(n, iterable):
#     args = [iter(iterable)] * n
#     return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))
#
#
# # def product_detail(request, *args, **kwargs):
# #     selected_product_id = kwargs['productId']
# #     new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})
# #
# #     product: Product = Product.objects.get_by_id(selected_product_id)
# #
# #     if product is None or not product.active:
# #         raise Http404('محصول مورد نظر یافت نشد')
# #
# #     product.visit_count += 1
# #
# #     product.save()
# #
# #     related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()
# #
# #     grouped_related_products = my_grouper(3, related_products)
# #
# #     galleries = ProductGallery.objects.filter(product_id=selected_product_id)
# #
# #     grouped_galleries = list(my_grouper(3, galleries))
# #
# #     context = {
# #         'product': product,
# #         'galleries': grouped_galleries,
# #         'related_products': grouped_related_products,
# #         'new_order_form': new_order_form
# #     }
# #
# #     return render(request, 'products/product_detail.html', context)
# #
#
# class SearchProductsView(ListView):
#     template_name = 'photos/list_view.html'
#     paginate_by = 6
#
#     def get_queryset(self):
#         request = self.request
#         print(request.GET)
#         query = request.GET.get('q')
#         if query is not None:
#             return Product.objects.search(query)
#
#         return Product.objects.get_active_products()
#
#
def texts_categories_partial(request):
    categories = TextCategoryModel.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'texts/categories-partial.html', context)
