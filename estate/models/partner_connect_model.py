from odoo import models, fields

class PartnerConnectModel(models.Model):
    _name = "connect.partner"
    _description = "This defines the connect partners."

    name = fields.Char()
    split_biller = fields.Boolean()
    active = fields.Boolean()