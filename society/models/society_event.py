from odoo import models,fields,api
from odoo.exceptions import UserError
class SocietyEvent(models.Model):
    _name="society.event"
    _description="Events in Society"
    _rec_name="subject"
    # name=fields.Char()
    subject=fields.Char(required=True)
    event_date=fields.Date(default=lambda self:fields.Date.today())
    room_id=fields.Many2one("society.resident",required=True)
    organizer=fields.Char(related="room_id.owner")
    state=fields.Selection(string="Request status",
                    selection=[('new','New'),('request','Requested'),('approve','Approved'),('complete','Completed'),('refuse','Refused')],
                    default="new")

    
    # @api.depends("room_id")
    # def _compute_organizer(self):
    #     for record in self:
    #         record.organizer=record.room_id.owner_id.name

    def approve_action(self):
        for rec in self:
            if rec.state not in ('complete','refuse'):
                rec.state="approve"
    
        return True
    
    def refuse_action(self):
        for rec in self:
            rec.state="refuse"
            
            # if rec.state not in ('complete','approve'):
            #     rec.state="refuse"
            # else:
            #     raise UserError("You cannot refuse ")
        return True
    
    def complete_button(self):
        for rec in self:
            rec.state="complete"
        return True

    def request_action(self):
        for rec in self:
            rec.state="request"


    seq_pr=fields.Char(string="E Number",required=True,readonly=True,default=lambda self:('New') )
    @api.model
    def create(self,vals):
        vals['seq_pr']=self.env['ir.sequence'].next_by_code('society.event')
        return super(SocietyEvent,self).create(vals)
