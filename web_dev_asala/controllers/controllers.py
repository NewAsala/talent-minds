# -*- coding: utf-8 -*-
# from odoo import http


# class WebDevAsala(http.Controller):
#     @http.route('/web_dev_asala/web_dev_asala', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_dev_asala/web_dev_asala/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_dev_asala.listing', {
#             'root': '/web_dev_asala/web_dev_asala',
#             'objects': http.request.env['web_dev_asala.web_dev_asala'].search([]),
#         })

#     @http.route('/web_dev_asala/web_dev_asala/objects/<model("web_dev_asala.web_dev_asala"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_dev_asala.object', {
#             'object': obj
#         })
