# netstat gui with pyqt
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
import os
import subprocess

class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)

        # configure table
        self.tableView.setRowCount(100)
        self.tableView.setColumnCount(8)
        self.tableView.setHorizontalHeaderLabels(['Proto','Recv-','Send-Q','Local Address','Foreign Address','State','PID/Program name','Time'])

        # get netstat output
        result = subprocess.check_output("netstat -antop", shell=True)
        lines = result.decode("utf-8").split("\n")

        # show in table
        lineIndex = 0
        for line in lines:
            print(line)

            if line is not None:
                if len(line) > 1 and line[0] == 't':
                    vals = line.split()
                    for j in range(0,8):
                        self.tableView.setItem(lineIndex,j, QTableWidgetItem(vals[j]))


                    lineIndex = lineIndex + 1
        self.tableView.move(0,0)
 
app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
