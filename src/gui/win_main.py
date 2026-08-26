from PySide6.QtWidgets import QMainWindow, QWidget
from win_main_ui import Ui_MainWindow

class WinMain( QMainWindow ):
    def __init__( self, aParent: QWidget = None ):
        super().__init__( aParent )

        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )

