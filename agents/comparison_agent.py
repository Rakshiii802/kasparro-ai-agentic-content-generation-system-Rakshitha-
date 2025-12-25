import copy

from templates.page_templates import COMPARISON_PAGE_TEMPLATE
from logicblocks.content_blocks import (
    extract_product_summary_block,
    generate_fictional_product_block
)


class ComparisonAgent:
    def run(self, product):
        """
        Generates comparison page using reusable logic blocks
        and explicit template definition.
        """

        page = copy.deepcopy(COMPARISON_PAGE_TEMPLATE)

        product_a = extract_product_summary_block(product)
        product_b = generate_fictional_product_block()

        page["products"].append(product_a)
        page["products"].append(product_b)

        return page

