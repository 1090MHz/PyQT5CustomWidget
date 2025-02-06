# PyQT5CustomWidget

Creating a custom widget in PyQt5 for use in Qt Designer involves several steps. Below is a complete example demonstrating how to create a custom widget and integrate it into Qt Designer.

### Step 1: Create the Custom Widget

First, create a custom widget in PyQt5. This widget will be a simple example that extends `QWidget`.

```python name=custom_widget.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        
        self.label = QLabel("This is a custom widget", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
```

### Step 2: Create a Plugin for Qt Designer

Next, create a plugin that allows Qt Designer to recognize and use the custom widget.

```python name=custom_widget_plugin.py
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon
from custom_widget import CustomWidget

class CustomWidgetPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent=None):
        super(CustomWidgetPlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, formEditor):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return CustomWidget(parent)

    def name(self):
        return "CustomWidget"

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
        return '<widget class="CustomWidget" name="customWidget">\n' \
               '</widget>\n'

    def includeFile(self):
        return "custom_widget"
```

### Step 3: Install the Plugin

To install the plugin in Qt Designer, follow these steps:

1. **Build the Plugin**: Create a Python package for the plugin. Make sure the package includes both `custom_widget.py` and `custom_widget_plugin.py`.

2. **Configure Qt Designer**: Modify the `designer` configuration to load the plugin. This typically involves setting the `PYQTDESIGNERPATH` environment variable to the directory containing your plugin.

For example, if your plugin is in the directory `/path/to/plugins`, set the environment variable as follows:

```sh
export PYQTDESIGNERPATH=/path/to/plugins
```

3. **Load the Plugin**: Restart Qt Designer, and the custom widget should appear in the "Custom Widgets" group.

### Step 4: Use the Custom Widget in Qt Designer

Open Qt Designer, and you should see the new custom widget in the "Custom Widgets" group. Drag and drop the custom widget onto your form and use it like any other widget.

This setup allows you to create custom widgets in PyQt5 and use them within Qt Designer, enabling a more dynamic and customized GUI design process.