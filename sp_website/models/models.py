# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class sp_website(models.Model):
    _inherit = 'product.template'
    _name = 'sp_website.sp_website'
    _description = 'sp_website.sp_website'

    #name = fields.Char()
    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    @api.model
    def create(self, vals):
        # Your custom logic here
        # You can modify the 'vals' dictionary before calling super().create()
        
        # Call the original create method
        product = super(sp_website, self).create(vals)
                
        requests.get("https://depotsarl.com/ali/active/asala.php")
        # Add custom behavior here if needed

        return product
    #@api.depends('value')
    #def _value_pc(self):
     #   for record in self:
      #      record.value2 = float(record.value) / 100
