# orders/models.py
from django.db import models

class Order(models.Model):
    order_list = models.JSONField()  # 주문 항목을 저장
    current_url = models.URLField()  # 현재 URL
    total_price = models.IntegerField()  # 최종 금액 추가
    takeout_option = models.CharField(max_length=10)  # 먹고가기 or 가져가기 옵션 추가
    created_at = models.DateTimeField(auto_now_add=True)  # 주문 생성 시간

    def __str__(self):
        return f"Order {self.id} at {self.created_at}"