import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import mainwindows  # 调用生成的.py文件
from tkinter import filedialog
import shutil
import re

def replacement(Path,old,new):
    with open(Path, "r+") as f1:
       contents = f1.read()
       pattern = re.sub(old,new,contents)
       f1.seek(0)
       f1.truncate()
       f1.write(pattern)
       f1.close()

def Click_b1():
    ui.plainTextEdit.setPlainText(filedialog.askopenfilename())

def Click_b2():
    shutil.copy("ecut-test.sh.sample","ecut-test.sh")
    f=open(ui.plainTextEdit.toPlainText())
    scf_in = f.read()
    f.close()
    replacement("ecut-test.sh","Inputscf_in",scf_in)
    replacement("ecut-test.sh","Inputscale",ui.plainTextEdit_2.toPlainText())
    replacement("ecut-test.sh","Input_command",ui.plainTextEdit_3.toPlainText())
    replacement("ecut-test.sh","ecutrho                   = *\d*","ecutrho                   =  ${ecutr}")
    replacement("ecut-test.sh","ecutwfc                   = *\d*","ecutwfc                   =  ${ecut}")
    replacement("ecut-test.sh","K_POINTS {automatic} \n *\d *\d *\d ","K_POINTS {automatic} \n$kmeshs ")
    replacement("ecut-test.sh","Input_kmeshs",ui.plainTextEdit_4.toPlainText())
    msg_box = QMessageBox(QMessageBox.Information, "Note", "ecut-test.sh is already produced. OVO from your Maple!")
    msg_box.exec_()

def Click_b3():
    shutil.copy("k-test.sh.sample","k-test.sh")
    f=open(ui.plainTextEdit.toPlainText())
    scf_in = f.read()
    f.close()
    replacement("k-test.sh","Inputscf_in",scf_in)
    replacement("k-test.sh","Input_kmeshs",ui.plainTextEdit_2.toPlainText())
    replacement("k-test.sh","Input_command",ui.plainTextEdit_3.toPlainText())
    replacement("k-test.sh","ecutrho                   = *\d*","ecutrho                   =  ${ecutr}")
    replacement("k-test.sh","ecutwfc                   = *\d*","ecutwfc                   =  ${ecut}")
    replacement("k-test.sh","K_POINTS {automatic} \n *\d *\d *\d ","K_POINTS {automatic} \n$k ")
    replacement("k-test.sh","Inputecut",ui.plainTextEdit_4.toPlainText())
    msg_box = QMessageBox(QMessageBox.Information, "Note", "k-test.sh is already produced. OVO from your Maple!")
    msg_box.exec_()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainwindows.Ui_QEtest()  
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(Click_b1)
    ui.pushButton_2.clicked.connect(Click_b2)
    ui.pushButton_3.clicked.connect(Click_b3)
    sys.exit(app.exec_())

