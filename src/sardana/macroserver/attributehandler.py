#!/usr/bin/env python

##############################################################################
##
## This file is part of Sardana
##
## http://www.tango-controls.org/static/sardana/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Sardana is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Sardana is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Sardana.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

"""This is the main macro server module"""

__all__ = ["AttributeLogHandler", "AttributeBufferedLogHandler"]

__docformat__ = 'restructuredtext'

import logging
import threading
import weakref
import operator
import types

from taurus.core.util import LIFO


class AttributeLogHandler(logging.Handler):
    
    def __init__(self, dev, attr_name, level=logging.NOTSET, max_buff_size=0):
        logging.Handler.__init__(self, level)
        self._attr_name = attr_name
        self._level = level
        self._max_buff_size = max_buff_size
        self._dev = weakref.ref(dev)
        
        dev.set_change_event(attr_name, True, False)
        attr_list = dev.get_device_attr()
        attr = attr_list.get_attr_by_name(attr_name)
        attr.set_value([])

        self._buff = LIFO(max_buff_size)

    def emit(self, record):
        output = self.getRecordMessage(record)
        self.appendBuffer(output)
        self.sendText(output)

    def getRecordMessage(self, record):
        return record.getMessage().split('\n')
    
    def sendText(self, output):
        self._dev().push_change_event(self._attr_name, output)
            
    def read(self, attr):
        """Read from the buffer and assign to the attribute value"""
        attr.set_value(self._buff.getCopy())
    
    def clearBuffer(self):
        self._buff.clear()
        
    def appendBuffer(self, d):
        if operator.isSequenceType(d):
            if type(d) in types.StringTypes:
                self._buff.append(d)
            else:
                self._buff.extend(d)
        else:
            self._buff.append(str(d))
    
    def sync(self):
        pass
    
    def finish(self):
        pass
    
AttributeBufferedLogHandler = AttributeLogHandler