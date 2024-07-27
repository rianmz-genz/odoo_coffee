# -*- coding: utf-8 -*-
# from odoo import http


# class Mycoffee(http.Controller):
#     @http.route('/mycoffee/mycoffee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mycoffee/mycoffee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mycoffee.listing', {
#             'root': '/mycoffee/mycoffee',
#             'objects': http.request.env['mycoffee.mycoffee'].search([]),
#         })

#     @http.route('/mycoffee/mycoffee/objects/<model("mycoffee.mycoffee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mycoffee.object', {
#             'object': obj
#         })

