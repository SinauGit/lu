# Copyright 2022 CreuBlanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    reconcile_mode = fields.Selection(
        [("edit", "Edit Move"), ("keep", "Keep Suspense Accounts")],
        default="edit",
        required=True,
    )

    def get_rainbowman_message(self):
        self.ensure_one()
        if self.get_journal_dashboard_datas()["number_to_reconcile"] > 0:
            return False
        return _("Well done! Everything has been reconciled")
    
    def open_action(self):
        if self.type in ('bank', 'cash'):
            return {
                'name': "Cash & Bank Reconciliation",
                'type': 'ir.actions.act_window',
                'view_mode': 'kanban,tree',
                'res_model': 'account.bank.statement.line',
                'domain': [('journal_id','=',self.id)],
                'context': {'default_journal_id': self.id, 'default_date': fields.Date.today(), 'view_ref': 'account_reconcile_oca.bank_statement_line_form_reconcile_view'}
            }
        return super().open_action()

    def create_cash_statement(self):
        return {
                'name': "Cash & Bank Reconciliation",
                'type': 'ir.actions.act_window',
                'view_mode': 'kanban,tree',
                'res_model': 'account.bank.statement.line',
                'domain': [('journal_id','=',self.id)],
                'context': {'default_journal_id': self.id, 'default_date': fields.Date.today(), 'view_ref': 'account_reconcile_oca.bank_statement_line_form_reconcile_view'}
            }
