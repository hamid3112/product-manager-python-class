#!/usr/bin/env python
# coding: utf-8

# In[2]:


# product_management/products_utils.py

from product_management.product_models import Product, ProductCategory

# دیتای اولیه محصولات
product_data = [
    {"id": 1, "name": "لب‌تاب ایسوس", "price": 30000000, "category": ProductCategory.ELECTRONICS, "stock": 10},
    {"id": 2, "name": "کتاب بربادرفته", "price": 50000, "category": ProductCategory.BOOKS, "stock": 6},
    {"id": 4, "name": "تلویزیون سامسونگ", "price": 7000000, "category": ProductCategory.HOME_APPLIANCES, "stock": 1},
    {"id": 5, "name": "کلاه لبه‌دار", "price": 250000, "category": ProductCategory.CLOTHING, "stock": 15},
    {"id": 7, "name": "گوشی شیائومی", "price": 6000000, "category": ProductCategory.ELECTRONICS, "stock": 88}
]


def get_all_product():
    return [
        Product(
            product_id=item["id"],
            name=item["name"],
            price=item["price"],
            category=item["category"],
            stock=item["stock"]
        ) for item in product_data
    ]


def get_product_electronic(product_list):
    return [p.name for p in product_list if p.category == ProductCategory.ELECTRONICS]


def low_stock_product(product_list, threshold=5):
    return [
        {
            "id": p.product_id,
            "name": p.name,
            "price": p.price,
            "category": p.category.value,
            "stock": p.stock
        }
        for p in product_list if p.stock < threshold
    ]

