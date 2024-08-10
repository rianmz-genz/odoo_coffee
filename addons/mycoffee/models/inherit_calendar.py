from odoo import models, fields, api
import logging
import hashlib

logger = logging.getLogger(__name__)

class CalendarInherit(models.Model):
    _inherit = 'calendar.event'
    
    sale_ids = fields.Many2many('sale.order', 'calendar_sale_rel', 'calendar_id', 'sale_id', string='Sales Orders')
    fleet_ids = fields.Many2many('fleet.vehicle', 'calendar_fleet_rel', 'calendar_id', 'fleet_id', string='Fleets')

class SaleInherit(models.Model):
    _inherit = 'sale.order'
    
    calendar_ids = fields.Many2many('calendar.event', 'calendar_sale_rel', 'sale_id', 'calendar_id', string='Calendars')
    fleet_ids = fields.Many2many('fleet.vehicle', 'sale_fleet_rel', 'sale_id', 'fleet_id', string='Fleets')

class FleetInherit(models.Model):
    _inherit = 'fleet.vehicle'
    
    calendar_ids = fields.Many2many('calendar.event', 'calendar_fleet_rel', 'fleet_id', 'calendar_id', string='Calendars')
    sale_ids = fields.Many2many('sale.order', 'sale_fleet_rel', 'fleet_id', 'sale_id', string='Sales Orders')

class UserInherit(models.Model):
    _inherit = 'res.users'
    
    token = fields.Char('Token', compute='_compute_token')

    def _compute_token(self):
        for user in self:
            # Contoh logika untuk menghitung token
            # Anda bisa mengganti ini dengan logika sesuai kebutuhan
            if user.id:
                token_string = f"user_{user.id}_{user.login}"
                user.token = hashlib.sha256(token_string.encode('utf-8')).hexdigest()
            else:
                user.token = False
