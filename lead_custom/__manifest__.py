# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Iprog CRM Custom', 
    'version': '1.0',
    'category': 'crm customization',
    'author': 'Odoo PS',
    'license' :'LGPL-3',
    'description': """ added fields in opportunity form view""",
    'depends':['base', 'crm'],
    'data' : [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
}
