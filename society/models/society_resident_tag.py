from odoo import models,fields
class SocietyResidentTag(models.Model):
    _name="society.resident.tag"
    _description="Type of flats"

    name=fields.Char(required=True)