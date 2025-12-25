def generate_intro_block(product):
    return f"{product['name']} is designed to help with {', '.join(product['benefits'])}."


def extract_usage_block(product):
    return product["usage"]


def extract_safety_block(product):
    return product["side_effects"]


def extract_skin_type_block(product):
    return f"Suitable for {', '.join(product['skin_type'])} skin types."


def extract_price_block(product):
    return product["price"]
def extract_name_block(product):
    return product["name"]


def extract_concentration_block(product):
    return product["concentration"]


def extract_ingredients_block(product):
    return product["ingredients"]


def extract_benefits_block(product):
    return product["benefits"]
def extract_product_summary_block(product):
    return {
        "name": product["name"],
        "ingredients": product["ingredients"],
        "benefits": product["benefits"],
        "price": product["price"]
    }


def generate_fictional_product_block():
    return {
        "name": "RadiantGlow Serum",
        "ingredients": ["Vitamin C"],
        "benefits": ["Brightening"],
        "price": "₹899"
    }


