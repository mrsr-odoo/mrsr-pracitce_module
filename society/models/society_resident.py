from odoo import models,fields 
class SocietyResident(models.Model):
    _name="society.resident"
    _description="Residential Society"

    room_no=fields.Char(required=True)
    owner=fields.Char()
    block=fields.Many2one('society.block')
    society_name=fields.Many2one('society.detail')
    members=fields.Char()
    contact_no=fields.Char()