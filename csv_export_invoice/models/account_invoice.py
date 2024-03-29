# Copyright 2021 Coop IT Easy SC
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    export_to_sftp = fields.Datetime(
        copy=False,
        string="Exported to SFTP",
    )
