from odoo import models, fields

class PartnerConnectSubscriptionTypeModel(models.Model):
    _name = "connect.partner.subscription.type"
    _description = "This defines the connect partners types."

    name = fields.Char()
    total=  fields.float()
    product_ids = fields.Many2many("connect.subscription.product",
                                   string="Product",
                                   relation='connect_type_product_rel')

    @api.depends('total')
    def _compute_total(self):
        for record in self:
            record.total = record.total + (record.product_ids.price * record.product_ids.amount)


