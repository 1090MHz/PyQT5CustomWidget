from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon
from custom_vtext import VerticalText

class VerticalTextPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent=None):
        super(VerticalTextPlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, formEditor):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return VerticalText(parent)

    def name(self):
        return "VerticalText"

    def group(self):
        return "Custom Widgets"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return "This is a custom widget"

    def whatsThis(self):
        return "This is a custom widget created for demonstration purposes."

    def isContainer(self):
        return False

    def domXml(self):
        return '<widget class="VerticalText" name="VerticalText">\n' \
               '</widget>\n'

    def includeFile(self):
        return "custom_vtext"