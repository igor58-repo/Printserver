# coding: utf-8
# This file is part of the Printrun suite.
#
# Printrun is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Printrun is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Printrun.  If not, see <http://www.gnu.org/licenses/>.

try:
    import wx
except:
    print _("WX is not installed. This program requires WX to run.")
    raise

global buttonSize
buttonSize = (90, 40)  # Define sizes for the buttons on top rows

from printrun import gviz
from printrun.xybuttons import XYButtons
from printrun.zbuttons import ZButtons
from printrun.graph import Graph
from printrun_utils import imagefile

def make_button(parent, label, callback, tooltip, container = None, size = wx.DefaultSize, style = 0):
    button = wx.Button(parent, -1, label, style = style, size = size)
    button.Bind(wx.EVT_BUTTON, callback)
    button.SetToolTip(wx.ToolTip(tooltip))
    if container:
        container.Add(button)
    return button

def make_sized_button(*args):
    return make_button(*args, size = buttonSize)

def make_autosize_button(*args):
    return make_button(*args, size = (-1, buttonSize[1]), style = wx.BU_EXACTFIT)

class KeyboardSizer(wx.GridBagSizer):
    def __init__(self, root):
	super(KeyboardSizer, self).__init__()
	self.parent = root
	self.Abtn = self.make_button("A")
	self.Add(self.Abtn, pos=(0,0))
	self.Bbtn = self.make_button("B")
	self.Add(self.Bbtn, pos=(0,1))
	self.Cbtn = self.make_button("C")
	self.Add(self.Cbtn, pos=(0,2))
	self.Dbtn = self.make_button("D")
	self.Add(self.Dbtn, pos=(0,3))
	self.Ebtn = self.make_button("E")
	self.Add(self.Ebtn, pos=(0,4))
	self.Fbtn = self.make_button("F")
	self.Add(self.Fbtn, pos=(0,5))
	self.Gbtn = self.make_button("G")
	self.Add(self.Gbtn, pos=(0,6))
	self.Gbtn.SetBackgroundColour('#AAFFAA');
	self.Hbtn = self.make_button("H")
	self.Add(self.Hbtn, pos=(0,7))
	self.Ibtn = self.make_button("I")
	self.Add(self.Ibtn, pos=(0,8))
	self.Jbtn = self.make_button("J")
	self.Add(self.Jbtn, pos=(0,9))
	self.Kbtn = self.make_button("K")
	self.Add(self.Kbtn, pos=(1,0))
	self.Lbtn = self.make_button("L")
	self.Add(self.Lbtn, pos=(1,1))
	self.Mbtn = self.make_button("M")
	self.Add(self.Mbtn, pos=(1,2))
	self.Mbtn.SetBackgroundColour('#AAFFAA');
	self.Nbtn = self.make_button("N")
	self.Add(self.Nbtn, pos=(1,3))
	self.Obtn = self.make_button("O")
	self.Add(self.Obtn, pos=(1,4))
	self.Pbtn = self.make_button("P")
	self.Add(self.Pbtn, pos=(1,5))
	self.Qbtn = self.make_button("Q")
	self.Add(self.Qbtn, pos=(1,6))
	self.Rbtn = self.make_button("R")
	self.Add(self.Rbtn, pos=(1,7))
	self.Sbtn = self.make_button("S")
	self.Add(self.Sbtn, pos=(1,8))
	self.Tbtn = self.make_button("T")
	self.Add(self.Tbtn, pos=(1,9))
	self.Ubtn = self.make_button("U")
	self.Add(self.Ubtn, pos=(2,0))
	self.Vbtn = self.make_button("V")
	self.Add(self.Vbtn, pos=(2,1))
	self.Wbtn = self.make_button("W")
	self.Add(self.Wbtn, pos=(2,2))
	self.Xbtn = self.make_button("X")
	self.Add(self.Xbtn, pos=(2,3))
	self.Ybtn = self.make_button("Y")
	self.Add(self.Ybtn, pos=(2,4))
	self.Zbtn = self.make_button("Z")
	self.Add(self.Zbtn, pos=(2,5))
	self.Backbtn = self.make_button("<-")
	self.Add(self.Backbtn, pos=(2,6))
	self.Clrbtn = self.make_button("CLR")
	self.Clrbtn.SetBackgroundColour('#FFAAAA')
	self.Add(self.Clrbtn, pos=(2,7))
	self.Spacebtn = self.make_button(" ")
	self.Add(self.Spacebtn, pos=(2,8))
	self.Dotbtn = self.make_button(".")
	self.Add(self.Dotbtn, pos=(2,9))
	self.N0btn = self.make_button("0")
	self.Add(self.N0btn, pos=(3,0))
	self.N1btn = self.make_button("1")
	self.Add(self.N1btn, pos=(3,1))
	self.N2btn = self.make_button("2")
	self.Add(self.N2btn, pos=(3,2))
	self.N3btn = self.make_button("3")
	self.Add(self.N3btn, pos=(3,3))
	self.N4btn = self.make_button("4")
	self.Add(self.N4btn, pos=(3,4))
	self.N5btn = self.make_button("5")
	self.Add(self.N5btn, pos=(3,5))
	self.N6btn = self.make_button("6")
	self.Add(self.N6btn, pos=(3,6))
	self.N7btn = self.make_button("7")
	self.Add(self.N7btn, pos=(3,7))
	self.N8btn = self.make_button("8")
	self.Add(self.N8btn, pos=(3,8))
	self.N9btn = self.make_button("9")
	self.Add(self.N9btn, pos=(3,9))
	
    def make_button(self, label):
	button = wx.Button(self.parent.panel, -1, label, style=0, size = (36,36))
	button.Bind(wx.EVT_BUTTON, self.btn_press)
	return button
	
    def btn_press(self, event):
	button = event.GetEventObject()
        lbl = button.GetLabel()
        if lbl == "<-":
	    str = self.parent.commandbox.GetValue()
	    self.parent.commandbox.SetValue(str[:-1]) # remove last character
	    return
	if lbl == "CLR":
	    self.parent.commandbox.SetValue("")
	    return
        self.parent.commandbox.AppendText(lbl);
    
