from odoo import models, fields, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_sequence = fields.Char(string='Custom Sequence')

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.order.sequence') or '/'
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        if 'name' not in vals and 'custom_sequence' not in vals:
            vals['custom_sequence'] = self.name
        return super(SaleOrder, self).write(vals)
    



class AccountMove(models.Model):
    _inherit = 'account.move'

    custom_sequence = fields.Char(string='Custom Sequence')

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', '/') == '/':
    #         vals['name'] = self.env['ir.sequence'].next_by_code('account.move.sequence') or '/'
    #     return super(AccountMove, self).create(vals)
    
    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            journal = self.env['account.journal'].browse(vals.get('journal_id'))
            if journal.type == 'sale':
                sequence = self.env['ir.sequence'].sudo().search([('code', '=', 'account.move.sequence')], limit=1)
                today = datetime.now()
                current_year = today.year
                # current_year = 2025
                sequence_code = 'account.move.sequence'
                sequence_number = sequence.next_by_code(sequence_code) or '/'
                existing_sequence = sequence.search([('code', '=', sequence_code)])
                if existing_sequence:
                    if existing_sequence.suffix:
                        # Check if the suffix contains '%(year)s' format
                        if '%(year)s' in existing_sequence.suffix:
                            # Get the last sequence number and its year
                            last_sequence_year = int(sequence_number.split('/')[-1])
                            # If the last sequence year is different from the current year, reset the sequence number
                            if last_sequence_year != current_year:
                                sequence.write({'number_next_actual': 1,
                                                # 'suffix': '/LUI-WH/2025',
                                                })
                                sequence_number = sequence.next_by_code(sequence_code) or '/'
                vals['name'] = sequence_number
            if journal.type == 'cash':
                sequence = self.env['ir.sequence'].sudo().search([('code', '=', 'cash.sequence')], limit=1)
                today = datetime.now()
                current_year = today.year
                # current_year = 2026
                nilai = int(str(current_year)[2:])
                sequence_code = 'cash.sequence'
                sequence_number = sequence.next_by_code(sequence_code) or '/'
                existing_sequence = sequence.search([('code', '=', sequence_code)])
                if existing_sequence:
                    if existing_sequence.prefix:
                        # Check if the prefix contains '%(year)s' format
                        # if str(nilai) in existing_sequence.prefix.split('/')[-1]:
                            # Get the last sequence number and its year
                            last_sequence_year = int(sequence_number.split('/')[-1])
                            # If the last sequence year is different from the current year, reset the sequence number
                            if int(existing_sequence.prefix.split('/')[-1]) != nilai:
                                sequence.write({'number_next_actual': 1,
                                                'prefix': f"""{journal.code}/{nilai}"""
                                                # 'suffix': '/LUI-WH/2025',
                                                })
                                sequence_number = sequence.next_by_code(sequence_code) or '/'
                sequence.write({'prefix': f"""{journal.code}/{nilai}"""})
                vals['name'] = sequence_number
                vals['name'] = sequence_number
            if journal.type == 'bank':
                sequence = self.env['ir.sequence'].sudo().search([('code', '=', 'bank.sequence')], limit=1)
                today = datetime.now()
                # current_year = today.year
                current_year = 2026
                nilai = int(str(current_year)[2:])
                sequence_code = 'bank.sequence'
                sequence_number = sequence.next_by_code(sequence_code) or '/'
                existing_sequence = sequence.search([('code', '=', sequence_code)])
                if existing_sequence:
                    if existing_sequence.prefix:
                        # Check if the prefix contains '%(year)s' format
                        # if str(nilai) in existing_sequence.prefix.split('/')[-1]:
                            # Get the last sequence number and its year
                            last_sequence_year = int(sequence_number.split('/')[-1])
                            # If the last sequence year is different from the current year, reset the sequence number
                            if int(existing_sequence.prefix.split('/')[-1]) != nilai:
                                sequence.write({'number_next_actual': 1,
                                                'prefix': f"""{journal.code}/{nilai}"""
                                                # 'suffix': '/LUI-WH/2025',
                                                })
                                sequence_number = sequence.next_by_code(sequence_code) or '/'
                sequence.write({'prefix': f"""{journal.code}/{nilai}"""})
                vals['name'] = sequence_number
        return super(AccountMove, self).create(vals)

class ResCompany(models.Model):
    _inherit = 'res.company'

    director_id = fields.Many2one('res.partner', string='Direktur')