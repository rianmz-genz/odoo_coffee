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

class UserToken(models.Model):
    _name = 'user.token'
    
    user_id = fields.Many2one('res.users')
    token = fields.Char()
    