from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountAccount(models.Model):
    _inherit = "account.account"

    purchase_reconciliation = fields.Boolean(string="Purchase Reconciliation", default=False)
    cash_limit = fields.Float(string="Cash Limit")


class AccountPayment(models.Model):
    _inherit = "account.payment"

    internal_purchase = fields.Boolean(string="Purchase Transfer Internal", defualt=False)
