from odoo import models, fields

class PartnerConnectModel(models.Model):
    _name = "connect.partner"
    _description = "This defines the connect partners."

    name = fields.Char()
    split_biller = fields.Boolean()
    active = fields.Boolean(default=True)
    phone_number = fields.Char()
    partner_id = fields.Many2one("res.partner", string="Partner")
    subscription_type = fields.Many2Many("connect.partner.subscription.type", string="Subscription")