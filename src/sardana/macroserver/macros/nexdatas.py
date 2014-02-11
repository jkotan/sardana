#!/bin/env python
""" NeXus components setting """

import PyTango
import re
import json
import xml.dom.minidom
from sardana.macroserver.macro import Macro, Type



class nxs_components(Macro):
    """ Lists avaliable components """
    def run (self):
        db = PyTango.Database()
        try:
            servers = [self.getEnv("NeXusConfigDevice")]
        except:   
            servers = db.get_device_exported_for_class(
                "NXSConfigServer").value_string 
        if len(servers) > 0:
            nexusconfig_device = PyTango.DeviceProxy(servers[0])
            nexusconfig_device.Open()
            cps = nexusconfig_device.AvailableComponents()  
            mand = nexusconfig_device.MandatoryComponents()
            nomand = list(set(cps)- set(mand))
        
            self.output("Configuration Server: %s" % servers[0])
            self.output("Mandatory Components: %s" % str(mand))
            self.output("Other Components: %s" % str(nomand))



class nxs_datasources(Macro):
    """ Lists avaliable datasources """
    def run (self):
        db = PyTango.Database()
        try:
            servers = [self.getEnv("NeXusConfigDevice")]
        except:   
            servers = db.get_device_exported_for_class(
                "NXSConfigServer").value_string 
        if len(servers) > 0:
            nexusconfig_device = PyTango.DeviceProxy(servers[0])
            nexusconfig_device.Open()
            dss = nexusconfig_device.AvailableDataSources()  
            ds = list(set(dss))

            self.output("Configuration Server: %s" % servers[0])
            self.output("DataSources: %s" % str(ds))



class nxs_component_describe(Macro):
    """ Lists datasources of given component"""

    param_def = [
        ['component', Type.String, '', 'component name']  
        ]

    def run (self, component):
        db = PyTango.Database()
        try:
            servers = [self.getEnv("NeXusConfigDevice")]
        except:   
            servers = db.get_device_exported_for_class(
                "NXSConfigServer").value_string 
        if len(servers) > 0:
            nexusconfig_device = PyTango.DeviceProxy(servers[0])
            nexusconfig_device.Open()
            cps = nexusconfig_device.AvailableComponents()  
            self.output("Configuration Server: %s" % servers[0])

            if component:
                self.output("Component:")
                if component in cps:
                    dss = nexusconfig_device.ComponentDataSources(component)  
                    self.output("%s: %s" % (component, str(dss)))
            else:
                mand = nexusconfig_device.MandatoryComponents()
                nomand = list(set(cps)- set(mand))
        
                self.output("Mandatory Components:")
                for cp in mand:
                    dss = nexusconfig_device.ComponentDataSources(cp)  
                    self.output("%s: %s" % (cp, str(dss)))

                self.output("Other Components:")
                for cp in nomand:
                    dss = nexusconfig_device.ComponentDataSources(cp)  
                    self.output("%s: %s" % (cp, str(dss)))




class nxs_component_xml(Macro):
    """ Shows component xml"""

    param_def = [
        ['component', Type.String, '', 'component name']  
        ]

    def run (self, component):
        db = PyTango.Database()
        try:
            servers = [self.getEnv("NeXusConfigDevice")]
        except:   
            servers = db.get_device_exported_for_class(
                "NXSConfigServer").value_string 
        if len(servers) > 0:
            nexusconfig_device = PyTango.DeviceProxy(servers[0])
            nexusconfig_device.Open()
            cps = nexusconfig_device.AvailableComponents()  

            if component in cps:
                xmls = nexusconfig_device.Components([component])
                self.output("Configuration Server: %s" % servers[0])
                self.output("Component:\n%s" % str(xmls[0]))




class nxs_datasource_xml(Macro):
    """ Shows datasource xml"""

    param_def = [
        ['datasource', Type.String, '', 'datasource name']  
        ]

    def run (self, datasource):
        db = PyTango.Database()
        try:
            servers = [self.getEnv("NeXusConfigDevice")]
        except:   
            servers = db.get_device_exported_for_class(
                "NXSConfigServer").value_string 

        if len(servers) > 0:
            nexusconfig_device = PyTango.DeviceProxy(servers[0])
            nexusconfig_device.Open()
            dss = nexusconfig_device.AvailableDataSources()  

            if datasource in dss:
                xmls = nexusconfig_device.DataSources([datasource])
                self.output("Configuration Server: %s" % servers[0])
                self.output("DataSource:\n%s" % str(xmls[0]))



