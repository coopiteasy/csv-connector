# Copyright 2020 Coop IT Easy SC
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "SFTP Backend",
    "version": "12.0.1.0.0",
    "depends": ["base"],
    "author": "Coop IT Easy SC",
    "summary": "SFTP backend utils.",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "views/backend_sftp.xml",
        "views/menu.xml",
    ],
    "external_dependencies": {"python": ["paramiko"]},
    "installable": True,
}
