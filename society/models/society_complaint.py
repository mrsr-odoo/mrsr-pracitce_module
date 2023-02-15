from odoo import models,fields
class SocietyComplaint(models.Model):
    _name="society.complaint"
    _description="complaints"
    _rec_name="subject"

    subject=fields.Char(required=True)
    room=fields.Many2one("society.resident",required=True)
    description=fields.Text()