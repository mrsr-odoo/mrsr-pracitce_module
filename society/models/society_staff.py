from odoo import models,fields 
class SocietyStaff(models.Model):
    _name="society.staff"
    _description="Staff member of society"

    name=fields.Char(required=True)
    sequence=fields.Integer(default=1)
    mobile_no=fields.Char()
    