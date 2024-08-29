# orders/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import render
from lgcon.models import Menu

class OrderDataAPIView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def order_list_view(request):
    orders = Order.objects.all()
    order_details = []

    for order in orders:
        items = []
        # 각 항목은 JSON 형식의 딕셔너리 형태로 가정합니다.
        for item in order.order_list:  # order_list는 JSON 형식이어야 합니다.
            items.append({
                'name': item.get('name'),
                'price': item.get('price'),
                'number': item.get('number'),
            })
        
        order_details.append({
            'id': order.id,
            'items': items,
            'current_url': order.current_url,
            'order_type': order.takeout_option,  # "먹고가기" 또는 "가져가기"
            'total_amount': order.total_price,  # 최종금액
            'created_at': order.created_at,
        })

    return render(request, 'orders/order_list.html', {'orders': order_details})
