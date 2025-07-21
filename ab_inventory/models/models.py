# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            sequence = self.env['ir.sequence'].sudo().search([('code', '=', 'stock.picking.sequence')], limit=1)
            today = datetime.now()
            current_year = today.year
            # current_year = 2025
            sequence_code = 'stock.picking.sequence'
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
        return super(StockPicking, self).create(vals)