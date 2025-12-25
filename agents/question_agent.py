class QuestionGeneratorAgent:
    def run(self, product):
        """
        Generates categorized user questions based on product data.
        """
        return {
            "informational": [
                f"What is {product['name']}?"
            ],
            "usage": [
                "How should I use this product?"
            ],
            "safety": [
                "Are there any side effects?"
            ],
            "skin_type": [
                "Is this product suitable for oily or combination skin?"
            ],
            "purchase": [
                "What is the price of this product?"
            ]
        }
