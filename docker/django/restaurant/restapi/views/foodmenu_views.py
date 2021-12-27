from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.models import FoodMenu
from restapi.serializers import FoodMenuSerializer


class FoodMenuView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk is not None:
            try:
                data = FoodMenu.objects.get(id=pk)
                serializer = FoodMenuSerializer(data)
            except FoodMenu.DoesNotExist:
                return Response({"Error": "Data is not available"})
        else:
            data = FoodMenu.objects.all()
            serializer = FoodMenuSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = FoodMenuSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk=None):
        try:
            data = FoodMenu.objects.get(id=pk)
            serializer = FoodMenuSerializer(instance=data, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

        except FoodMenu.DoesNotExist:
            return Response({"Error": "Data is not available"})

    def delete(self, request, pk=None):
        try:
            data = FoodMenu.objects.get(id=pk)
            if data:
                data.delete()
            return Response("Delete Successfully")
        except FoodMenu.DoesNotExist:
            return Response({"Error": "Data is not available"})
