# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class sp_website(models.Model):
    _inherit = 'product.template'
    _description = 'sp_website'

    @api.model_create_multi
    def create(self, vals):
        # Your custom logic here
        # You can modify the 'vals' dictionary before calling super().create()
        
        # Call the original create method
       product = super(sp_website, self).create(vals)

       URL = "https://depotsarl.com/ecomerce/odoo/api.php"
       PARAMS = {'action':'post_edit','id':product.id}
       requests.get(url = URL, params = PARAMS)
       #requests.get("https://depotsarl.com/ecomerce/odoo/api.php?action=post_edit&id="product.id)
        # Add custom behavior here if needed

       return product
    #name = fields.Char()
    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    #@api.depends('value')
    #def _value_pc(self):
     #   for record in self:
      #      record.value2 = float(record.value) / 100
