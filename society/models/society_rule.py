from odoo import models,fields 
class SocietyRules(models.Model):
    _name="society.rule"
    _description="Rules of society"
    name=fields.Char(required=True)
    soc_id=fields.Many2one("society.detail")