# coding: utf-8

# Copyright 2014-2015 Álvaro Justen <https://github.com/turicas/rows/>
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

from __future__ import unicode_literals

import unicodecsv

import rows.utils


def import_from_csv(filename_or_fobj, delimiter=',', quotechar='"',
                    *args, **kwargs):
    'Import data from a CSV file'

    fobj = rows.utils.fobj_from_filename_or_fobj(filename_or_fobj)
    encoding = kwargs.get('encoding', 'utf-8')
    csv_reader = unicodecsv.reader(fobj, encoding=encoding,
                                   delimiter=str(delimiter),
                                   quotechar=str(quotechar))

    return rows.utils.create_table(csv_reader, *args, **kwargs)


def export_to_csv(table, filename_or_fobj, encoding='utf-8'):
    # TODO: will work only if table.fields is OrderedDict

    fobj = rows.utils.fobj_from_filename_or_fobj(filename_or_fobj, mode='w')
    csv_writer = unicodecsv.writer(fobj, encoding=encoding)

    csv_writer.writerow(table.fields.keys())
    for row in table.serialize(encoding=encoding):
        csv_writer.writerow(row)

    fobj.close()
