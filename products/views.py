import json
from django.views import View
from django.http import JsonResponse
from .models import Category, Product, Nutrition, Menu

class ProductsView(View):
    def get(self, request):
        results = []
        products = Product.objects.all()
        for product in products:
            results.append({
                "id" : product.id,
                "korean_name" : product.korean_name,
                "english_name" : product.english_name,
                "description" : product.description,
                "category_id" : product.category.id
            })
        return JsonResponse({"products" : results}, status=200)
        
    def post(self, request):
        """
        목적   : Client에서 보내주는 상품 정보(카테고리, korean_name, english_name, description
                 , protein, size, sodium)를 데이터베이스에 products, category, nutrtion 테이블에 저장한다. 
        """
        """
        Input  : 
            {
                "menu" : "음료",
                "category": "콜드브루",
                "description": "테스트",
                "english_name": "Nitro...",
                "korean_name": "나이트로 바닐라 크 림",
                "protein": 10.3,
                "size": 60.5,
                "sodium": 10.5
            }
        """
        input_data = json.loads(request.body)

        """
        Logic  :
            0. Menu 모델을 사용해서, menu 테이블에 row("음료")를 추가한다.
            1. Category 모델을 사용해서, category 테이블에 row("콜드브루")를 추가한다.
            2. Nutrition 모델을 사용해서, nutrtion 테이블에 row("pro, size, sodium")를 추가한다.
            3. Product 모델을 사용해서, product 테이블에 row("desc, en, ko, ca")를 추가한다.
        """
        # 1.
        menu = Menu.objects.create(name=input_data["menu"])
        # 2.
        category = Category.objects.create(name=input_data["category"], menu_id = menu.id)
        # 3.
        nutrition = Nutrition.objects.create(
            protein_g = input_data["protein"],
            sodium_mg = input_data["sodium"],
            size_ml   = input_data["size"]
        )
        # 4.
        product = Product(
            korean_name = input_data["korean_name"],
            english_name = input_data["english_name"],
            description = input_data["description"],
            category_id = category.id,
            nutrition_id = nutrition.id
        )

        """
        Output : 
            {
                "message" : "SCCUESS"
            }, status_code = 201
        """
        product.save()

        return JsonResponse({"message" : "SUCCESS"}, status=201)