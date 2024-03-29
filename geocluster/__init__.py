# -*- coding: utf-8 -*-
"""
/***************************************************************************
 geocluster
                                 A QGIS plugin
 geocluster
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-03-05
        copyright            : (C) 2024 by Federico Falasca
        email                : federico.falasca@graduate.univaq.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Federico Falasca'
__date__ = '2024-03-05'
__copyright__ = '(C) 2024 by Federico Falasca'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load UrbanShapes class from file UrbanShapes.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geocluster import OpenManualPlugin
    return OpenManualPlugin()
    from .geocluster import GridPlugin
    return GridPlugin()
    from .geocluster import JoinPlugin
    return JoinPlugin()
    from .geocluster import Feature_extractionPlugin
    return Feature_extractionPlugin()
