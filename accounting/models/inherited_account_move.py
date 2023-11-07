from odoo import models, fields, api

class InheritedAccountMove(models.Model):
    _inherit = "account.move"

    book_keeper = fields.Char()

    def action_fill_book_keeper(self):
        self.book_keeper = "some user"
        return True