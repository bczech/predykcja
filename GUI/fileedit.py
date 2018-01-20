import os, csv
import pandas as pd
from PyQt5.QtWidgets import *



class PredoBreedCSV(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)

        self.init_ui()


    def init_ui(self):
        self.show()


    def new_sheet(self):
        pass


    def open_sheet(self, path):
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(3)
                my_file = csv.reader(csv_file, delimiter=';', lineterminator='\n')

                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)

                    if len(row_data) > 3:
                        self.setColumnCount(len(row_data))

                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)

            self.datacsv = pd.read_csv(path[0], sep=';')
            self.show()


    def save_sheet(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), '*.csv')
        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')

                for row in range(self.rowCount()):
                    row_data = []

                    for column in range(self.columnCount()):
                        item = self.item(row, column)

                        if item is not None:
                            row_data.append(item.text())

                        else:
                            row_data.append('')
                    writer.writerow(row_data)
            self.open_sheet(path)

        else:
            pass



class PredoBreedTXT(QWidget):
    def __init__(self):
        super().__init__()

        self.text = QTextEdit(self)

        self.init_ui()


    def init_ui(self):
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.text)

        self.setLayout(v_layout)
        self.setWindowTitle('PredoBreed')

        self.show()


    def new_text(self):
        pass


    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        if filename[0] != '':
            with open(filename[0], 'w') as f:
                my_text = self.text.toPlainText()
                f.write(my_text)
            self.open_text(filename)

        else:
            pass


    def open_text(self, path):
        with open(path[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)
        self.datatxt = pd.read_csv(path[0], sep='\t')
        datatxt = self.datatxt
        text = self.text
        return datatxt, text


    def clear_text(self):
        self.text.clear()