# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields ,models


class AccountMove(models.Model):
    _inherit = 'crm.lead'

    import_date = fields.Date()
    project_type = fields.Selection([('type_1', 'Fixed Cost'), ('type_2', 'Staff Augmentation')])
    lead_type = fields.Selection([('out_bound', 'Outbound'), ('in_bound', 'Inbound')])
    lead_source = fields.Selection([
            ('source1', 'Client Referral'),
            ('source2', 'LinkedIn'),
            ('source3', 'Calling'),
            ('source4', 'External Referral'),
            ('source5', 'Bidding Platforms'),
            ('source7', 'Email Marketing'),
            ('source8', 'Employee Referral'),
            ('source9', 'Existing Client'),
            ('source10', 'Website'),
            ('source12', 'SEO & Marketing'),
            ('source13', 'Tech Events'),
            ('source14', 'WhatsApp'),
            ('source15', 'Others'),
            ('source16', 'Partners'),
            ('source17', 'Consultants'),
        ])
    recieved_by = fields.Selection([
            ('recieved1', 'Partners'),
            ('recieved2', 'Consultants'),
            ('recieved3', 'Internal Sales Team'),
        ])
    partners = fields.Selection([
            ('recieved1', 'Qodequay'), 
            ('recieved2', 'ScreenRoot'),
            ('recieved3', 'Sumit - Odoo'),
            ('recieved4', 'Sagar - BotSpot'),
            ('recieved5', 'Shabbir'),
            ('recieved6', 'GlobalStep')
        ])
    consultants = fields.Selection([
            ('recieved1', 'Mayur - Australia'),
            ('recieved2', 'AAR Solutions'),
        ])


