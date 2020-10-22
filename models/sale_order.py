from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def check_min_price(self, order=None):
        company = self.env.user.company_id
        currency_obj = self.env['res.currency']
        diff_currency = False

        if order:
            if order.pricelist_id:
                if order.pricelist_id.currency_id != company.currency_id:
                    diff_currency = True

            for line in order.order_line:
                price_unit = line.price_unit
                if diff_currency:
                    price_unit = order.pricelist_id.currency_id._convert(price_unit, company.currency_id, company, order.date_order or fields.Date.today())

                if line.product_id and (price_unit < line.product_id.minimum_price):
                    raise UserError(_("Price is lower than the minimum product price !  \n Please recheck %s") % (line.product_id.name))
                    return False
        else:
            for order in self:
                if order.pricelist_id:
                    if order.pricelist_id.currency_id != company.currency_id:
                        diff_currency = True

                for line in order.order_line:
                    price_unit = line.price_unit
                    if diff_currency:
                        price_unit = order.pricelist_id.currency_id._convert(price_unit, company.currency_id, company, order.date_order)

                    if line.product_id and (price_unit < line.product_id.minimum_price):
                        raise UserError(_("Price is lower than the minimum product price !  \n Please recheck %s") % (line.product_id.name))
                        return False

        return True

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        self.check_min_price(res)
        return res

    @api.multi
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        self.check_min_price()
        return res