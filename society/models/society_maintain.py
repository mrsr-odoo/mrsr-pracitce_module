from datetime import datetime
from odoo import models,fields,api
class SocietyMaintenance(models.Model):
    _name="society.maintain"
    _description="Maintenance pay"
    _rec_name="room_id"

    room_id=fields.Many2one("society.resident",required=True)
    current_year = datetime.now().year
    current_month=datetime.now().month
    date= fields.Date("Due Date",default=datetime.strptime('%s-%s-12' % (current_year,current_month),'%Y-%m-%d')    )
    # date=fields.Date()
    name=fields.Char(related="room_id.owner")
    amount=fields.Integer(default=1500,readonly=True)
    state=fields.Selection(string="Payment status",
                            selection=[("pending","Pending"),("paid","Paid"),("due","Due")],
                            default="pending")
    
    seq=fields.Char(string="M Number",required=True,readonly=True,default=lambda self:('New'))
    @api.model
    def create(self, vals_list):
        vals_list['seq']=self.env['ir.sequence'].next_by_code('society.maintain')
        return super(SocietyMaintenance,self).create(vals_list)

    # @api.depends("room_id.room_no")
    # def _compute_name(self):
    #     for record in self:
    #         record.name=record.room_id.owner_id.name

    def paid_action(self):
        for record in self:
            record.status="paid"
    

            
