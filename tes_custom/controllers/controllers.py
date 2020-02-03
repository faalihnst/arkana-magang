# -*- coding: utf-8 -*-
from odoo import http

# class Tes.custom(http.Controller):
#     @http.route('/tes.custom/tes.custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tes.custom/tes.custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tes.custom.listing', {
#             'root': '/tes.custom/tes.custom',
#             'objects': http.request.env['tes.custom.tes.custom'].search([]),
#         })

#     @http.route('/tes.custom/tes.custom/objects/<model("tes.custom.tes.custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tes.custom.object', {
#             'object': obj
#         })