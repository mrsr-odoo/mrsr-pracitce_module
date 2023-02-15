from odoo import models,fields 
class SocietyStaff(models.Model):
    _name="society.staff"
    _description="Staff member of society"

    name=fields.Char(required=True)
    mobile_no=fields.Char()
    