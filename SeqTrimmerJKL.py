# Take a directory of forward and reverse sequencing reads (of nucleases in PCM) and parses them into an Excel file
# in the format needed to paste into the alignment spreadsheet

import glob2
from Bio import SeqIO
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 171)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.select_directory)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(610, 120, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.trim_sequences)
        self.buttonBox.rejected.connect(self.test_cancel)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 571, 128))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_3.raise_()
        self.pushButton.raise_()
        self.pushButton.raise_()
        self.buttonBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def select_directory(self):
        input_dir = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.lineEdit_5.setText(str(input_dir))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SeqTrimmer"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Sequence Folder"))
        self.label_2.setText(_translate("MainWindow", "Forward Primer Name"))
        self.label_3.setText(_translate("MainWindow", "Reverse Primer Name"))
        self.label_4.setText(_translate("MainWindow", "Forward sequence tag"))
        self.label_5.setText(_translate("MainWindow", "Reverse Sequence tag"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "pCOMBOseqF"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "SV40JKL2"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "ATGAATACAAAATAT"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "TTAGGGGGACGAC"))

    def test_cancel(self):
        MainWindow.close()

    def trim_sequences(self):
        if self.lineEdit_5.text() == "":
            pass
        else:
            seq_directory = self.lineEdit_5.text()
            if self.lineEdit_4.text() == "":
                forwardid = "pCOMBOseqF"
            else:
                forwardid = self.lineEdit_4.text()
            if self.lineEdit_3.text() == "":
                reverseid = "SV40JKL2"
            else:
                reverseid = self.lineEdit_3.text()
            if self.lineEdit_2.text() == "":
                startseq = "ATGAATACAAAATAT"
            else:
                startseq = self.lineEdit_2.text()
            if self.lineEdit.text() == "":
                endseq = "TTAGGGGGACGAC"
            else:
                endseq = self.lineEdit.text()
            # print (seq_directory)
            # print (forwardid)
            # print (reverseid)
            # print (startseq)
            # print (endseq)
            seq_path = seq_directory + r"\\*.seq"
            files = glob2.glob(seq_path)
            forward_reads = []
            reverse_reads = []
            for seqfile in files:
                sequence = ""
                for seq in SeqIO.parse(open(seqfile), "fasta"):
                    if forwardid in seq.id:
                        if startseq not in str(seq.seq):
                            sequence = "Check manually"
                        else:
                            startpoint = str(seq.seq).find(startseq)
                            sequence = str(seq.seq)[startpoint:]
                        nametrimmer = str(seq.id).find(forwardid)
                        name = str(seq.id)[:nametrimmer - 1]
                        forward_reads.append([name, sequence])
                    elif reverseid in seq.id:
                        if endseq not in str(seq.seq):
                            sequence = "Check manually"
                        else:
                            endpoint = str(seq.seq).find(endseq)
                            sequence = str(seq.seq)[endpoint:]
                        nametrimmer = str(seq.id).find(reverseid)
                        name = str(seq.id)[:nametrimmer - 1]
                        reverse_reads.append([name, sequence])
            outpath = seq_directory + r"\\Results.csv"
            forward_reads.sort()
            reverse_reads.sort()
            with open(outpath, "w") as output_file:
                for line in forward_reads:
                    output_file.write(str(line[0]) + "," + str(line[1]) + "\n")
                output_file.write("\n\n")
                for line in reverse_reads:
                    output_file.write(str(line[0]) + "," + str(line[1]) + "\n")
        QMessageBox.about(MainWindow, " ", "Done!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# TODO
# from Bio import SeqIO
#
# my_file = "example.csv"  # Obviously not FASTA
#
# def is_fasta(filename):
#     with open(filename, "r") as handle:
#         fasta = SeqIO.parse(handle, "fasta")
#         return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file
#
# is_fasta(my_file)
# False
#
# Also add in a file open check - it will fail if any of the files are open
