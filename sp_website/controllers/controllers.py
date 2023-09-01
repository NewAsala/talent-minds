# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SpWebsite(http.Controller):
    @http.route('/sp_website/sp_website', auth='public')
    def index(self, **kw):
        #return "Hello, world"
        return request.render('sp_website.test_page',{})

#     @http.route('/sp_website/sp_website/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sp_website.listing', {
#             'root': '/sp_website/sp_website',
#             'objects': http.request.env['sp_website.sp_website'].search([]),
#         })

#     @http.route('/sp_website/sp_website/objects/<model("sp_website.sp_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sp_website.object', {
#             'object': obj
#         })
