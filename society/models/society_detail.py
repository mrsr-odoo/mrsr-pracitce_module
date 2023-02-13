from odoo import models,fields 
class SocietyDetail(models.Model):
    _name="society.detail"
    _description="Description of society"

    name=fields.Char(required=True)
    block_count=fields.Integer()
    room_count=fields.Integer()
    location=fields.Char()
    garden=fields.Boolean()
    rules=fields.Text()