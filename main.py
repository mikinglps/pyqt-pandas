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

    def on_clicked(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self._df = pd.read_csv(path).head(5)
        self.show_table()
    
    def show_table(self):
        table = QTableWidget()
        for i in range(len(self._df['#'].astype('int'))):
            table.insertRow(i)
            for k in range(12):
                table.setColumnCount(12)
                table.setHorizontalHeaderLabels(self._df.columns)
                table.setItem(i, k, QTableWidgetItem(self._df.iloc[[i],[k]].to_string(index=False, header=False)))
        self._layout.addWidget(table)
        table.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget();
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle("Load File and Parse to Pandas")
    window.setLayout(ButtonHandler()._layout)
    window.show()
    sys.exit(app.exec_())