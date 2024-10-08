#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2016 <microelly2@freecadbuch.de>                        *
#*   Copyright (c) 2024 Julien Masnada <rostskadat@gmail.com>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

__title__="FreeCAD GeoData2 Toolkit"
__author__ = "Thomas Gundermann & al"
__url__ = "http://www.freecadbuch.de"
__vers__ ="py3.01"

import FreeCAD as App

try:
    import cv2
except:
    App.Console.PrintWarning("GeoData2 WB: Cannot import module named cv2. Some import might not be available.\n")

try:
    import gdal
    import gdalconst
except:
    App.Console.PrintWarning("GeoData2 WB: Cannot import module named gdal gdalconst. Some import might not be available.\n")

App.addImportType("OSM format (*.osm)","importOSM")
App.addExportType("CSV format (*.csv *.tsv)","importCSV")