class XYZControlsSizer(wx.GridBagSizer):

    def __init__(self, root):
        super(XYZControlsSizer, self).__init__()
        self.root = root;
        root.xyb = XYButtons(root.panel, root.moveXY, root.homeButtonClicked, root.spacebarAction, root.settings.bgcolor)
        root.zb = ZButtons(root.panel, root.moveZ, root.settings.bgcolor)
        imageStop = wx.Image(imagefile('stop_btn.png'), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        root.stopBtn = wx.BitmapButton(root.panel, -1, bitmap=imageStop, size = (248,248), style = wx.BU_EXACTFIT)
        root.stopBtn.Bind(wx.EVT_BUTTON, root.do_reset)
        root.stopBtn.SetToolTip(wx.ToolTip("Stop!"))
        #root.stopBtn.Hide()
        self.addStop()
        self.addxyz()
        wx.CallAfter(root.xyb.SetFocus)
        
    def addxyz(self):
        self.Clear()
        self.root.stopBtn.Hide()
        self.root.xyb.Show()
        self.root.zb.Show()
        self.Add(self.root.xyb, pos = (0, 1), flag = wx.ALIGN_CENTER)
        self.Add(self.root.zb, pos = (0, 2), flag = wx.ALIGN_CENTER)
        self.Layout()
        
    def addStop(self):
        self.Clear()
        self.root.xyb.Hide()
        self.root.zb.Hide()
        self.root.stopBtn.Show()
        self.Add(self.root.stopBtn, pos = (0, 1), flag = wx.ALIGN_CENTER)
        self.Layout()
        

class LeftPane(wx.GridBagSizer):

    def __init__(self, root):
        super(LeftPane, self).__init__()
        llts = wx.BoxSizer(wx.HORIZONTAL)
        self.Add(llts, pos = (0, 0), span = (1, 9))
        self.xyzsizer = XYZControlsSizer(root)
        root.xyzsizer = self.xyzsizer
        self.Add(self.xyzsizer, pos = (1, 0), span = (1, 8), flag = wx.ALIGN_CENTER)
        
        for i in root.cpbuttons:
            btn = make_button(root.panel, i.label, root.procbutton, i.tooltip, size = (-1,35), style = wx.BU_EXACTFIT)
            btn.SetBackgroundColour(i.background)
            btn.SetForegroundColour("black")
            btn.properties = i
            root.btndict[i.command] = btn
            root.printerControls.append(btn)
            if i.pos == None:
                if i.span == 0:
                    llts.Add(btn)
            else:
                self.Add(btn, pos = i.pos, span = i.span)

        root.xyfeedc = wx.SpinCtrl(root.panel,-1, str(root.settings.xy_feedrate), min = 0, max = 50000, size = (70,35))
        root.xyfeedc.SetToolTip(wx.ToolTip("Set Maximum Speed for X & Y axes (mm/min)"))
        llts.Add(wx.StaticText(root.panel,-1, _("XY:")), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        llts.Add(root.xyfeedc)
        llts.Add(wx.StaticText(root.panel,-1, _("mm/min   Z:")), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        root.zfeedc = wx.SpinCtrl(root.panel,-1, str(root.settings.z_feedrate), min = 0, max = 50000, size = (70,35))
        root.zfeedc.SetToolTip(wx.ToolTip("Set Maximum Speed for Z axis (mm/min)"))
        llts.Add(root.zfeedc,)

        #root.monitorbox = wx.CheckBox(root.panel,-1, _("Watch"))
        #root.monitorbox.SetToolTip(wx.ToolTip("Monitor Temperatures in Graph"))
        #self.Add(root.monitorbox, pos = (2, 6))
        #root.monitorbox.Bind(wx.EVT_CHECKBOX, root.setmonitor)
        
        self.Add(wx.StaticText(root.panel,-1, _("Хотэнд:")), pos = (2, 0), span = (1, 1), flag = wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT)
        htemp_choices = [root.temps[i]+" ("+i+")" for i in sorted(root.temps.keys(), key = lambda x:root.temps[x])]

        root.settoff = make_button(root.panel, _("Выкл"), lambda e: root.do_settemp("off"), _("Отключить хотэнд"), size = (50,40), style = wx.BU_EXACTFIT)
        root.printerControls.append(root.settoff)
        self.Add(root.settoff, pos = (2, 1), span = (1, 1))

        if root.settings.last_temperature not in map(float, root.temps.values()):
            htemp_choices = [str(root.settings.last_temperature)] + htemp_choices
        root.htemp = wx.ComboBox(root.panel, -1,
                choices = htemp_choices, style = wx.CB_DROPDOWN, size = (70,-1))
        root.htemp.SetToolTip(wx.ToolTip("Select Temperature for Hotend"))
        root.htemp.Bind(wx.EVT_COMBOBOX, root.htemp_change)

        self.Add(root.htemp, pos = (2, 2), span = (1, 2))
        root.settbtn = make_button(root.panel, _("Set"), root.do_settemp, _("Switch Hotend On"), size = (45, 40), style = wx.BU_EXACTFIT)
        root.printerControls.append(root.settbtn)
        self.Add(root.settbtn, pos = (2, 4), span = (1, 1))

        self.Add(wx.StaticText(root.panel,-1, _("Стол:")), pos = (3, 0), span = (1, 1), flag = wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT)
        btemp_choices = [root.bedtemps[i]+" ("+i+")" for i in sorted(root.bedtemps.keys(), key = lambda x:root.temps[x])]

        root.setboff = make_button(root.panel, _("Выкл"), lambda e:root.do_bedtemp("off"), _("Выключить подогрев стола"), size = (50,40), style = wx.BU_EXACTFIT)
        root.printerControls.append(root.setboff)
        self.Add(root.setboff, pos = (3, 1), span = (1, 1))

        if root.settings.last_bed_temperature not in map(float, root.bedtemps.values()):
            btemp_choices = [str(root.settings.last_bed_temperature)] + btemp_choices
        root.btemp = wx.ComboBox(root.panel, -1,
                choices = btemp_choices, style = wx.CB_DROPDOWN, size = (70,-1))
        root.btemp.SetToolTip(wx.ToolTip("Select Temperature for Heated Bed"))
        root.btemp.Bind(wx.EVT_COMBOBOX, root.btemp_change)
        self.Add(root.btemp, pos = (3, 2), span = (1, 2))

        root.setbbtn = make_button(root.panel, _("Set"), root.do_bedtemp, ("Switch Heated Bed On"), size = (45, 40), style = wx.BU_EXACTFIT)
        root.printerControls.append(root.setbbtn)
        self.Add(root.setbbtn, pos = (3, 4), span = (1, 1))

        root.btemp.SetValue(str(root.settings.last_bed_temperature))
        root.htemp.SetValue(str(root.settings.last_temperature))

        ## added for an error where only the bed would get (pla) or (abs).
        #This ensures, if last temp is a default pla or abs, it will be marked so.
        # if it is not, then a (user) remark is added. This denotes a manual entry

        for i in btemp_choices:
            if i.split()[0] == str(root.settings.last_bed_temperature).split('.')[0] or i.split()[0] == str(root.settings.last_bed_temperature):
                root.btemp.SetValue(i)
        for i in htemp_choices:
            if i.split()[0] == str(root.settings.last_temperature).split('.')[0] or i.split()[0] == str(root.settings.last_temperature) :
                root.htemp.SetValue(i)

        if( '(' not in root.btemp.Value):
            root.btemp.SetValue(root.btemp.Value + ' (user)')
        if( '(' not in root.htemp.Value):
            root.htemp.SetValue(root.htemp.Value + ' (user)')

        root.edist = wx.SpinCtrl(root.panel,-1, "5", min = 0, max = 1000, size = (80,40))
        root.edist.SetBackgroundColour((225, 200, 200))
        root.edist.SetForegroundColour("black")
        self.Add(root.edist, pos = (4, 2), span = (1, 2))
        self.Add(wx.StaticText(root.panel,-1, _("mm")), pos = (4, 4), span = (1, 1))
        root.edist.SetToolTip(wx.ToolTip("Amount to Extrude or Retract (mm)"))
        root.efeedc = wx.SpinCtrl(root.panel,-1, str(root.settings.e_feedrate), min = 0, max = 50000, size = (80,40))
        root.efeedc.SetToolTip(wx.ToolTip("Extrude / Retract speed (mm/min)"))
        root.efeedc.SetBackgroundColour((225, 200, 200))
        root.efeedc.SetForegroundColour("black")
        root.efeedc.Bind(wx.EVT_SPINCTRL, root.setfeeds)
        self.Add(root.efeedc, pos = (5, 2), span = (1, 2))
        self.Add(wx.StaticText(root.panel,-1, _("mm/\nmin")), pos = (5, 4), span = (1, 1))
        root.xyfeedc.Bind(wx.EVT_SPINCTRL, root.setfeeds)
        root.zfeedc.Bind(wx.EVT_SPINCTRL, root.setfeeds)
        root.zfeedc.SetBackgroundColour((180, 255, 180))
        root.zfeedc.SetForegroundColour("black")

class VizPane(wx.BoxSizer):

    def __init__(self, root):
        super(VizPane, self).__init__(wx.VERTICAL)
        root.gviz = gviz.gviz(root.panel, (140,140),
            build_dimensions = root.build_dimensions_list,
            grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
            extrusion_width = root.settings.preview_extrusion_width)
        root.gviz.SetToolTip(wx.ToolTip("Click to examine / edit\n  layers of loaded file"))
        root.gviz.showall = 1
        try:
            raise ""
            import printrun.stlview
            root.gwindow = printrun.stlview.GCFrame(None, wx.ID_ANY, 'Gcode view, shift to move view, mousewheel to set layer', size = (600, 600))
        except:
            root.gwindow = gviz.window([],
            build_dimensions = root.build_dimensions_list,
            grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
            extrusion_width = root.settings.preview_extrusion_width)
        root.gviz.Bind(wx.EVT_LEFT_DOWN, root.showwin)
        root.gwindow.Bind(wx.EVT_CLOSE, lambda x:root.gwindow.Hide())
        self.Add(root.gviz, 1, flag = wx.SHAPED)
        #cs = root.centersizer = wx.GridBagSizer()
        #self.Add(cs, 0, flag = wx.EXPAND)

class LogPane(wx.BoxSizer):

    def __init__(self, root):
        super(LogPane, self).__init__(wx.VERTICAL)
        root.lowerrsizer = self
        endjobSizer = wx.BoxSizer(wx.HORIZONTAL)
        endjobSizer.Add(wx.StaticText(parent=root.panel, label="End Job: "))
        root.endjobBedOff = wx.CheckBox(root.panel, label="Bed off")
        endjobSizer.Add(root.endjobBedOff)
        root.endjobHeatOff = wx.CheckBox(root.panel, label="Heat off")
        endjobSizer.Add(root.endjobHeatOff)
        self.Add(endjobSizer,0);
        root.logbox = wx.TextCtrl(root.panel, style = wx.TE_MULTILINE, size = (300,100))
        root.logbox.SetEditable(0)
        self.Add(root.logbox, 1, wx.EXPAND)
        root.kb = KeyboardSizer(root)
        self.Add(root.kb,0)
        lbrs = wx.BoxSizer(wx.HORIZONTAL)
        root.commandbox = wx.TextCtrl(root.panel, style = wx.TE_PROCESS_ENTER, size = (200,20))
        root.commandbox.SetToolTip(wx.ToolTip("Send commands to printer\n(Type 'help' for simple\nhelp function)"))
        root.commandbox.Bind(wx.EVT_TEXT_ENTER, root.sendline)
        root.commandbox.Bind(wx.EVT_CHAR, root.cbkey)
        root.commandbox.history = [u""]
        root.commandbox.histindex = 1
        #root.printerControls.append(root.commandbox)
        lbrs.Add(root.commandbox, 1)
        root.sendbtn = make_button(root.panel, _("Send"), root.sendline, _("Send Command to Printer"), style = wx.BU_EXACTFIT, container = lbrs, size=(-1, 36))
        #root.printerControls.append(root.sendbtn)
        self.Add(lbrs, 0, wx.EXPAND)

class MainToolbar(wx.BoxSizer):

    def __init__(self, root):
        super(MainToolbar, self).__init__(wx.HORIZONTAL)
        
        imageFS = wx.Image(imagefile('fullscreen.png'), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        root.fullscreenbtn = wx.BitmapButton(root.panel, -1, bitmap=imageFS, size = (buttonSize[1], buttonSize[1]), style = wx.BU_EXACTFIT) #size is square, it's not a typo
        root.fullscreenbtn.Bind(wx.EVT_BUTTON, root.fullscreen)
	root.fullscreenbtn.SetToolTip(wx.ToolTip("Переключить в полноэкранный режим"))
	self.Add(root.fullscreenbtn)
        root.rescanbtn = make_autosize_button(root.panel, _("Порт"), root.rescanports, _("Communication Settings\nClick to rescan ports"))
        self.Add(root.rescanbtn, 0, wx.TOP|wx.LEFT, 0)

        root.serialport = wx.ComboBox(root.panel, -1,
                choices = root.scanserial(),
                style = wx.CB_DROPDOWN, size = (100, 25))
        root.serialport.SetToolTip(wx.ToolTip("Выбрать порт для подключения принтера"))
        root.rescanports()
        self.Add(root.serialport)

        self.Add(wx.StaticText(root.panel,-1, "@"), 0, wx.RIGHT|wx.ALIGN_CENTER, 0)
        root.baud = wx.ComboBox(root.panel, -1,
                choices = ["2400", "9600", "19200", "38400", "57600", "115200", "250000"],
                style = wx.CB_DROPDOWN,  size = (100, 25))
        root.baud.SetToolTip(wx.ToolTip("Select Baud rate for printer communication"))
        try:
            root.baud.SetValue("115200")
            root.baud.SetValue(str(root.settings.baudrate))
        except:
            pass
        self.Add(root.baud)
        root.connectbtn = make_autosize_button(root.panel, _("Подключение"), root.connect, _("Подключение к принтеру"), self)

        root.resetbtn = make_autosize_button(root.panel, _("Сброс"), root.reset, _("Перезагрузить принтер"), self)
        root.loadbtn = make_autosize_button(root.panel, _("Загрузить файл"), root.loadfile, _("Загрузить файл 3D-модели"), self)
        #root.platebtn = make_autosize_button(root.panel, _("Compose"), root.plate, _("Simple Plater System"), self)
        #root.sdbtn = make_autosize_button(root.panel, _("SD"), root.sdmenu, _("SD Card Printing"), self)
        #root.printerControls.append(root.sdbtn)
        #self.Hide(root.sdbtn)
        #self.Hide(root.platebtn)
        
        root.printbtn = make_autosize_button(root.panel, _("Печать"), root.printfile, _("Старт печати загруженного файла"), self)
        root.printbtn.Disable()
        root.pausebtn = make_autosize_button(root.panel, _("Пауза"), root.pause, _("Приостановить печать"), self)
        root.recoverbtn = make_autosize_button(root.panel, _("Вернуть"), root.recover, _("Восстановить предыдущую печать"), self)
     
        #root.fullscreenbtn = make_autosize_button(root.panel, "FS", root.fullscreen, "Make full screen", self)

class MainWindow(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # this list will contain all controls that should be only enabled
        # when we're connected to a printer
        self.printerControls = []

    def fullscreen(self, event):
	self.ShowFullScreen(not self.IsFullScreen())
        
    def createGui(self):
        self.panel = wx.Panel(self,-1, size = self.size)
        self.panel.SetBackgroundColour(self.settings.bgcolor)
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.uppersizer = MainToolbar(self)
        self.lowersizer = wx.BoxSizer(wx.HORIZONTAL)
        self.leftpane = LeftPane(self)
        self.lowersizer.Add(self.leftpane)
        self.hiddensizer = wx.BoxSizer(wx.HORIZONTAL)
        self.lowersizer.Add(self.hiddensizer)
        self.lowersizer.Hide(self.hiddensizer)
        #self.vizlogsizer = wx.BoxSizer(wx.VERTICAL)
        self.vizlogsizer = wx.GridBagSizer(hgap=5, vgap=5)
        vp = VizPane(self)
        #self.hiddensizer.Add(vp) #, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL)
        #self.hiddensizer.Hide(vp)
        self.leftpane.Add(vp, pos=(2,5), span=(4,1))
        
        self.tempdisp = wx.StaticText(self.panel,wx.ID_ANY, "",size=(300,15))
        self.graph = Graph(self, wx.ID_ANY)
	#self.kb = KeyboardSizer(self)
        self.vizlogsizer.Add(self.graph, pos=(0,0)) # wx.ID_ANY)
        #self.hiddensizer.Add(self.tempdisp)
        self.vizlogsizer.Add(self.tempdisp, pos=(1,0))
        self.vizlogsizer.Add(LogPane(self), pos=(2,0))
        #self.vizlogsizer.Add(self.kb, pos=(0,0))
        self.lowersizer.Add(self.vizlogsizer) #,wx.ID_ANY, wx.EXPAND)
        self.centersizer = wx.GridBagSizer()
        self.lowersizer.Add(self.centersizer)
        self.mainsizer.Add(self.uppersizer)
        self.mainsizer.Add(self.lowersizer) #, 1, wx.EXPAND)
        self.panel.SetSizer(self.mainsizer)
        self.status = self.CreateStatusBar()
        self.status.SetStatusText(_("Нет соединения с принтером"))
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.editbutton)
        self.Bind(wx.EVT_CLOSE, self.kill)

        self.mainsizer.Layout()
        self.mainsizer.Fit(self)

        # disable all printer controls until we connect to a printer
        self.pausebtn.Disable()
        self.recoverbtn.Disable()
        for i in self.printerControls:
            i.Disable()

        #self.panel.Fit()
        self.cbuttons_reload()
        self.graph.StartPlotting(1000)
