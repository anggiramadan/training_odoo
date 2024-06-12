# -*- coding: utf-8 -*-
# from odoo import http


# class Capri(http.Controller):
#     @http.route('/capri/capri', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capri/capri/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('capri.listing', {
#             'root': '/capri/capri',
#             'objects': http.request.env['capri.capri'].search([]),
#         })

#     @http.route('/capri/capri/objects/<model("capri.capri"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capri.object', {
#             'object': obj
#         })

