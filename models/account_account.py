from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AccountAccount(models.Model):
    _inherit = "account.account"

    purchase_reconciliation = fields.Boolean(string="Purchase Reconciliation", default=False)
    cash_limit = fields.Float(string="Cash Limit")


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.model
    def create(self, values):
        if 'is_internal_transfer' in values:
            if values['is_internal_transfer']:
                amount = values['amount']
                destination_journal = self.env['account.journal'].browse(values['destination_journal_id'])
                default_account_id = destination_journal.default_account_id
                if default_account_id.purchase_reconciliation:
                    limit = default_account_id.cash_limit

                    balances = {
                        read['account_id'][0]: read['balance']
                        for read in self.env['account.move.line'].read_group(
                            domain=[('account_id', 'in', default_account_id.ids)],
                            fields=['balance', 'account_id'],
                            groupby=['account_id'],
                        )
                    }

                    balance = balances.get(default_account_id.id, 0)
                    if (balance + amount) > limit:
                        maximum_allocation = limit - balance
                        if maximum_allocation < 0:
                            error = "Account Cash transfer limit already Exceeded"
                            raise ValidationError(error)
                        else:
                            error = "You can only transfer LKR " + str(maximum_allocation) + \
                                    " amount. Account transfer limit exceeded"
                            raise ValidationError(error)
        return super(AccountPayment, self).create(values)
