# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    state = fields.Selection(selection_add=[('preCancel', 'For Cancellation')])   
    def action_precancel(self):
        self.ensure_one()
        self.state = 'preCancel'
        return True
    


