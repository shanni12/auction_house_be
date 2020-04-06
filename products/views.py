from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerializer
from json import dumps, loads


@api_view(['GET'])
def products_list(request):
    """
    list all the products in the db.
    """
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def product_update(request, pk, format=None):
    """
    update the product in the db
    """
    try:
        product = Products.objects.get(pk=pk)
    except Exception:
        return Response(status.HTTP_404_NOT_FOUND)

    product_data = ProductsSerializer(product).data
    product_bids = loads(product_data.get("bids", {}))
    try:
        if isinstance(request.data, dict):
            if request.data.values():
                bid_amount = list(request.data.values())[0]
                if isinstance(bid_amount, int):
                    product_bids.update(request.data)
                    product.bids = dumps(product_bids)
                    product.save()
                else:
                    Response(status.HTTP_400_BAD_REQUEST)
    except:
        Response(status.HTTP_400_BAD_REQUEST)

    return Response(status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def product_create(request, format=None):
    """
    create a new product
    """

    serializer = ProductsSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
