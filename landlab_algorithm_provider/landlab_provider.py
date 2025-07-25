# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Landlab Algorithm Provider
                                 A QGIS plugin
 Earth Surface Dynamics modeling algorithms
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2025-07-25
        copyright            : (C) 2025 by Lucas Amion
        email                : lamion@dcc.uchile.cl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Lucas Amion'
__date__ = '2025-07-25'
__copyright__ = '(C) 2025 by Lucas Amion'


from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsProcessingProvider
from .algorithms.stream_power_eroder import StreamPowerEroder
from . import resources # noqa: F401 Import resources to ensure icons are available


class LandlabProvider(QgsProcessingProvider):

  def loadAlgorithms(self, *args, **kwargs):
    self.addAlgorithm(StreamPowerEroder())

  def id(self, *args, **kwargs):
    """The ID of your plugin, used for identifying the provider.

    This string should be a unique, short, character only string,
    something like "qgis" or "gdal". This string should not be
    localised.
    """
    return 'landlab_algorithm_provider'

  def name(self, *args, **kwargs):
    """The human friendly name of your plugin in Processing.

    This string should be as short as possible (e.g. "Lastools", not
    "Lastools version 1.0.1 64-bit") and localised.
    """
    return self.tr('Landlab Algorithm Provider')

  def icon(self):
    """Should return a QIcon which is used for your provider inside
    the Processing toolbox.
    """
    return QIcon(":/plugins/landlab_algorithm_provider/img/icon.png")

  def longName(self):
    """
    Returns the a longer version of the provider name, which can include
    extra details such as version numbers. E.g. "Lastools LIDAR tools
    (version 2.2.1)". This string should be localised. The default
    implementation returns the same string as name().
    """
    return self.name()
