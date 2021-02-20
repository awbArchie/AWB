# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = "account.payment"
                           
    state = fields.Selection(selection_add=[('preCancel', 'For Cancellation')])                           
    def action_precancel(self):
        self.ensure_one()
        self.state = 'preCancel'
        return True



