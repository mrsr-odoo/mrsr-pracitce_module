from odoo import models,fields 
class SocietyResident(models.Model):
    _name="society.resident"
    _description="Residential Society"
    _rec_name="room_no"

    room_no=fields.Char(required=True)
    owner=fields.Many2one('res.users')
    block=fields.Many2one('society.block')
    society_name=fields.Many2one('society.detail')
    members=fields.Char()
    contact_no=fields.Char()