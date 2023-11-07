from odoo import models, fields

class PartnerConnectSubscriptionTypeModel(models.Model):
    _name = "connect.partner.subscription.type"
    _description = "This defines the connect partners types."

    name = fields.Char()
    product_ids = fields.Many2many("connect.subscription.product",
                                   string="Product",
                                   relation='connect_type_product_rel')



