from odoo import models,fields 
class SocietyBlock(models.Model):
    _name="society.block"
    _description="Blocks of Society"

    name=fields.Char(required=True)