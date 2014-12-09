# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 - hiro TAKADA. All Rights Reserved
#    @author hiro TAKADA <hiro@thdo.biz>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Monthly Billing',
    'version': '1.0.0',
    'category': 'Tools',
    'author': 'hiro TAKADA',
    'summary': 'Add Monthly Billing',
    'description': """
    - Add Closing Date field to Payment Term
    """,
    'depends': ["account"], 
    'data': [
        'account_monthly_billing.xml',
#        'tg_partner_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}