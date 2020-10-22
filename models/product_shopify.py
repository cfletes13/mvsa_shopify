# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_studio_image_shopify = fields.Binary(string='Imagen Sopify',
                                           store=True, attachment=True)
    x_studio_website_shopify = fields.Boolean(default=False,
                                              string='Website Shopify')
