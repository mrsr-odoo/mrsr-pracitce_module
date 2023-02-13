from odoo import models,fields 
class SocietyResident(models.Model):
    _name="society.resident"
    _description="Residential Society"

    room_no=fields.Char(required=True)
    owner=fields.Char()
    block=fields.Char()
    society_name=fields.Char()
    members=fields.Char()
    