class nxs_component_describe_full(Macro):
    """ Lists datasources of available components """

    
    param_def = [
        ['component', Type.String, '', 'component name (\'\' for all)'],
        ['strategy', Type.String, '', 'strategy mode (\'\' for all)'],
        ['dstype', Type.String, '', 'datasource type (\'\' for all)'],  
        ['env_components', Type.Boolean, False, 'environment components'],  
        ['silence', Type.Boolean, False, 'silence mode']
        ]

    
    def __checkNode(self, node):
        label = 'datasources'
        dstype = None
        name = None
        if node.nodeName == 'datasource':
            if node.hasAttribute("type"):
                dstype  = node.attributes["type"].value
            if node.hasAttribute("name"):
                name = node.attributes["name"].value
#            self.output("DSNODE: %s, %s", name, dstype)        

        elif node.nodeType == node.TEXT_NODE:
            dstxt = node.data
            index = dstxt.find("$%s." % label)
#            self.output("dstxt:\n  %s"  % (dstxt))
#            self.output("DS0: %s %s"  % (name,index))
            while index != -1 and not dstype:
                try:
                    subc = re.finditer(
                        r"[\w]+", 
                        dstxt[(index+len(label)+2):]).next().group(0)
                except Exception:
#                    self.output("EXC: %s" % str(e))
                    subc = ''
                name = subc.strip() if subc else ""
                try:
                    dsource = self.__nexusconfig_device.DataSources([str(name)])
                except:
                    dsource = []
#                self.output("DS: %s %s"  % (name,str(dsource)))
                if len(dsource)>0:
                    indom = xml.dom.minidom.parseString(dsource[0])
                    dss = indom.getElementsByTagName("datasource")
                    for ds in dss:
                        if ds.nodeName == 'datasource':
                            if ds.hasAttribute("type"):
                                dstype  = ds.attributes["type"].value
                            if ds.hasAttribute("name"):
                                name = ds.attributes["name"].value
                index = dstxt.find("$%s." % label, index+1)
#                self.output("DSTXT: %s, %s", name, dstype)        
        return name, dstype
                

    def __appendNode(self, node, dss, mode, counter): 
        prefix = '__unnamed__'
        name, dstype = self.__checkNode(node)
        if name:
            if name not in dss:
                dss[name] = [] 
        else:
            name = prefix + str(counter) 
            while name in dss.keys():
                name = prefix + str(counter) 
                counter = counter + 1
            dss[name] = [] 
        dss[name].append((str(mode), str(dstype) if dstype else None))
        
        counter = counter +1
        return (name, counter)

    def __getDataSourceAttributes(self, cp):         
        dss = {}
        xmlc = self.__nexusconfig_device.Components([cp])
        names = []
        if not len(xmlc)>0:
            return names
        indom = xml.dom.minidom.parseString(xmlc[0])
        strategy = indom.getElementsByTagName("strategy")
        counter = 1

        for sg in strategy:
            if sg.hasAttribute("mode"):
                mode = sg.attributes["mode"].value
                name = None
                nxt = sg.nextSibling
                while nxt and not name:
                    name, counter = self.__appendNode(nxt, dss, mode, counter)
                    nxt = nxt.nextSibling    

                prev = sg.previousSibling
                while prev and not name:
                    name, counter = self.__appendNode(prev, dss, mode, counter)
                    prev = prev.previousSibling  
        return dss



    def run(self, component, strategy, dstype, env_components, silence):
        self.__result = [{}, {}]
        db = PyTango.Database()
        try:
            servers = [self.getEnv("NeXusConfigDevice")]
        except:   
            servers = db.get_device_exported_for_class(
                "NXSConfigServer").value_string 
        if len(servers) > 0:
            self.__nexusconfig_device = PyTango.DeviceProxy(servers[0])
            self.__nexusconfig_device.Open()
            if env_components:
                cps = self.getEnv("NeXusComponents")
            elif component:
                cpp = self.__nexusconfig_device.AvailableComponents()  
                cps = [component] if component in cpp else []
               
            else:
                cps = self.__nexusconfig_device.AvailableComponents()  
            if not component:
                mand = self.__nexusconfig_device.MandatoryComponents()
                cps = list(set(cps)- set(mand))

            if not silence:
                self.output("Configuration Server: %s" % servers[0])

            if not component:
                if not silence:
                    self.output("\nMandatory Components: %s" %  mand)
                for cp in mand:
                    dss = self.__getDataSourceAttributes(cp)  
                    tr = {}
                    for ds in dss.keys():
                        for vds in dss[ds]:
                            if (not strategy or vds[0] == strategy) and \
                                    (not dstype or vds[1] == dstype):
                                if ds not in tr:
                                    tr[ds] = []
                                tr[ds].append(vds)
                    if not silence:
                        self.output("%s: %s" % (cp, str(tr)))
                    self.__result[0][cp] = tr

            if not silence and not component:
                self.output("\nOther Components: %s" % (str(cps)))
            for cp in cps:
                dss = self.__getDataSourceAttributes(cp)  
                tr = {}
                for ds in dss.keys():
                    for vds in dss[ds]:
                        if (not strategy or vds[0] == strategy) and \
                                (not dstype or vds[1] == dstype):
                            if ds not in tr:
                                tr[ds] = []
                            tr[ds].append(vds)
                if not silence:
                    self.output("%s: %s" % (cp, str(tr)))
                self.__result[1][cp] = tr
     
    @property
    def data(self):
        return self.__result



