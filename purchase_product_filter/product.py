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
# from osv import osv, fields

class product_product(osv.osv):
    _name = "product.product"
    _inherit = "product.product"
    
    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        if context:
            supplier_id = context.get('supplier_id', False)
#             prod_ids = self.search(cr, uid, [])
            if supplier_id:
#                 cr.execute("SELECT distinct(product_id) FROM product_supplierinfo where name = %s" % (supplier_id))
                prodsupp_obj = self.pool.get('product.supplierinfo')
                prod_tmpl_ids = prodsupp_obj.search(cr, uid, [('name','=',supplier_id)])
#                 prod_tmpl_ids = set(prod_tmpl_ids)
#                 prod_ids = self.search(cr, uid, [('product_tmpl_id','in',prod_tmpl_ids)])
#                 prod_ids = prod_obj.search(cr, uid, [('product_tmpl_id','in',prod_tmpl_ids)])
                args.append(('id','in',prod_tmpl_ids))
#         if context and context.get('supplier_id', False):
#             product_limit = self.pool.get('res.partner').read(cr,uid,context['supplier_id'],['supplier_product_limit'])['supplier_product_limit']
#             if product_limit:
#                 #    ids = []
#                 cr.execute("SELECT distinct(product_id) FROM product_supplierinfo where name = %s" % (context.get('supplier_id')))
#                 ids = [x[0] for x in cr.fetchall()]
#                 args.append(('id', 'in', ids))
                order = 'default_code'
        return super(product_product, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)

#     def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
#         if context is None:
#             context = {}
#         if context.get('search_default_categ_id'):
#             args.append((('categ_id', 'child_of', context['search_default_categ_id'])))
#         return super(product_product, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)
