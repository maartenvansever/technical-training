from odoo import models, fields

class ProductConnectModel(models.Model):
    _name = "connect.subscription.product"
    _description = "This defines the product fields"

    name = fields.Char()
    price = fields.Float()
    amount = fields.Float()




