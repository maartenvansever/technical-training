from odoo import models, fields, api

class InheritedAccountMove(models.Model):
    _inherit = "account.move"

    book_keeper = fields.Char()
