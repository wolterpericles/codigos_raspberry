from PyQt5 import QtWidgets
from gui_amperimetro import Ui_MainWindow
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.selecionarEntrada.addItems(["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9"])


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()