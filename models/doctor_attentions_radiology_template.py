
# -*- coding: utf-8 -*-
##############################################################################
#
#   OpenERP, Open Source Management Solution
#   Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging
_logger = logging.getLogger(__name__)
import openerp
import re
import codecs
from openerp.osv import fields, osv
from openerp.tools.translate import _

class doctor_attentions_radiology_template(osv.osv):

	_name = 'doctor.attentions.radiology.template'

	_columns = {
		'active' : fields.boolean('Plantilla Activa'),
		'attentiont_id': fields.many2one('doctor.attentions.radiology', 'Attention Radiology', ondelete='restrict'),
		'cuerpo' : fields.text(u'Plantilla Texto'),
		'name' : fields.char('Nombre Plantilla', required=True),
	}

	_defaults = {
		'active' : True,
	}


	_sql_constraints = [('name_uniq', 'unique (name)', 'Ya existe una plantilla con este nombre')]


doctor_attentions_radiology_template()