from core.base_agent import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    def can_act(self, bus):
        # Can act only if product is parsed and questions not generated yet
        return bus.has("PARSED_PRODUCT") and not bus.has("QUESTIONS")

    def act(self, bus):
        product = bus.read("PARSED_PRODUCT")

        questions = [
            f"What is {product['name']}?",
            f"What are the key ingredients of {product['name']}?",
            f"Who should use {product['name']}?",
            f"How is {product['name']} different from alternatives?",
        ]

        bus.publish("QUESTIONS", questions)
        print(" QuestionGeneratorAgent ran")


