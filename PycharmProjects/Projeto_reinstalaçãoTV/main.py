from PyQt5 import uic,QtWidgets
import os
from PyQt5.QtWidgets import *
import time

app = QtWidgets.QApplication([])
tela = uic.loadUi("tela.ui")

def instalar ():
    tela.setEnabled(False)
    tela.BotaoStatus.setText("Aguarde a reinstalação...")
    QApplication.processEvents()
    os.system("taskkill /f /im teamviewer.exe")
    os.system("taskkill /f /im teamviewer.exe")
    os.system("""powershell.exe -command "& {(new-object System.Net.WebClient).DownloadFile('https://download.teamviewer.com/download/version_13x/TeamViewer_Setup.exe','C:\SCL\ieam13.exe')}""")
    os.system("""powershell.exe -Command "& {$Install = Start-Process 'C:\SCL\ieam13.exe' -ArgumentList '/S' -PassThru}""")
    time.sleep(20)

    tela.BotaoStatus.setText("Team Viewer reinstalado com sucesso!!!")
    tela.setEnabled(True)

tela.BotaoInstalar.clicked.connect(instalar)

tela.show()
app.exec()