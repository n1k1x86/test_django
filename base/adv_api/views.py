from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import AdvModel
from .serializers import AdvModelSerializer
from django.http import Http404

class AdvModelListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request) -> Response:
        """
        GET method for getting list of adv_model objects
        """
        queryset = AdvModel.objects.all()
        serializer = AdvModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        """
        POST method for adding data into database
        """
        serializer = AdvModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvModelRetrieveUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk) -> AdvModel:
        """
        Method for getting model object by id
        """
        try:
            return AdvModel.objects.get(pk=pk)
        except AdvModel.DoesNotExist:
            raise Http404

    def get(self, request, pk) -> Response:
        """
        GET method for getting adv_model obj by id from database
        """
        model_obj = self.get_object(pk)
        serializer = AdvModelSerializer(model_obj)
        return Response(serializer.data)

    def put(self, request, pk) -> Response:
        """
        PUT method for editting adv_model by id
        """
        model_obj = self.get_object(pk)
        serializer = AdvModelSerializer(model_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
