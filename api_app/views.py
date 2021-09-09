from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextModelSerializers,TextCategoryModelSerializers
from text_app.text_model import TextModel,TextCategoryModel
from django.http import Http404

### API-VIEWS ###
class TextListAPI(APIView):

    def get(self,request):
        query = TextModel.objects.filter(is_gold__exact=False)
        serializer = TextModelSerializers(query,many=True)
        # data = [{'image':f"res.com/{d.image}"} for d in serializer.data]
        return Response(serializer.data,status = status.HTTP_200_OK)
        # return Response(data,status = status.HTTP_200_OK)
    def post(self,request):
        serializer = TextModelSerializers(data=request.data)
        query = TextCategoryModel.objects.get(id= request.data['category'])
        print(query)
        if serializer.is_valid():
            serializer.save(category = query)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

# Create TextCategoryListAPI
class TextCategoryListAPI(APIView):

    def get(self,request):
        query = TextCategoryModel.objects.filter(is_gold__exact=False)
        serializer = TextCategoryModelSerializers(query,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    def post(self,request):
        serializer = TextCategoryModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class GetByCategory(APIView):
    # query by category
    def get(self, request,pk):
        # category_name = self.kwargs['category_name']
        # print(category_name)
        category = TextCategoryModel.objects.filter(id__exact=pk)
        query = TextModel.objects.get_texts_by_category(pk)
        serializer = TextModelSerializers(query,many=True)
        if pk is None:
            raise Response(serializer.error,status = status.HTTP_404_NOT_FOUND)
        # data = [{'id':d['id'],'image':f"res.com/{d['image']}"} for d in serializer.data]
        return Response(serializer.data,status = status.HTTP_200_OK)



