from core.message_bus import MessageBus
from agents.parser_agent import ProductParserAgent
from agents.question_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent
from agents.product_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent





from product_data import product_data
import json
import os


def run_system(agents, bus):
    """
    Generic scheduler that allows agents to act
    based on shared state, without enforcing order.
    """
    progress = True

    while progress:
        progress = False
        for agent in agents:
            if agent.can_act(bus):
                agent.act(bus)
                progress = True


if __name__ == "__main__":
    bus = MessageBus()

    # Seed the system with raw input
    bus.publish("RAW_PRODUCT", product_data)

    agents = [
        ProductParserAgent(),
        QuestionGeneratorAgent(),
        FAQAgent(),
        ProductPageAgent(),
        ComparisonAgent()    
    ]

    run_system(agents, bus)

    # Persist outputs
    os.makedirs("output", exist_ok=True)

    with open("output/product_page.json", "w") as f:
        json.dump(bus.read("PRODUCT_PAGE"), f, indent=2)

    print("✅ Agentic content generation completed.")


