# Copyright 2020 Coop IT Easy SC
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Export Invoice CSV",
    "version": "12.0.1.1.0",
    "depends": [
        "csv_export_base",
        "l10n_be_invoice_bba",
        "provelo_analytic_account",
    ],
    "author": "Coop IT Easy SC",
    "summary": "Export your invoices as CSV flat files",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "data": [
        "data/cron.xml",
        "views/account_invoice.xml",
        "views/account_tax.xml",
        "views/export_csv_invoice.xml",
        "views/menu.xml",
    ],
    "installable": True,
}
