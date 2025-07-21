from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_print_invoice(self):
        return self.env.ref('ab_invoice_report.report_invoice_action').report_action(self)

    def payment_method(self):
        bill = [
            ('ref', 'ilike', self.name),
        ]
        return self.env['account.payment'].search(bill)

    def ammount_totals(self):
        total = 0
        for line in self.line_ids:
            total += line.price_subtotal
        return total