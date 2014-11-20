from PySide import QtGui

import maya.cmds as cmds


class TestDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)           
        self.setObjectName('testDialogControl')     
        self.setWindowTitle("Test window")
        self.__vlayout = QtGui.QVBoxLayout(self)
        self.__button = QtGui.QPushButton('Test')
        self.__button.pressed.connect(self.testcmd)
        self.__vlayout.addWidget(self.__button)
        self.dock_ui()
        
    def testcmd(self):
        print 'test'
        
    def dock_ui(self):
        self.close()
        
        if cmds.dockControl('testDock', q=1, ex=1):
            cmds.deleteUI('testDock')
            
        allowedAreas = ['right', 'left']
        
        try:
            floatingLayout = cmds.paneLayout(configuration='single', width=200, height=400)
        except:
            self.show()
            return False

        cmds.dockControl('testDock', area='right', allowedArea=allowedAreas, content=floatingLayout, label='TestDock')
        cmds.control('testDialogControl', e=True, p=floatingLayout)
        return True
        
test = TestDialog()
test.show()