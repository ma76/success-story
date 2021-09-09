from django.db import models
from text_app.category_model import TextCategoryModel
# Create TextManager
class TextManager(models.Manager):
    def get_is_not_gold_texts(self):
        return self.get_queryset().filter(is_gold__exact=False)
    def get_texts_by_category(self,pk):
        return self.get_queryset().filter(category__id__exact=pk,is_gold__exact=False).filter()

# Create Text-Model
class TextModel(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    is_gold = models.BooleanField(default=False)
    category = models.ForeignKey(TextCategoryModel,on_delete=models.CASCADE,related_name='texts')
    objects = TextManager()

    class Meta:
        verbose_name = 'متن'
        verbose_name_plural = 'متن ها'