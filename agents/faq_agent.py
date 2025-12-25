from logicblocks.content_blocks import (
    generate_intro_block,
    extract_usage_block,
    extract_safety_block,
    extract_skin_type_block,
    extract_price_block
)


class FAQAgent:
    def run(self, questions, product):
        """
        Generates FAQ page using reusable logic blocks and templates.
        """

        faq_items = []

        faq_items.append({
            "question": questions["informational"][0],
            "answer": generate_intro_block(product)
        })

        faq_items.append({
            "question": questions["usage"][0],
            "answer": extract_usage_block(product)
        })

        faq_items.append({
            "question": questions["safety"][0],
            "answer": extract_safety_block(product)
        })

        faq_items.append({
            "question": questions["skin_type"][0],
            "answer": extract_skin_type_block(product)
        })

        faq_items.append({
            "question": questions["purchase"][0],
            "answer": extract_price_block(product)
        })

        return {
            "page_type": "faq",
            "items": faq_items
        }

