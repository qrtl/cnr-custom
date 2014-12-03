# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Rooms For (Hong Kong) Limited (<http://www.openerp-asia.net>).
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

from openerp.osv import fields, osv

class product_template(osv.osv):
    _inherit = "product.template"
    _columns = {
        'name_furigana': fields.char('Furigana', select=True),
        'packaging': fields.selection([('barrel','Barrel'),('circular','Circular Box'),('cup','Cup'),('box','Box'),('pack','Pack')], 'Packaging'),
        'shipping_method': fields.selection([('regular','Regular'), ('cool','Cool')], 'Shipping Method'),
        'display_stock': fields.integer('Display Stock'),
        'net_weight': fields.float('Net Weight'),
        'gross_weight': fields.float('Gross Weight'),
        'days_until_ship': fields.integer('Days until Shipping'),
        'purch_lead_time': fields.integer('Purchasing Lead Time'),
        'ship_weight': fields.float('Shipping Weight'),
        'ship_height': fields.float('Shipping Height'),
        'ship_width': fields.float('Shipping Width'),
        'ship_length': fields.float('Shipping Length'),
        'ingredients': fields.text('Materials/Ingredients', translate=True),
        'salt_percent': fields.float('Salt %'),
        'allergy': fields.selection([('wheat','Wheat'),('egg','Egg'),('peanut','Peanut')], 'Allergy'),
        'designer': fields.selection([('designer1','Designer 1'),('designer2','Designer 2')], 'Designer'),
        'manufacture_country': fields.many2one('res.country', 'Manufacture Country', ondelete='restrict'),
        'alcohol_percent': fields.float('Alcohol %'),
        'buyer': fields.many2one('res.partner', 'Buyer', domain=[('is_company','=',False)]),
        'buyer_commission': fields.float('Buyer Commission'),
    }
