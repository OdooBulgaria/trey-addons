# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2016-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
{
    'name': 'My Account Contract',
    'category': 'Website',
    'summary': (
        'Add your contract documents in the frontend portal (contracts'
        ', issues, tasks)'
    ),
    'description': '''
    ''',
    'author': 'Trey (www.trey.es)',
    'website': 'https://www.trey.es',
    'version': '8.0.1.0.0',
    'depends': [
        'account',
        'account_analytic_analysis',
        'analytic_user_function',
        'base',
        'hr_timesheet_invoice',
        'sale',
        'portal',
        'product',
        'project',
        'website_myaccount',
        'website',
        'mail'],
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        'templates/website.xml',
        'templates/website_myaccount.xml',
        'templates/website_myaccount_contract.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
}
