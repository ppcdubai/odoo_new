from odoo import models, fields


class HrContractOvertime(models.Model):
    _inherit = 'hr.contract'
    over_hour = fields.Monetary('Overtime Hour Wage')
    over_day = fields.Monetary('Overtime Day Wage')
