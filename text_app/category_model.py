from django.db import models

# Create TextCategory-Model
class TextCategoryModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    is_gold = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'