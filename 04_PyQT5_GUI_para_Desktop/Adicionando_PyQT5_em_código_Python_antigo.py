"""
     Adicionando PyQT5 em código Python antigo
"""
import sys
from geraValidaCPF import *
from validacpf import *
from geradorcpf import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class GeraValidaCPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
            str(gera_cpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    geraCPFValida = GeraValidaCPF()
    geraCPFValida.show()
    qt.exec_()
