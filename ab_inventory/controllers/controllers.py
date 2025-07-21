# -*- coding: utf-8 -*-
# from odoo import http


# class AbInventory(http.Controller):
#     @http.route('/ab_inventory/ab_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ab_inventory/ab_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ab_inventory.listing', {
#             'root': '/ab_inventory/ab_inventory',
#             'objects': http.request.env['ab_inventory.ab_inventory'].search([]),
#         })

#     @http.route('/ab_inventory/ab_inventory/objects/<model("ab_inventory.ab_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ab_inventory.object', {
#             'object': obj
#         })
