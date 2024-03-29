# Copyright 2020 Coop IT Easy SC
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Export CSV Base",
    "version": "12.0.1.1.0",
    "depends": ["account", "sftp_backend"],
    "author": "Coop IT Easy SC",
    "summary": "Base to create module to export csv files.",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "data": [
        "data/data.xml",
        "security/ir.model.access.csv",
        "views/csv_export_history.xml",
        "views/menu.xml",
    ],
    "installable": True,
}
