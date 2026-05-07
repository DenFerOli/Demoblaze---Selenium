# config/data.py
from config.settings import TEST_USERS

PRODUCT_CATEGORIES = {
    "phones": "Phones",
    "laptops": "Laptops", 
    "monitors": "Monitors"
}

PRODUCTS = {
    "Samsung galaxy s6": {
        "category": "Phones",
        "price": "$360",
        "description": "Samsung Galaxy S6 32GB White"
    },
    "Nokia lumia 1520": {
        "category": "Phones",
        "price": "$820",
        "description": "Nokia Lumia 1520 16GB Black"
    },
    "MacBook Pro": {
        "category": "Laptops",
        "price": "$1100",
        "description": "Apple MacBook Pro 15-inch"
    },
    "Sony vaio i5": {
        "category": "Laptops",
        "price": "$790",
        "description": "Sony Vaio i5 8GB RAM"
    }
}

EXPECTED_MESSAGES = {
    "product_added": "Product added",
    "signup_success": "Sign up successful",
    "login_success": "Welcome",
    "purchase_complete": "Thank you for your purchase!"
}

TEST_CUSTOMER = {
    "name": "João Silva",
    "country": "Brazil",
    "city": "São Paulo",
    "card": "4111111111111111",
    "month": "12",
    "year": "2025"
}