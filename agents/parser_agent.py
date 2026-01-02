from core.base_agent import BaseAgent

class ProductParserAgent(BaseAgent):

    def can_act(self, bus):
        # Can act only if raw product exists AND parsed product does not
        return bus.has("RAW_PRODUCT") and not bus.has("PARSED_PRODUCT")

    def act(self, bus):
        raw = bus.read("RAW_PRODUCT")

        parsed = {
            "name": raw.get("name"),
            "category": raw.get("category"),
            "price": raw.get("price"),
            "features": raw.get("features", [])
        }

        bus.publish("PARSED_PRODUCT", parsed)


