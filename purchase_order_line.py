from odoo import api, fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    def _get_product_purchase_description(self, product_lang):
        # handle the case where display_name is empty
        if not product_lang.display_name:
            self.ensure_one()
            name = product_lang.name
            if product_lang.description_purchase:
                name += '\n' + product_lang.description_purchase
            return name
        else:
            super()._get_product_purchase_description(product_lang)