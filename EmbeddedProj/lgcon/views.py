from django.shortcuts import render
from .models import Menu, Order, Category
import environ

env = environ.Env()
environ.Env.read_env() 

PG = env("PG")

# Create your views here.
def landing(requset, pk):

    menu_names = Menu.objects.order_by("name")
    category = Category.objects.all()

    return render(
        requset,
        "lgcon/index.html",
        {   
            "pk" : pk,
            "PG" : PG,
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

