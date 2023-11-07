from odoo import models, fields, api

class InheritedAccountMove(models.Model):
    _inherit = "account.move"

    book_keeper = fields.Char()

    def action_fill_accountant(self):
        """ When an invoice linked to a sales order selling registrations is
        paid confirm attendees. Attendees should indeed not be confirmed before
        full payment. """
        res = super(InheritedAccountMove, self).action_fill_accountant()
        self.book_keeper = "some user"
        return res