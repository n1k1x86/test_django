from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdvModel
from .serializers import AdvModelSerializer
from django.http import Http404

class AdvModelListCreateAPIView(APIView):
    def get(self, request):
        queryset = AdvModel.objects.all()
        serializer = AdvModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvModelRetrieveUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            return AdvModel.objects.get(pk=pk)
        except AdvModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        your_model = self.get_object(pk)
        serializer = AdvModelSerializer(your_model)
        return Response(serializer.data)

    def put(self, request, pk):
        your_model = self.get_object(pk)
        serializer = AdvModelSerializer(your_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
