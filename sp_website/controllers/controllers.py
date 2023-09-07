# -*- coding: utf-8 -*-
from odoo import http

class SpWebsite(http.Controller):
    @http.route('/',type='http', auth='public',website=True)
    def index(self, **kw):
        #return "Hello, world"
        #return http.request.render('sp_website.test_page',{})
        categories = http.request.env['public.category'].search([])
        cat_val =
        {
            'cat':categories,
        }
        return http.request.render('sp_website.test_page',cat_val)

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
