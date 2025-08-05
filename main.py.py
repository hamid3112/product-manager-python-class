#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# main.py

from product_management.product_models import Product, ProductCategory
from product_management.products_utils import get_all_product, get_product_electronic, low_stock_product

if __name__ == "__main__":
    product_list = get_all_product()

    print("📦 محصولات الکترونیک:")
    print(get_product_electronic(product_list))

    print("\n⚠️ محصولات رو به اتمام:")
    print(low_stock_product(product_list))

    print("\n🆕 نمونه محصول جدید:")
    sample = Product(8, "پیراهن", 500000, ProductCategory.CLOTHING, 8)
    sample.display_info()

    print("\n📦 به‌روزرسانی موجودی:")
    sample.update_stock(20)
    sample.display_info()

