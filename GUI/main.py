import os, sys, csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class PredoBreedInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.Qlmain = QLabel('')
        self.Qltext = QLabel('')
        v_box = QVBoxLayout()
        v_box.addWidget(self.Qlmain)
        v_box.addWidget(self.Qltext)
        self.setLayout(v_box)
        self.show()

    def about_us(self):

        self.mainFont = QFont()
        self.mainFont.setBold(True)
        self.mainFont.setPixelSize(self.width() * 2)

        self.textFont = QFont()
        self.textFont.setItalic(True)
        self.textFont.setPixelSize(self.width())

        self.Qlmain.setText('About us!')
        self.Qlmain.setOpenExternalLinks(True)
        self.Qlmain.setAlignment(Qt.AlignHCenter)
        self.Qlmain.setFont(self.mainFont)

        self.Qltext.setText('We\'re Bioinformatic students, you can find us at Faculty of Biology \n'
                            'and Animal Science in Wroclaw University of Environmental and Life Sciences. \n')
        self.Qltext.setAlignment(Qt.AlignCenter)
        self.Qltext.setFont(self.textFont)


    def help(self):
        pass

    def license(self):

        self.urlLicense="<a href=\"https://github.com/bwczech/predykcja/blob/master/GUI/LICENSE.txt\">The Beerware License</a>"

        self.mainFont = QFont()
        self.mainFont.setBold(True)
        self.mainFont.setPixelSize(self.width() * 2)

        self.textFont = QFont()
        self.textFont.setItalic(True)
        self.textFont.setPixelSize(self.width())

        self.Qlmain.setText(self.urlLicense)
        self.Qlmain.setOpenExternalLinks(True)
        self.Qlmain.setAlignment(Qt.AlignHCenter)
        self.Qlmain.setFont(self.mainFont)

        self.Qltext.setText('Artur Wójtowicz and Bartosz Czech wrote this code. As long as you retain \n'
                             'this notice, you can do whatever you want with this stuff. If we \n'
                             'meet someday, and you think this stuff is worth it, you can \n'
                             'buy us a beer in return.')
        self.Qltext.setAlignment(Qt.AlignCenter)
        self.Qltext.setFont(self.textFont)

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
        self.datatxt = pd.read_csv(path[0], sep=';')

    def clear_text(self):
        self.text.clear()


class PredoBreedMain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.datatxt = ()
        self.datacsv = ()

        self.init_ui()

    def init_ui(self):
        # Set a menubar
        bar = self.menuBar()

        # Append bars to Menu
        file = bar.addMenu('File')
        run = bar.addMenu('Run')
        info = bar.addMenu('Info')

        # Create Actions and Shortcuts
        # File Actions
        new_menu = file.addMenu('New')
        new_csv_action = QAction('CSV file', self)
        new_txt_action = QAction('TXT file', self)

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)


        # Run Actions


        # Info Actions
        how_to_action = QAction('Help', self)
        about_us_action = QAction('About us!', self)
        license_action = QAction('License', self)

        # Adding Actions into bars created
        # File Actions
        new_menu.addAction(new_csv_action)
        new_menu.addAction(new_txt_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addSeparator()
        file.addAction(quit_action)

        # Run Actions


        # Info Actions
        info.addAction(how_to_action)
        info.addAction(license_action)
        info.addAction(about_us_action)

        # What Actions would do
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)
        info.triggered.connect(self.respondinfo)

        self.setWindowTitle('PredoBreed')
        self.resize(1400, 800)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == 'CSV file':
            self.signal = 'csv'
            self.csv_widget = PredoBreedCSV(10000, 10)
            self.setCentralWidget(self.csv_widget)
            self.csv_widget.new_sheet()
        elif signal == 'TXT file':
            self.signal = 'txt'
            self.txt_widget = PredoBreedTXT()
            self.setCentralWidget(self.txt_widget)
            self.txt_widget.new_text()
        elif signal == '&Open':
            self.open_text()
        elif signal == '&Save':
            self.save_text()

    def respondinfo(self, q):
        signal = q.text()
        self.lic_widget = PredoBreedInfo()
        self.setCentralWidget(self.lic_widget)
        if signal == 'License':
            self.lic_widget.license()
        elif signal == 'About us!':
            self.lic_widget.about_us()
        elif signal == 'Help':
            self.lic_widget.help()

    def open_text(self):
        path = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if path[0][-3:] == 'txt':
            self.signal = 'txt'
            self.datacsv = pd.read_csv(path[0], sep=';')
            self.datatxt = ''
            self.txt_widget = PredoBreedTXT()
            self.setCentralWidget(self.txt_widget)
            self.txt_widget.open_text(path)

        elif path[0][-3:] == 'csv':
            self.signal = 'csv'
            self.datatxt = pd.read_csv(path[0], sep=';')
            self.datacsv = ''
            self.csv_widget = PredoBreedCSV(10, 10)
            self.setCentralWidget(self.csv_widget)
            self.csv_widget.open_sheet(path)

    def save_text(self):
        if self.signal == 'txt':

            self.txt_widget.save_text()
        if self.signal == 'csv':

            self.csv_widget.save_sheet()
        else:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    writer = PredoBreedMain()
    sys.exit(app.exec_())
