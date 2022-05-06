import sys
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout
import random

rastgeleSayi = random.randrange(1,101)

class Pencere(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazi_alani = QTextEdit()
        self.tahmin = QPushButton("Tahmin Et!")
        self.yazi = QLabel("1 ile 100 arasında bir sayı giriniz.")

        h_box = QHBoxLayout()

        h_box.addWidget(self.tahmin)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.yazi_alani)

        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.tahmin.clicked.connect(self.tahmin_edildi)
        self.setWindowTitle("Sayı Tahmin Oyunu")
        self.show()
    def tahmin_edildi(self):
        if str(rastgeleSayi) > self.yazi_alani.toPlainText():
            self.yazi.setText("Rastegele sayi tahmininizden daha büyük.")
        elif str(rastgeleSayi) < self.yazi_alani.toPlainText():
            self.yazi.setText("Rastgele sayi tahmininizden daha küçük.")
        else:
            self.yazi.setText("Tebrikler tahmininiz doğru")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())