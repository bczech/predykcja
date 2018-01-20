import os, sys, csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from fileedit import PredoBreedTXT, PredoBreedCSV
from calculations import Calculations
from readme import PredoBreedInfo



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
        BLUP_action = QAction('BLUP', self)

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
        run.addAction(BLUP_action)

        # Info Actions
        info.addAction(how_to_action)
        info.addAction(license_action)
        info.addAction(about_us_action)

        # What Actions would do
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)
        run.triggered.connect(self.respondrun)
        info.triggered.connect(self.respondinfo)

        self.setWindowTitle('PredoBreed')
        self.resize(1400, 800)

        self.show()


    def quit_trigger(self):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            qApp.quit()

        else:
            pass


    def respondrun(self, q):
        signal = q.text()

        if signal == 'BLUP':
            self.cal_widget = Calculations()
            self.setCentralWidget(self.cal_widget)

            if self.signal == 'txt':
                self.cal_widget.onlyshow(self.signal, self.txt_widget.datatxt)

            elif self.signal == 'csv':
                self.cal_widget.onlyshow(self.signal, self.csv_widget.datacsv)


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
            self.txt_widget = PredoBreedTXT()
            self.setCentralWidget(self.txt_widget)
            self.txt_widget.open_text(path)

        elif path[0][-3:] == 'csv':
            self.signal = 'csv'
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