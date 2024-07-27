# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritCalendar(models.Model):
    _inherit = 'calendar.event'

    fleet_id = fields.Many2one("fleet.vehicle", string="Fleet", required=True)

