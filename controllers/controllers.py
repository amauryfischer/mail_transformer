# -*- coding: utf-8 -*-
from odoo import http

# class FromMailToItems(http.Controller):
#     @http.route('/from_mail_to_items/from_mail_to_items/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/from_mail_to_items/from_mail_to_items/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('from_mail_to_items.listing', {
#             'root': '/from_mail_to_items/from_mail_to_items',
#             'objects': http.request.env['from_mail_to_items.from_mail_to_items'].search([]),
#         })

#     @http.route('/from_mail_to_items/from_mail_to_items/objects/<model("from_mail_to_items.from_mail_to_items"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('from_mail_to_items.object', {
#             'object': obj
#         })