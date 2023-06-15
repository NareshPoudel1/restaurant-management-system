# Create your views here.
from django.shortcuts import render
from .models import Product, ProductRecommendation

def recommended_products(request, product_id):
    product = Product.objects.get(id=product_id)
    product_recommendation, _ = ProductRecommendation.objects.get_or_create(product=product)
    if not product_recommendation.recommended_products:
        product_recommendation.fit()
    recommended_products = product_recommendation.get_recommendations()
    context = {'product': product, 'recommended_products': recommended_products}
    return render(request, 'shop/recommended_products.html', context)
