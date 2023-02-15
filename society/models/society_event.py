from odoo import models,fields
class SocietyEvent(models.Model):
    _name="society.event"
    _description="Events in Society"

    name=fields.Char()
    subject=fields.Char()
    event_date=fields.Date()
    room_id=fields.Many2one("society.resident")