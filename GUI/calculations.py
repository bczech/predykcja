import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Calculations(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.h2askvalue = QLabel('Squared h value: ')
        self.h2askvalue.setAlignment(Qt.AlignRight)

        self.h2value = QLineEdit()
        self.h2value.setAlignment(Qt.AlignCenter)
        self.h2value.setText('0.25')

        self.h2slider = QSlider(Qt.Horizontal)
        self.h2slider.setMinimum(0)
        self.h2slider.setMaximum(100)
        self.h2slider.setValue(25)
        self.h2slider.setTickInterval(10)
        self.h2slider.setTickPosition(QSlider.TicksBelow)

        self.parents = QTextBrowser()
        self.breed = QTextBrowser()
        self.ranking = QTextBrowser()

        self.startbut = QPushButton('Ranking', self)
        self.plot = QPushButton('Plot', self)
        self.Pearson = QPushButton('Pearson', self)

        lay = QGridLayout()

        lay.addWidget(self.h2askvalue, 1, 0)
        lay.addWidget(self.h2value, 1, 1)
        lay.addWidget(self.h2slider, 1, 2)
        lay.addWidget(self.startbut, 1, 3)
        lay.addWidget(self.plot, 1, 4)
        lay.addWidget(self.Pearson, 1, 5)

        lay.addWidget(self.parents, 10, 0, 1, 1)
        lay.addWidget(self.breed, 10, 1, 1, 1)
        lay.addWidget(self.ranking, 10, 2, 1, 4)

        self.setLayout(lay)
        self.show()

        self.h2slider.valueChanged.connect(self.h2_change)

        self.startbut.clicked.connect(self.rankingchange)
        self.plot.clicked.connect(self.showplot)
        self.Pearson.clicked.connect(self.CalcPears)

        self.show()


    def CalcPears(self):
        if self.rank != '':
            corr = Calc().Pearson(self.y, self.predy)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Korelacja Pearsona: %15s' % corr[0])
            msg.setInformativeText('Wartość p: %27s' % corr[1])
            msg.setWindowTitle("Pearson")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Ranking has to be done as first")
            msg.setWindowTitle("Warning!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


    def onlyshow(self, signal, data):
        self.rank = ''
        self.dane = ''

        for i in data[0:0]:
            self.dane += str(i) + '\t'

        self.dane += '\n'
        for j in range(data.shape[0]):
            for i in data[0:0]:
                self.dane += str(data[i][j]) + '\t'
            self.dane += '\n'

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Two files required. One with breeding values, second with information about parents.")
        msg.setInformativeText("Check details for information about already opened file.")
        msg.setWindowTitle("Two files required!")
        msg.setDetailedText(self.dane)
        msg.setStandardButtons(QMessageBox.Open)
        msg.exec_()

        path = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))

        data2 = self.getdata2(path, signal, data)

        for j in range(data2.shape[0]):
            for i in data2[0:0]:
                self.dane2 += str(data2[i][j]) + '\t'
            self.dane2 += '\n'

        if 'sire' in data2[0:0]:
            sire = 'dane2'
            self.parents.setText(self.dane2)

        else:
            sire = 'dane'
            self.parents.setText(self.dane)

        if 'sire' not in data2[0:0]:
            self.breed.setText(self.dane2)

        else:
            self.breed.setText(self.dane)

        if sire == 'dane2':
            self.datasi = Calc().datasire(data2, data)

        elif sire == 'dane':
            datasi = Calc().datasire(data, data2)
            self.wynik = datasi[0]
            self.dane_hod = datasi[1]
            self.dane_hodowlane = datasi[2]


    def getdata2(self, path, signal, data):
        if path[0] != '':
            if path[0][-3:] == 'txt':
                data2 = pd.read_csv(path[0], sep='\t')
                self.dane2 = ''
                for i in data2[0:0]:
                    self.dane2 += str(i) + '\t'
                self.dane2 += '\n'
                return data2

            elif path[0][-3:] == 'csv':
                data2 = pd.read_csv(path[0], sep=';')
                self.dane2 = ''
                for i in data2[0:0]:
                    self.dane2 += str(i) + '\t'
                self.dane2 += '\n'
                return data2

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Only files in format .txt or .csv acceptable")
                msg.setInformativeText("Open, to try again. Cancel to pass.")
                msg.setWindowTitle("Warning!")
                msg.setDetailedText(self.dane)
                msg.setStandardButtons(QMessageBox.Open | QMessageBox.Cancel)
                msg.exec_()
                self.signal = signal
                self.data = data
                msg.buttonClicked.connect(self.msgbtn)
        else:
            self.onlyshow(signal, data)


    def msgbtn(self, i):
        if i.text() == 'Open':
            self.onlyshow(self.signal, self.data)

        elif i.text() == 'Cancel':
            pass

        else:
            print('Error msgbtn')



    def rankingchange(self):
        RankingCh = Calc().rankingchange(self.h2value.text(), self.datasi[0], self.datasi[1], self.datasi[2])
        self.rank = RankingCh[0]
        self.y = RankingCh[1]
        self.predy = RankingCh[2]
        self.ranking.setText(self.rank)


    def showplot(self):
        if self.rank != '':
            Calc().makeplot(self.y, self.predy)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Ranking has to be done as first")
            msg.setWindowTitle("Warning!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


    def h2_change(self):
        my_value = str(self.h2slider.value() / 100)
        self.h2value.setText(my_value)

class Calc:
    def RelMatrixA(self, s, d):
        n = len(s)
        N = n + 1
        A = np.zeros((N, N))
        s = (s == 0) * N + s
        d = (d == 0) * N + d

        for i in range(n):
            A[i, i] = 1 + A[s[i] - 1, d[i] - 1] * 0.5

            for j in range(i + 1, n):
                if j > n:
                    break
                A[i, j] = (A[i, s[j] - 1] + A[i, d[j] - 1]) * 0.5
                A[j, i] = A[i, j]
        return A

    def datasire(self, data, data2):
        self.datasire = data.as_matrix()
        n = len(self.datasire[:, 0])
        wynik = self.RelMatrixA(self.datasire[:, 1], self.datasire[:, 2])[0:n, 0:n]
        dane_hod = data2
        dane_hodowlane = data2.as_matrix()
        return wynik, dane_hod, dane_hodowlane

    def rankingchange(self, h2, wynik, dane_hod, dane_hodowlane):
        self.y = dane_hodowlane[:, 1]
        List = []

        for k in dane_hodowlane[:, 2]:
            if k not in List:
                List.append(k)

        herd = {}
        for j in range(len(List)):
            herd[j] = List[j]

        x = np.zeros((len(dane_hodowlane), len(herd) + 1))
        for i in range(len(x)):
            for j in range(len(herd)):
                if herd[j] == dane_hodowlane[:, 2][i]:
                    x[i][0], x[i][j + 1] = 1, 1

        z = np.zeros((len(self.y), len(self.y)))
        np.fill_diagonal(z, 1)
        np.savetxt('macierz_stalych_testowy.txt', x)
        np.savetxt('macierz_losowych_testowy.txt', z)
        A = wynik
        odwrA = np.linalg.inv(A)
        x_t = x.transpose()
        z_t = z.transpose()
        L11 = x_t.dot(x)
        L21 = z_t.dot(x)
        L12 = x_t.dot(z)
        L22 = z_t.dot(z) + odwrA * (1 - float(h2)) / float(h2)
        L1 = np.column_stack((L11, L12))
        L2 = np.column_stack((L21, L22))
        L = np.concatenate([L1, L2])
        odwrL = np.linalg.pinv(L)
        P1 = x_t.dot(self.y)
        P2 = z_t.dot(self.y)
        P = np.concatenate([P1, P2])
        result = odwrL.dot(P)
        b = result[0:len(herd) + 1]
        a = result[len(herd) + 1:]
        self.predy = x.dot(b) + z.dot(a)
        self.e = self.predy - self.y
        dane_hod['BreedingValue'] = a
        self.dane_hod2 = dane_hod.nlargest(dane_hod.shape[0], 'BreedingValue')
        self.dane_hod2 = self.dane_hod2.values.tolist()
        self.rank = ''

        for i in dane_hod[0:0]:
            self.rank += str(i) + '\t'
        self.rank += '\n'

        for i in range(len(self.dane_hod2)):
            for j in range(len(self.dane_hod2[i])):
                self.rank += str(self.dane_hod2[i][j]) + '\t'
            self.rank += '\n'
        return self.rank, self.y, self.predy

    def Pearson(self, y, predy):
        predylist = []

        for i in range(len(predy)):
            predylist.append(predy[i])

        return stats.pearsonr(predylist, y)

    def makeplot(self, y, predy):
        plt.figure(figsize=(20, 10))

        for i in range(len(predy)):
            plt.scatter(y[i], predy[i], color='black')

        plt.title('Real values versus prognoses')
        plt.xlabel('Real values')
        plt.ylabel('Phenotype prognoses')
        plt.show()