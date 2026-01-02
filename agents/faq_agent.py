from core.base_agent import BaseAgent

class FAQAgent(BaseAgent):
    def can_act(self, bus):
        return (
            bus.has("PARSED_PRODUCT")
            and bus.has("QUESTIONS")
            and not bus.has("FAQ_PAGE")
        )

    def act(self, bus):
        product = bus.read("PARSED_PRODUCT")
        questions = bus.read("QUESTIONS")

        faq_items = []
        for q in questions:
            faq_items.append({
                "question": q,
                "answer": f"{product['name']} details are based on provided product data."
            })

        faq_page = {
            "page_type": "faq",
            "items": faq_items
        }

        bus.publish("FAQ_PAGE", faq_page)
        print("FAQAgent ran")