class nxs_set_mntgrp_from_components(Macro):
    """Macro nxs_set_mntgrp_from_components"""
    

    param_def = [
        ['timer', Type.String, '', 'master timer'],
        ['flagClear', Type.Boolean, False, 'clear measurement group']
        ]

    def prepare(self, timer, flagClear):
        ## tango database
        self.__db = PyTango.Database()
        ## pools
        self.__pools = []
        ## configuration
        self.__hsh = {}
        self.__hsh['controllers'] = {} 
        self.__hsh['description'] = "Measurement Group" 
        self.__hsh['label'] = "" 
        self.__masterTimer = 'exp_t01'

    def __getDeviceNamesByClass(self, className):
        srvs = self.__getServerNameByClass(className)
        argout = []
        for srv in srvs:
            lst = self.__db.get_device_name( srv, className).value_string
            for i in range(0, len( lst)):
                argout.append( lst[i])
        return argout


    def __getServerNameByClass(self,  argin): 
        srvs = self.__db.get_server_list( "*").value_string
        argout = []
        for srv in srvs:
            classList = self.__db.get_server_class_list( srv).value_string
            for clss in classList:
                if clss == argin:
                    argout.append(srv)
                    break
        return argout


    def __setpools(self):
        poolNames = self.__getDeviceNamesByClass( "Pool")
        self.__pools = []
        for pool in poolNames:
            dp = PyTango.DeviceProxy(pool)
            try:
                dp.ping()
                self.__pools.append(dp)    
                self.output("APOOL: %s" % pool)
            except:
                pass

    def run (self, timer, flagClear):
        aliases = []
        self.__setpools()
        res = self.nxs_describe_components_full('',
            'STEP', 'CLIENT', True, True).data
        for grp in res:
            for dss in grp.values():
                for ds in dss.keys():
                    aliases.append(str(ds))
        self.output("devices:\n %s" % (str(aliases)))

        mntGrpName = self.getEnv('ActiveMntGrp')
        self.__mg = self.getObj(mntGrpName, type_class=Type.MeasurementGroup)
        cfg = self.__mg.Configuration
        self.output("CONF:\n%s" % str(cfg))
        if flagClear:
            self.__hsh['label'] = mntGrpName
            self.index = len(self.__mg.ElementList)
        else:
            self.__hsh = json.loads(self.__mg.Configuration)
            self.index = 0
        if timer:
            self.__masterTimer = timer
        elif not flagClear:
            self.__masterTimer = self.__db.get_alias(str(
                    "/".join((self.__hsh['timer'].split("/"))[1:])))
        self.output("TIMER: %s" % self.__masterTimer)    
        self.__hsh[ u'monitor'] = self.__findFullDeviceName(self.__masterTimer)
        self.__hsh[ u'timer'] = self.__findFullDeviceName(self.__masterTimer)
            
            
        pool = self.__mg.getPoolObj()
        self.output("POOL:\n%s" % str(pool))
        ctrls = pool.read_attribute("ControllerList").value
        self.output("CTRLS:\n%s" % str(ctrls))

        for alias in aliases:
            self.__addDevice(alias)
        self.output("RESULT:\n%s" % str(self.__hsh))
            
