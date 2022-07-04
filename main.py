from PySide6.QtWidgets import QApplication
from guiApp import Ui_MainWindow
import sys

class AppUi_MainWindow(Ui_MainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.pushButton_confirmation_usb.clicked.connect(self.button_confirmation_usb_clicked)
        
    def button_confirmation_usb_clicked(self) -> None:
        self.confirmation_label_usb.setText("Button Clicked")
        
    def addItem_list_disc_from_so(self):
        pass
    #TODO: https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
    #TODO: Llamar a la función que enlista los discos del SO.
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = AppUi_MainWindow()
    widget.show()
    
    sys.exit(app.exec())