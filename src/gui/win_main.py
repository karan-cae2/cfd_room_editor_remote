from PySide6.QtWidgets import QMainWindow, QWidget
from win_main_ui import Ui_MainWindow
from models.tree_model import TreeModel

class WinMain( QMainWindow ):
    def __init__( self, aParent: QWidget = None ):
        super().__init__( aParent )

        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )

        
        self.model = TreeModel()
        self.ui.treeView.setModel(self.model)
        

