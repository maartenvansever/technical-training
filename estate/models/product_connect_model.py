from odoo import models, fields

class ProductConnectModel(models.Model):
    _name = "connect.partner.subscription.product"
    _description = "This defines the product fields"

    name = fields.Char()
    price = fields.Float()
    amount = fields.Float()