#        self.__updateConfiguration()

        
    def __findDeviceController( self, device):
        """
        returns the controller that belongs to a device
        """
        lst = []
        for pool in self.__pools:
            if not pool.ExpChannelList is None:
                lst += pool.ExpChannelList
        ctrl = None
        for elm in lst:
            chan = json.loads( elm)
            if device == chan['name']:
                ctrl = chan['controller']
                break
#        if ctrl is None and device.find("adc") >= 0:
#            ctrl = os.getenv("TANGO_HOST") + "/" 
# + "controller/hasylabadcctrl/hasyadcctrl"
#        elif ctrl is None and device.find("vfc") >= 0:
#            ctrl = os.getenv("TANGO_HOST") + "/" 
# + "controller/vfcadccontroller/hasyvfcadcctrl"
        return ctrl


    def __findFullDeviceName( self, device):
        """
          input: exp_c01
          returns: expchan/hasylabvirtualcounterctrl/1
        """
        lst = []
        for pool in self.__pools:
            lst += pool.AcqChannelList
        argout = None
        for elm in lst:
            chan = json.loads( elm)
            if device == chan['name']:
                #
                # from: expchan/hasysis3820ctrl/1/value
                # to:   expchan/hasysis3820ctrl/1
                #
                arr = chan['full_name'].split("/")
                argout = "/".join(arr[0:-1])
        return argout


    def __updateConfiguration( self):
        """
        json-dump the dictionary self.__hsh to the Mg configuration
        """
        self.__mg.Configuration = json.dumps( self.__hsh)

    def __addDevice( self, device):
        ctrl = self.__findDeviceController( device)
        if not ctrl:
            return
        if not self.__hsh[ u'controllers'].has_key( ctrl):
#            self.masterTimer = device
#            self.__hsh[ u'monitor'] = self.__findFullDeviceName( device)
#            self.__hsh[ u'timer'] = self.__findFullDeviceName( device)
            self.__hsh[ u'controllers'][ ctrl] = {}
            self.__hsh[ u'controllers'][ ctrl][ u'units'] = {}
            self.__hsh[ u'controllers'][ ctrl][ u'units'][u'0'] = {}
            self.__hsh[ u'controllers'][ ctrl][ u'units'][u'0'][
                u'channels'] = {}
            self.__hsh[ u'controllers'][ ctrl][ u'units'][u'0'][ u'id'] = 0
            self.__hsh[ u'controllers'][ ctrl][ u'units'][u'0'][
                u'monitor'] = self.__findFullDeviceName(self.__masterTimer)
            self.__hsh[ u'controllers'][ ctrl][ u'units'][u'0'][ 
                u'timer'] = self.__findFullDeviceName(self.__masterTimer)
            self.__hsh[ u'controllers'][ ctrl][ u'units'][u'0'][ 
                u'trigger_type'] = 0

        ctrlChannels = self.__hsh[ u'controllers'][ctrl][ u'units'][ u'0'][
            u'channels']
        
        if not self.__findFullDeviceName( device) in ctrlChannels.keys():
            self.output("adding index %s %s" % (self.index, device))
            dct = {}
            dct[ u'_controller_name'] = unicode(ctrl)
            dct[ u'_unit_id'] = u'0'
            dct[ u'conditioning'] = u''
            dct[ u'data_type'] = u'float64'
            dct[ u'data_units'] = u'No unit'
            dct[ u'enabled'] = True
            dct[ u'full_name'] = self.__findFullDeviceName( device)
            dct[ u'index'] = self.index
            self.index += 1
            dct[ u'instrument'] = None
            dct[ u'label'] = unicode(device)
            dct[ u'name'] = unicode(device)
            dct[ u'ndim'] = 0
            dct[u'nexus_path'] = u''
            dct[ u'normalization'] = 0
            dct[ u'output'] = True
            dct[ u'plot_axes'] = []
            dct[ u'plot_type'] = 0
            dct[ u'shape'] = []
            dct[ u'source'] = dct['full_name'] + "/value"
            ctrlChannels[self.__findFullDeviceName( device)] = dct
            






