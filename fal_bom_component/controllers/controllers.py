# -*- coding: utf-8 -*-
# from odoo import http


# class FalBomComponent(http.Controller):
#     @http.route('/fal_bom_component/fal_bom_component', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fal_bom_component/fal_bom_component/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fal_bom_component.listing', {
#             'root': '/fal_bom_component/fal_bom_component',
#             'objects': http.request.env['fal_bom_component.fal_bom_component'].search([]),
#         })

#     @http.route('/fal_bom_component/fal_bom_component/objects/<model("fal_bom_component.fal_bom_component"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fal_bom_component.object', {
#             'object': obj
#         })

