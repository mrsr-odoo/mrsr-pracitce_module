from odoo import models,fields 
class SocietyDetail(models.Model):
    _name="society.detail"
    _description="Description of society"
    
    name=fields.Char(required=True)
    block_count=fields.Char()
    room_count=fields.Integer()
    location=fields.Char()
    garden=fields.Boolean()
    temple=fields.Boolean()
    rule_ids=fields.One2many("society.rule","soc_id")
    garden_area=fields.Integer(default=10)