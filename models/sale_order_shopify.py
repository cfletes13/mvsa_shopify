# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderShopify(models.Model):
    _inherit = 'sale.order'

    x_studio_metodo_de_pago = fields.Char(string='Metodo de Pago',)
    x_studio_metodo_de_envio_shopify = fields.Char(string='Metodo de Envio Shopify')
    x_studio_pago_con_gift_cards = fields.Boolean(default=False,
                                                  string='Pago con Gift Cards')
