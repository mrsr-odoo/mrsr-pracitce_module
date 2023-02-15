from odoo import models,fields
class SocietyHelp(models.Model):
    _name="society.help"
    _description="Need help"
    _rec_name="subject"

    
    
    room_id=fields.Many2one("society.resident",required=True)
    staff_id=fields.Many2one("society.staff")
    subject=fields.Char(required=True)
    description=fields.Text()