import copy

from templates.page_templates import PRODUCT_PAGE_TEMPLATE
from logicblocks.content_blocks import (
    extract_name_block,
    extract_concentration_block,
    extract_ingredients_block,
    extract_benefits_block,
    extract_usage_block,
    extract_skin_type_block,
    extract_price_block
)


class ProductPageAgent:
    def run(self, product):
        """
        Generates product description page using explicit templates
        and reusable logic blocks.
        """

        page = copy.deepcopy(PRODUCT_PAGE_TEMPLATE)

        page["name"] = extract_name_block(product)
        page["concentration"] = extract_concentration_block(product)
        page["ingredients"] = extract_ingredients_block(product)
        page["benefits"] = extract_benefits_block(product)
        page["usage"] = extract_usage_block(product)
        page["skin_type"] = extract_skin_type_block(product)
        page["price"] = extract_price_block(product)

        return page

