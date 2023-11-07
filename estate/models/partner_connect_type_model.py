from odoo import models, fields, api

class PartnerConnectSubscriptionTypeModel(models.Model):
    _name = "connect.partner.subscription.type"
    _description = "This defines the connect partners types."

    name = fields.Char()
    total=  fields.Float(compute='_compute_total')
    product_ids = fields.Many2many("connect.subscription.product",
                                   string="Product",
                                   relation='connect_type_product_rel')

    @api.depends('product_ids.price', 'product_ids.amount')
    def _compute_total(self):
        for record in self:
            for product in record.product_ids:
                record.total += product.price * product.amount


