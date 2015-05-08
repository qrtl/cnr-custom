# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

import urllib
import urlparse

# from openerp import tools
# from openerp import SUPERUSER_ID
from openerp.osv import osv, fields
from openerp.tools.translate import _


class MailMail(osv.Model):
    _inherit = ['mail.mail']

    def _get_unsubscribe_url(self, cr, uid, mail, email_to, msg=None, context=None):
        base_url = self.pool.get('ir.config_parameter').get_param(cr, uid, 'web.base.url')
        url = urlparse.urljoin(
            base_url, 'mail/mailing/%(mailing_id)s/unsubscribe?%(params)s' % {
                'mailing_id': mail.mailing_id.id,
                'params': urllib.urlencode({'db': cr.dbname, 'res_id': mail.res_id, 'email': email_to})
            }
        )
        return _('<small><a href="%s">%s</a></small>') % (url, msg or _('Click to unsubscribe'))
