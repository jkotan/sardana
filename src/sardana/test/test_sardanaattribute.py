#!/usr/bin/env python

##############################################################################
##
# This file is part of Sardana
##
# http://www.sardana-controls.org/
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Sardana is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Sardana is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Sardana.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

from mock import MagicMock

from taurus.external.unittest import TestCase

from sardana.sardanaattribute import Buffer, BufferedAttribute
from sardana.pool.poolpseudocounter import Value


class TestBuffer(TestCase):
    """Unit tests for Buffer class"""

    def setUp(self):
        self.buffer = Buffer([1, 2, 3])

    def test_extend(self):
        """Test extend method with a simple case of a list."""
        chunk = [4, 5, 6]
        self.buffer.extend(chunk)
        self.assertEqual(self.buffer[0], 1)
        self.assertEqual(self.buffer[5], 6)


class TestBufferedAttribute(TestCase):
    """Unit tests for BufferedAttribute class"""

    def setUp(self):
        self.attr = BufferedAttribute(MagicMock())

    def test_buffered_attribute_listeners(self):
        """Test if calling add_listener and remove_listener is consistent
        with the buffered_attribute_listener property.

        Use pseudocounter's Value attribute, which is a buffered attribute,
        as a dummy listener.
        """
        pc1_value = Value(MagicMock())
        pc2_value = Value(MagicMock())
        self.attr.add_listener(pc1_value.on_change)
        self.assertEqual(len(self.attr.buffered_attribute_listeners), 1)
        self.attr.add_listener(pc2_value.on_change)
        self.assertEqual(len(self.attr.buffered_attribute_listeners), 2)
        self.attr.remove_listener(pc1_value.on_change)
        self.assertEqual(len(self.attr.buffered_attribute_listeners), 1)
        self.attr.remove_listener(pc2_value.on_change)
        self.assertEqual(len(self.attr.buffered_attribute_listeners), 0)

    def test_append_value_buffer(self):
        """Test if append_value_buffer correctly fills the last_value_chunk
        as well as permanently adds the value to the value_buffer (a buffered
        attribute listener was added previously in order to provoke a
        persistent append).
        """
        pc_value = Value(MagicMock())
        self.attr.add_listener(pc_value.on_change)
        self.attr.append_value_buffer(1)
        self.assertIs(len(self.attr.value_buffer), 1)
        self.assertIs(len(self.attr.last_value_chunk), 1)

    def test_extend_value_buffer(self):
        """Test if extend_value_buffer correctly fills the last_value_chunk
        as well as permanently adds the value to the value_buffer (a buffered
        attribute listener was added previously in order to provoke a
        persistent append).
        """
        pc_value = Value(MagicMock())
        self.attr.add_listener(pc_value.on_change)
        self.attr.extend_value_buffer([1, 2, 3])
        self.assertIs(len(self.attr.value_buffer), 3)
        self.assertIs(len(self.attr.last_value_chunk), 3)

    def test_extend_value_buffer_no_buffered_attribute_listener(self):
        """Test if extend_value_buffer correctly fills the last_value_chunk
        but does not add the value to the value_buffer (a non-buffered
        attribute listener was added previously so a non-persistent append
        should take place).
        """
        def listener(*args):
            return

        self.attr.add_listener(listener)
        self.attr.extend_value_buffer([1, 2, 3])
        self.assertIs(len(self.attr.last_value_chunk), 3)
        self.assertIs(len(self.attr.value_buffer), 0)

    def test_is_value_necessary(self):
        """Test if is_value_required is able to recognize that there is no
        listener waiting for a given value.
        """
        pc_value = Value(MagicMock())
        self.attr.add_listener(pc_value.on_change)
        # imitate that the listener already has a 0th element
        pc_value.value_buffer._next_idx = 1
        self.assertFalse(self.attr.is_value_required(0))
