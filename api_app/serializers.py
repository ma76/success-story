from rest_framework import serializers
from text_app.text_model import TextModel, TextCategoryModel

#
class TextModelSerializers(serializers.ModelSerializer):
    # if you set categories AS StringRelatedField = you have name of Category instead of ID
    # categories = serializers.StringRelatedField()
    class Meta:
        model = TextModel
        fields = ['category','is_gold','text']
        # fields = '__all__'

#
class TextCategoryModelSerializers(serializers.ModelSerializer):
    # photos = PhotoSerializers(read_only=True,many=True)
    # photos = serializers.StringRelatedField(many=True,read_only=True)
    # photos = serializers.SlugRelatedField(slug_field='image',read_only=True,many=True) # UTF-8 Error may be persian url
    class Meta:
        model = TextCategoryModel
        fields = '__all__'
