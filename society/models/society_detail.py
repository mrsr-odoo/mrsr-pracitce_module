from odoo import models,fields 
class SocietyDetail(models.Model):
    _name="society.detail"
    _description="Description of society"
    
    name=fields.Char(required=True)
    tag_ids=fields.Many2many("society.resident.tag")
    block_count=fields.Char()
    room_count=fields.Char()
    location=fields.Char()
    garden=fields.Boolean()
    temple=fields.Boolean()
    rules=fields.Text()