# -*- coding: utf-8 -*-

# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from openerp import fields, models


class CSVExportHistory(models.Model):
    _name = "csv.export.history"
    _order = "date desc"

    date = fields.Datetime(string="Date", required=True)
    path = fields.Char(string="Path", required=True)
    model = fields.Char(string="model", required=True)
    filename = fields.Char(string="File Name", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    success = fields.Boolean(string="Success", required=False)
