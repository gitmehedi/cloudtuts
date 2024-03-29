from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.models.restaurant import Restaurant
from restapi.serializers import RestaurantSerializer


class RestaurantView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk is not None:
            try:
                data = Restaurant.objects.get(id=pk)
                serializer = RestaurantSerializer(data)
            except Restaurant.DoesNotExist:
                return Response({"Error": "Data is not available"})
        else:
            data = Restaurant.objects.all()
            serializer = RestaurantSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk=None):
        try:
            data = Restaurant.objects.get(id=pk)
            serializer = RestaurantSerializer(instance=data, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({"Error": "Data is not available"})

    def delete(self, request, pk=None):
        try:
            data = Restaurant.objects.get(id=pk)
            if data:
                data.delete()
            return Response("Delete Successfully")
        except Restaurant.DoesNotExist:
            return Response({"Error": "Data is not available"})
