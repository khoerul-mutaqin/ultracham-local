# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    x_studio_purchase_type = fields.Selection(
        selection=[
            ('Lokal', 'Lokal'),
            ('Import', 'Import'),
            ],
        string='Purchase Type')
    