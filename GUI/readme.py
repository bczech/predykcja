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

        self.Qltext.setText('Artur Wójtowicz and Bartosz Czech – biostatistics and bioinformatic programming students\n'
                            'at Faculty of Biology and Animal Science at Wroclaw University of Environmental and Life Sciences. \n'
                            'Aim of this software was to create a tool which will be used by animal husbandrists to genetic \n'
                            'evaluation of farmed animals.\n'
                            '\nWe are interesting in applying a statistics models in biology. We would like to facilitate \n'
                            'the work of biologists and zootechnicians for whom statistical tools are not always easy to use.\n'
                            'Widespread use of the BLUP method has inspired us to create a tool for prediction a genetic value\n'
                            'based on relationship between animals, yield value and belonging to the herd. \n'
                            '\nIn the future we would like to create extra models to this software, insofar as we are able, based on\n'
                            'molecular markers (e.g. SNPs, INDELs, VCFs).\n')
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