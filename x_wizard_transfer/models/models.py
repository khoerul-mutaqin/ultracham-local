# -*- coding: utf-8 -*-

from odoo import models, fields, api

class XWizardTransfer(models.Model):
    _name = 'x_wizard_transfer'
    _description = 'X Wizard Transfer'

    x_name = fields.Char()
    x_schedule_date = fields.Datetime(string='Schedule date')
    x_stock_picking = fields.Many2one('stock.picking', string='Picking')


