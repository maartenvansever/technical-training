from odoo import models, fields

class PartnerConnectModel(models.Model):
    _name = "connect.partner"
    _description = "This defines the connect partners"

    name = fields.char()
    split_biller = fields.Boolean(required=True)