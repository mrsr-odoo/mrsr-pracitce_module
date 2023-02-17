from odoo import models,fields,api
from odoo.exceptions import UserError
class SocietyEvent(models.Model):
    _name="society.event"
    _description="Events in Society"
    _rec_name="subject"
    # name=fields.Char()
    subject=fields.Char(required=True)
    event_date=fields.Date()
    room_id=fields.Many2one("society.resident")
    organizer=fields.Char(compute="_compute_organizer")
    event_status=fields.Selection(string="Request status",
                    selection=[('refuse','Refused'),('approve','Approved'),('complete','Completed')])

    
    @api.depends("room_id")
    def _compute_organizer(self):
        for record in self:
            record.organizer=record.room_id.owner_id.name

    def approve_action(self):
        for rec in self:
            if rec.event_status not in ('complete','refuse'):
                rec.event_status="approve"
            else:
                raise UserError("You must plan another event")
        return True
    
    def refuse_action(self):
        for rec in self:
            if rec.event_status not in ('complete','approve'):
                rec.event_status="refuse"
            else:
                raise UserError("You cannot refuse ")
        return True
    
    def complete_button(self):
        for rec in self:
            if rec.event_status not in ('refuse'):
                rec.event_status="complete"
            else:
                UserError("Event is completed")

        return True