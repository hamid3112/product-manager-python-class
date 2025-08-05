# 🛒 Product Management System

A simple Python-based product management system designed to handle product details, stock levels, and categorization using object-oriented programming principles.

## 📁 Project Structure

```

my\_project/
│
├── product\_management/
│   ├── **init**.py
│   ├── product\_models.py      # Product and category classes
│   └── products\_utils.py      # Utility functions for product handling
│
├── main.py                    # Example usage and test cases
└── README.md                  # Project documentation

````

## 🚀 Features

- Object-Oriented Design with `Product` and `ProductCategory` classes
- Enum-based categorization of products
- Functions to:
  - Get all products
  - Filter electronic products
  - Identify low-stock items
- Clean and readable code with localization support (e.g., Persian labels)

## 📦 Product Categories

- Electronics
- Books
- Home Appliances
- Clothing

## 🧪 Example Functions

```python
get_all_product()
get_product_electronic(product_list)
low_stock_product(product_list, threshold=5)
````

## ▶️ How to Run

1. Clone the repository or copy the project files.
2. Make sure you are in the project root directory.
3. Run:

```bash
python main.py
```

## 📌 Dependencies

This project uses only standard Python libraries, no external packages required.
اگر خواستی می‌تونم اسم تو یا لینک گیت‌هابت رو هم در انتهای فایل درج کنم. همین‌طور اگر پروژه رو روی GitHub منتشر کردی، خوشحال می‌شم لینک ریپوی نهایی رو هم ببینم تا کمکت کنم برای بهتر دیده شدنش.
```
