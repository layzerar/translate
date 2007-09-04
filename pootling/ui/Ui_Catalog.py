# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/k-da/Documents/poxole/trunk/pootling/ui/Catalog.ui'
#
# Created: Tue Sep  4 14:37:52 2007
#      by: PyQt4 UI code generator 4-snapshot-20070212
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Catalog(object):
    def setupUi(self, Catalog):
        Catalog.setObjectName("Catalog")
        Catalog.setWindowModality(QtCore.Qt.NonModal)
        Catalog.resize(QtCore.QSize(QtCore.QRect(0,0,359,412).size()).expandedTo(Catalog.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Catalog.sizePolicy().hasHeightForWidth())
        Catalog.setSizePolicy(sizePolicy)

        self.centralwidget = QtGui.QWidget(Catalog)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.treeCatalog = QtGui.QTreeWidget(self.centralwidget)

        font = QtGui.QFont(self.treeCatalog.font())
        font.setPointSize(10)
        self.treeCatalog.setFont(font)
        self.treeCatalog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.treeCatalog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeCatalog.setAcceptDrops(False)
        self.treeCatalog.setAlternatingRowColors(True)
        self.treeCatalog.setObjectName("treeCatalog")
        self.gridlayout.addWidget(self.treeCatalog,0,0,1,1)
        Catalog.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(Catalog)
        self.menubar.setGeometry(QtCore.QRect(0,0,359,29))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")

        self.menuOpenRecentProject = QtGui.QMenu(self.menuProject)
        self.menuOpenRecentProject.setEnabled(False)
        self.menuOpenRecentProject.setObjectName("menuOpenRecentProject")

        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Catalog.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(Catalog)
        self.statusbar.setObjectName("statusbar")
        Catalog.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(Catalog)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setObjectName("toolBar")
        Catalog.addToolBar(self.toolBar)

        self.actionQuit = QtGui.QAction(Catalog)
        self.actionQuit.setIcon(QtGui.QIcon("../images/exit.png"))
        self.actionQuit.setObjectName("actionQuit")

        self.actionAbout = QtGui.QAction(Catalog)
        self.actionAbout.setObjectName("actionAbout")

        self.actionAboutQt = QtGui.QAction(Catalog)
        self.actionAboutQt.setObjectName("actionAboutQt")

        self.actionReload = QtGui.QAction(Catalog)
        self.actionReload.setEnabled(False)
        self.actionReload.setIcon(QtGui.QIcon("../images/reload.png"))
        self.actionReload.setObjectName("actionReload")

        self.actionConfigure = QtGui.QAction(Catalog)
        self.actionConfigure.setIcon(QtGui.QIcon("../images/configure.png"))
        self.actionConfigure.setObjectName("actionConfigure")

        self.actionFind_in_Files = QtGui.QAction(Catalog)
        self.actionFind_in_Files.setEnabled(False)
        self.actionFind_in_Files.setIcon(QtGui.QIcon("../images/find.png"))
        self.actionFind_in_Files.setObjectName("actionFind_in_Files")

        self.actionStatistics = QtGui.QAction(Catalog)
        self.actionStatistics.setEnabled(False)
        self.actionStatistics.setIcon(QtGui.QIcon("../images/statistic.png"))
        self.actionStatistics.setObjectName("actionStatistics")

        self.actionBuildTM = QtGui.QAction(Catalog)
        self.actionBuildTM.setObjectName("actionBuildTM")

        self.actionNew = QtGui.QAction(Catalog)
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtGui.QAction(Catalog)
        self.actionOpen.setObjectName("actionOpen")

        self.actionBuild = QtGui.QAction(Catalog)
        self.actionBuild.setIcon(QtGui.QIcon("../images/memory.png"))
        self.actionBuild.setObjectName("actionBuild")

        self.actionConfigure1 = QtGui.QAction(Catalog)
        self.actionConfigure1.setIcon(QtGui.QIcon("../images/configure.png"))
        self.actionConfigure1.setObjectName("actionConfigure1")

        self.actionStop = QtGui.QAction(Catalog)
        self.actionStop.setEnabled(False)
        self.actionStop.setIcon(QtGui.QIcon("../images/stop.png"))
        self.actionStop.setObjectName("actionStop")

        self.actionClose = QtGui.QAction(Catalog)
        self.actionClose.setEnabled(False)
        self.actionClose.setIcon(QtGui.QIcon("../images/fileclose.png"))
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionFind_in_Files)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionStatistics)
        self.menuEdit.addAction(self.actionReload)
        self.menuEdit.addAction(self.actionStop)
        self.menuProject.addAction(self.actionNew)
        self.menuProject.addAction(self.actionOpen)
        self.menuProject.addAction(self.menuOpenRecentProject.menuAction())
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionClose)
        self.menuSettings.addAction(self.actionBuild)
        self.menuSettings.addAction(self.actionConfigure)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionFind_in_Files)
        self.toolBar.addAction(self.actionStatistics)
        self.toolBar.addAction(self.actionReload)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.actionConfigure)

        self.retranslateUi(Catalog)
        QtCore.QMetaObject.connectSlotsByName(Catalog)

    def retranslateUi(self, Catalog):
        Catalog.setWindowTitle(QtGui.QApplication.translate("Catalog", "Catalog Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.treeCatalog.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Catalog Manager</h3>Catalog Manager is a central place where you can see all files in your project as tree with the statistic information such as the number of untranslated strings, fuzzy strings, translated strings, total number of entries, file location, last revision and last translator.", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Catalog", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Catalog", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProject.setTitle(QtGui.QApplication.translate("Catalog", "&Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpenRecentProject.setToolTip(QtGui.QApplication.translate("Catalog", "This open recent project.", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpenRecentProject.setStatusTip(QtGui.QApplication.translate("Catalog", "Open the recent project.", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpenRecentProject.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Open recent project</h3>Use this to open the project file that was just opened lately.", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpenRecentProject.setTitle(QtGui.QApplication.translate("Catalog", "Open &Recent Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("Catalog", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Catalog", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("Catalog", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("Catalog", "Quit the application.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Quit</h3>Use this to quit the application. Any unsaved changes will be prompted.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("Catalog", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("Catalog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setStatusTip(QtGui.QApplication.translate("Catalog", "Display information about this software.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>About</h3>Display information about this software.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("Catalog", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setStatusTip(QtGui.QApplication.translate("Catalog", "Display information about the Qt toolkit.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>About Qt</h3>Display information about the Qt toolkit.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload.setText(QtGui.QApplication.translate("Catalog", "&Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload.setStatusTip(QtGui.QApplication.translate("Catalog", "Reload the current files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Reload</h3>Set the current files or folders to get the most up-to-date version.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload.setShortcut(QtGui.QApplication.translate("Catalog", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure.setText(QtGui.QApplication.translate("Catalog", "&Configure...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_in_Files.setText(QtGui.QApplication.translate("Catalog", "&Find in Files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_in_Files.setStatusTip(QtGui.QApplication.translate("Catalog", "Find string through files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_in_Files.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Find</h3>Use this to find a word or a string through all files of the current project in the Catalog Manager. The find dialog will be shown at the bottom of the editor.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_in_Files.setShortcut(QtGui.QApplication.translate("Catalog", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStatistics.setText(QtGui.QApplication.translate("Catalog", "&Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStatistics.setStatusTip(QtGui.QApplication.translate("Catalog", "Show status of selected file or folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStatistics.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Statistics</h3>Show status of selected file or folder with information about filename, untranslated, fuzzy, translated and total number of strings.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStatistics.setShortcut(QtGui.QApplication.translate("Catalog", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuildTM.setText(QtGui.QApplication.translate("Catalog", "&Build TM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("Catalog", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("Catalog", "Opens a new project dialog...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>New...</h3>Use this to open a dialog for entering  the information for a new project.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("Catalog", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("Catalog", "Open an existing project...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Open</h3>Use this to open an existing project.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setText(QtGui.QApplication.translate("Catalog", "Build TM...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setToolTip(QtGui.QApplication.translate("Catalog", "Build the translation memory.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setStatusTip(QtGui.QApplication.translate("Catalog", "Build the translation memory.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Build TM</h3>Use this to build the translation memory from the list of files in Catalog.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure1.setText(QtGui.QApplication.translate("Catalog", "Configure...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure1.setStatusTip(QtGui.QApplication.translate("Catalog", "Set the prefered configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure1.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Configure...</h3>Configure the translated file paths in a project and can toogle the view of Catalog Manager.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("Catalog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setStatusTip(QtGui.QApplication.translate("Catalog", "Stop loading catalog.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Stop</h3>Stop loading catalog.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setShortcut(QtGui.QApplication.translate("Catalog", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("Catalog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setStatusTip(QtGui.QApplication.translate("Catalog", "Close project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setWhatsThis(QtGui.QApplication.translate("Catalog", "<h3>Close</h3>Use this to close the opening project. The Catalog treeview will be cleared.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("Catalog", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Catalog = QtGui.QMainWindow()
    ui = Ui_Catalog()
    ui.setupUi(Catalog)
    Catalog.show()
    sys.exit(app.exec_())
