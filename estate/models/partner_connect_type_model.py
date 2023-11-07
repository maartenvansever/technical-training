from odoo import models, fields, api

class PartnerConnectSubscriptionTypeModel(models.Model):
    _name = "connect.partner.subscription.type"
    _description = "This defines the connect partners types."

    name = fields.Char()
    total=  fields.Float(compute='_compute_total')
    product_ids = fields.Many2many("connect.subscription.product",
                                   string="Product",
                                   relation='connect_type_product_rel')
    total_taxed = fields.Float(compute='_compute_total_taxed', inverse="_inverse_total_taxed")
    tax = fields.Float()

    @api.depends('total', 'tax')
    def _compute_total_taxed(self):
        for record in self:
            record.total_taxed = record.total * record.tax
    def _inverse_total_taxed(self):
        for record in self:
            record.tax = record.total_taxed / record.total

    @api.depends('product_ids.price', 'product_ids.amount')
    def _compute_total(self):
        for record in self:
            for product in record.product_ids:
                record.total += product.price * product.amount


