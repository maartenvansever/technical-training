from odoo import models, fields

class PartnerConnectSubscriptionTypeModel(models.Model):
    _name = "connect.partner.subscription.type"
    _description = "This defines the connect partners types."

    name = fields.Char()


