import json

from product_data import PRODUCT_DATA
from agents.parser_agent import ProductParserAgent
from agents.question_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent
from agents.product_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent


def save_json(data, filename):
    with open(f"output/{filename}", "w") as f:
        json.dump(data, f, indent=2)


def main():
    # Step 1: Parse product data
    parser = ProductParserAgent()
    product = parser.run(PRODUCT_DATA)

    # Step 2: Generate questions
    question_agent = QuestionGeneratorAgent()
    questions = question_agent.run(product)

    # Step 3: Generate FAQ page
    faq_agent = FAQAgent()
    faq_page = faq_agent.run(questions, product)

    # Step 4: Generate Product page
    product_agent = ProductPageAgent()
    product_page = product_agent.run(product)

    # Step 5: Generate Comparison page
    comparison_agent = ComparisonAgent()
    comparison_page = comparison_agent.run(product)

    # Save outputs
    save_json(faq_page, "faq.json")
    save_json(product_page, "product_page.json")
    save_json(comparison_page, "comparison_page.json")


if __name__ == "__main__":
    main()
