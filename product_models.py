#!/usr/bin/env python
# coding: utf-8

# In[3]:


# product_management/product_models.py

from enum import Enum


class ProductCategory(Enum):
    ELECTRONICS = "لوازم الکترونیک"
    BOOKS = "کتاب‌ها"
    HOME_APPLIANCES = "لوازم خانگی"
    CLOTHING = "لباس"


class Product:
    def __init__(self, product_id, name, price, category: ProductCategory, stock=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def display_info(self):
        print(f"نام محصول: {self.name}")
        print(f"موجودی: {self.stock}")
        print(f"قیمت: {self.price}")
        print(f"کد محصول: {self.product_id}")
        print(f"دسته‌بندی: {self.category.value}")
        print("-------------------------------------")

    def update_stock(self, num):
        if not isinstance(num, int):
            raise TypeError("ورودی باید عدد صحیح باشد.")
        if self.stock + num < 0:
            self.stock = 0
        else:
            self.stock += num

    def is_available(self, quantity):
        return self.stock >= quantity

