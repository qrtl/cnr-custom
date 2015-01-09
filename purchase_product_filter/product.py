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


class product_product(osv.osv):
    _inherit = "product.product"
    
    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        if context and context.get('prod_filter', False) and context.get('supplier_id', False):
            sql = """
            select id from product_product
            where product_tmpl_id in
                ( select distinct(product_tmpl_id)
                from product_supplierinfo
                where name = %s )
            """ % (context.get('supplier_id'))
            cr.execute(sql)
            ids = [x[0] for x in cr.fetchall()]
            args.append(('id', 'in', ids))
            order = 'default_code'
        return super(product_product, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)

