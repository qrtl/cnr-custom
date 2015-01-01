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

from openerp.tools.translate import _
from openerp import models, fields, api, _

class purchase_order(models.Model):

    _inherit = "purchase.order"

    free_ship_from = fields.Float(string='Free Shipping From',
                                  related='partner_id.free_ship_from')
    preferred_order_method = fields.Selection(string='Preferred Order Method',
                                         related='partner_id.preferred_order_method')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
