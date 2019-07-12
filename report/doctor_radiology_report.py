# -*- coding: utf-8 -*-
# #############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
###############################################################################

import time
from openerp.report import report_sxw
from openerp import pooler
import logging
_logger = logging.getLogger(__name__)


class doctor_radiology_report(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(doctor_radiology_report, self).__init__(cr, uid, name, context=context)
		self.localcontext.update({
			'time': time,
			'select_escolaridad': self.select_escolaridad
		})

	def select_escolaridad(self, patient_educational_level):
		tipo = ''
		if patient_educational_level == '1':
			tipo='Pregrado'
		elif patient_educational_level == 2:
			tipo='Postgrado'
		elif patient_educational_level == 3:
			tipo='Maestrías'
		elif patient_educational_level == 4:
			tipo='Especialización'
		elif patient_educational_level == 5:
			tipo='Jardín'
		elif patient_educational_level == 6:
			tipo='Primaria'
		return tipo


report_sxw.report_sxw('report.doctor.attentions.radiology.report','doctor.attentions.radiology','addons/doctor_radiology/report/doctor_radiology_report.rml', parser=doctor_radiology_report)
