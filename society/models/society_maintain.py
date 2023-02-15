from odoo import models,fields
class SocietyMaintenance(models.Model):
    _name="society.maintain"
    _description="Maintenance pay"
    _rec_name="room_id"

   
    room_id=fields.Many2one("society.resident",required=True)
    date=fields.Date()
    amount=fields.Integer()