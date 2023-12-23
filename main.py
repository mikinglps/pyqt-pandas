import sys
import pandas as pd
from PyQt5.QtWidgets import *;

class ButtonHandler:
    def __init__(self):
        self._df = []
        self._layout = QVBoxLayout()
        self._button = QPushButton("Load File")
        self._layout.addWidget(self._button) 
        self._button.clicked.connect(lambda: self.on_clicked())
        self._isActive = False;
        self._table = QTableWidget()

    def on_clicked(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self._df = pd.read_csv(path).head(5)
        self.show_table()
    
    def show_table(self):
        if self._isActive is True:
            self._layout.removeWidget(self._table)
            self._table.deleteLater()
            self._table = QTableWidget()
            self._isActive = False
        
        for i in range(len(self._df['#'].astype('int'))):
            self._table.insertRow(i)
            for k in range(12):
                self._table.setColumnCount(12)
                self._table.setHorizontalHeaderLabels(self._df.columns)
                self._table.setItem(i, k, QTableWidgetItem(self._df.iloc[[i],[k]].to_string(index=False, header=False)))
        self._layout.addWidget(self._table)
        self._table.show()
        self._isActive = True;
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget();
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle("Load File and Parse to Pandas")
    window.setLayout(ButtonHandler()._layout)
    window.show()
    sys.exit(app.exec_())