from django.shortcuts import render
from .models import Menu, Order, Category
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def landing(requset, pk):

    menu_names = Menu.objects.order_by("name")
    category = Category.objects.all()

    return render(
        requset,
        "lgcon/index.html",
        {
            "menu" : menu_names,
            "category" : category
        }
    )

def test(requset):
    
    menu_names = Menu.objects.order_by("name")
    category = Category.objects.all()

    return render(
        requset,
        "lgcon/test.html",
        {
            "menu" : menu_names,
            "category" : category
        }
    )

    # model = Menu
    # context = {"id" : pk}

    # def get_context_data(self, **kwargs):
    #     context = super(landing, self).get_context_data()
    #     context["menu"] = Menu.objects.all()
    #     context["catagory"] = Category.objects.all()
        
    # return render(requset, "lgcon/index.html", context=context)

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        order_data = {
            "customer_name": request.POST.get("customer_name"),
            "product_name": request.POST.get("product_name"),
            "amount": request.POST.get("amount"),
            # 필요한 추가 필드들
        }

        try:
            response = requests.post('http://localhost:8000/orders/api/orders/', data=order_data)
            if response.status_code == 201:
                return JsonResponse({"message": "Order created successfully"}, status=201)
            else:
                return JsonResponse({"message": "Failed to create order"}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"message": str(e)}, status=500)