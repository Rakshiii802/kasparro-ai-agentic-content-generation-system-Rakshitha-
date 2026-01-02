from core.base_agent import BaseAgent

class ProductPageAgent(BaseAgent):
    def can_act(self, bus):
        return bus.has("PARSED_PRODUCT") and not bus.has("PRODUCT_PAGE")

    def act(self, bus):
        product = bus.read("PARSED_PRODUCT")

        product_page = {
            "page_type": "product",
            "name": product["name"],
            "category": product.get("category"),
            "price": product.get("price"),
            "features": product.get("features", [])
        }

        bus.publish("PRODUCT_PAGE", product_page)
        print(" ProductPageAgent ran")




