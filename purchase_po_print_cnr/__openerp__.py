# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Rooms For (Hong Kong) Limited T/A OSCG (<http://www.openerp-asia.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Purchase Order Print',
    'version': '1.0',
    'category': 'Purchase',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'summary': 'Makes adjustments to PO print format',
    'description': """
* Makes adjustments to PO print format
* Adds a text field in company definition to keep fixed remarks to be printed on PO
    """,
    'depends': ["purchase"], 
    'data': [
        'res_company_view.xml',
        'views/report_purchaseorder_z1.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
