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

import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
# from operator import itemgetter
# import time
from types import MethodType

import openerp
from openerp import netsvc, tools, pooler
# from openerp import SUPERUSER_ID, api
from openerp.osv import fields, osv
# from openerp.osv import expression
from openerp.tools.translate import _
# from openerp.tools.float_utils import float_round as round

_logger = logging.getLogger(__name__)

class view_monthly_billing_form(osv.osv):
    _inherit = 'account.payment.term'
    _columns = {
#        'date_valid': fields.boolean('Date Valid'),
        'monthly_closing': fields.boolean('Monthly Closing'),
        'closing_date': fields.integer('Closing Date'),
        }
    _defaults = {
#        'closing_date': 31,
#        'date_valid': False,
        }

    def compute(self, cr, uid, id, value, date_ref=False, context=None):
        if not date_ref:
            date_ref = datetime.now().strftime('%Y-%m-%d')
        pt = self.browse(cr, uid, id, context=context)
        amount = value
        result = []
        obj_precision = self.pool.get('decimal.precision')
        prec = obj_precision.precision_get(cr, uid, 'Account')
        for line in pt.line_ids:
            if line.value == 'fixed':
                amt = round(line.value_amount, prec)
            elif line.value == 'procent':
                amt = round(value * line.value_amount, prec)
            elif line.value == 'balance':
                amt = round(amount, prec)
            if amt:
                if not pt.monthly_closing:
                    next_date = (datetime.strptime(date_ref, '%Y-%m-%d') + relativedelta(days=line.days))
                    if line.days2 < 0:
                        next_first_date = next_date + relativedelta(day=1,months=1) #Getting 1st of next month
                        next_date = next_first_date + relativedelta(days=line.days2)
                    if line.days2 > 0:
                        next_date += relativedelta(day=line.days2, months=1)
                # additional code is here
                #if pt.monthly_closing:
                else:
                    #next_day = line.days
                    #next_day = line.date
                    months_to_add = line.months_added
                    ref_date = datetime.strptime(date_ref, '%Y-%m-%d')
                    if ref_date.day > pt.closing_date:
                        months_to_add += 1
                    next_date = ref_date + relativedelta(day=line.date, months=months_to_add)
                # up to here
                result.append( (next_date.strftime('%Y-%m-%d'), amt) )
                amount -= amt

        amount = reduce(lambda x,y: x+y[1], result, 0.0)
        dist = round(value-amount, prec)
        if dist:
            result.append( (time.strftime('%Y-%m-%d'), dist) )
        return result


class account_payment_term_line(osv.osv):
#    _name = 'account.payment.term'
    _inherit = 'account.payment.term.line'
    _columns = {
        'months_added': fields.integer('Months to Add'),
        'month_end_pay': fields.boolean('Payment at Month End'),
        'date': fields.integer('Date of the Month'),
        }
    _defaults = {
#        'closing_date': 31,
#        'date_valid': False,
        }


