from core.base_agent import BaseAgent

class ComparisonAgent(BaseAgent):
    def can_act(self, bus):
        return bus.has("PARSED_PRODUCT") and not bus.has("COMPARISON_PAGE")

    def act(self, bus):
        product = bus.read("PARSED_PRODUCT")

        comparison_page = {
            "page_type": "comparison",
            "products": [
                {
                    "name": product["name"],
                    "price": product.get("price"),
                    "features": product.get("features", [])
                },
                {
                    "name": "Generic Competitor",
                    "price": "Lower",
                    "features": ["Basic functionality"]
                }
            ]
        }

        bus.publish("COMPARISON_PAGE", comparison_page)
        print(" ComparisonAgent ran")




