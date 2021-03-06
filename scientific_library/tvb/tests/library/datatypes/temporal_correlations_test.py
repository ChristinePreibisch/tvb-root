# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2020, Baycrest Centre for Geriatric Care ("Baycrest") and others
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#
"""
Created on Mar 20, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa@codemart.ro>
"""

import numpy
from tvb.tests.library.base_testcase import BaseTestCase
from tvb.datatypes import temporal_correlations, time_series


class TestTemporalCorrelations(BaseTestCase):
    """
    Tests the defaults for `tvb.datatypes.temporal_correlations` module.
    """

    def test_crosscorrelation(self):
        data = numpy.random.random((10, 10))
        ts = time_series.TimeSeries(data=data, title='meh')
        dt = temporal_correlations.CrossCorrelation(source=ts, array_data=numpy.array([0]))
        summary_info = dt.summary_info()
        assert summary_info['Dimensions'] == ('Offsets', 'Node', 'Node', 'State Variable', 'Mode')
        assert summary_info['Source'] == 'meh'
        assert summary_info['Temporal correlation type'] == 'CrossCorrelation'
        assert dt.labels_ordering == ('Offsets', 'Node', 'Node', 'State Variable', 'Mode')
        assert dt.source is not None
        assert dt.time is None
