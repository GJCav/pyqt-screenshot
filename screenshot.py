from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
import sys
import time


from Ui_GUI import Ui_main_window


def timestamp():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


class Screenshot:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        self.app = app

        self._set_ui()
        self._bind()

    def _set_ui(self):
        main_window = QtWidgets.QWidget()
        self.main_window = main_window

        self.set_frameless(True)

        ui = Ui_main_window()
        self.ui = ui
        ui.setupUi(main_window)

        self.set_shotarea_border()

    
    def _bind(self):
        ui = self.ui
        ui.closeBtn.clicked.connect(lambda: self.app.exit(0))
        ui.shotBtn.clicked.connect(self._event_shot)
        ui.saveBtn.clicked.connect(self._event_folder)
        ui.moveBtn.mousePressEvent = lambda event: self._event_move_press(event)
        ui.moveBtn.mouseMoveEvent = lambda event: self._event_move_move(event)
        ui.resizeBtn.mousePressEvent = lambda event: self._event_resize_press(event)
        ui.resizeBtn.mouseMoveEvent = lambda event: self._event_resize_move(event)


    def _event_move_press(self, event: QtGui.QMouseEvent):
        self._move_win_pos = self.main_window.mapToGlobal(QtCore.QPoint(0, 0))
        self._move_mouse_pos = event.globalPos()


    def _event_move_move(self, event: QtGui.QMouseEvent):
        if not hasattr(self, "_move_win_pos") or not hasattr(self, "_move_mouse_pos"):
            return
        self.main_window.move(self._move_win_pos + (event.globalPos() - self._move_mouse_pos))


    def _event_resize_press(self, event: QtGui.QMouseEvent):
        self._resize_win_size = self.main_window.size()
        self._resize_mouse_pos = event.globalPos()

    
    def _event_resize_move(self, event: QtGui.QMouseEvent):
        if not hasattr(self, "_resize_win_size") or not hasattr(self, "_resize_mouse_pos"):
            return
        newsize = QtCore.QSize(
            self._resize_win_size.width() + (event.globalPos() - self._resize_mouse_pos).x(), 
            self._resize_win_size.height() + (event.globalPos() - self._resize_mouse_pos).y()
        )
        self.main_window.resize(newsize)


    def _event_shot(self):
        shotBtn = self.ui.shotBtn
        shotBtn.setDisabled(True)

        shotArea = self.ui.shotArea
        rect = shotArea.rect()
        topleft = shotArea.mapToGlobal(rect.topLeft())
        
        screen = QApplication.primaryScreen()
        border_width = self._shotarea_border_width
        pixmap = screen.grabWindow(
            0, 
            topleft.x() + border_width, 
            topleft.y() + border_width, 
            rect.width() - border_width * 2, 
            rect.height() - border_width * 2
        )
        filename = "screenshot_" + timestamp() + ".png"
        path = QtCore.QDir.currentPath()
        if hasattr(self, "_save_folder"):
            path = self._save_folder
        pixmap.save(QtCore.QDir(path).filePath(filename))

        shotBtn.setDisabled(False)
        QtWidgets.QToolTip.showText(
            shotBtn.mapToGlobal(shotBtn.rect().topLeft()),
            "Screenshot saved!  " + filename,
            self.ui.shotBtn
        )


    def _event_folder(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self.main_window,
            "Save At",
            QtCore.QDir.currentPath()
        )
        self._save_folder = path or QtCore.QDir.currentPath()

    
    def set_shotarea_border(self, color: str = "blue", width: int = 4):
        self._shotarea_border_width = width
        self.ui.shotArea.setStyleSheet(
            f"border: {width}px dashed {color};\n"
            "background: transparent;"
        )


    def set_frameless(self, flag=True):
        main_window = self.main_window
        if flag:
            main_window.setWindowFlags(
                main_window.windowFlags() | 
                QtCore.Qt.FramelessWindowHint |
                QtCore.Qt.WindowStaysOnTopHint
            )
            main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        else:
            main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground, False)
            main_window.setWindowFlags(
                main_window.windowFlags() &
                ~QtCore.Qt.FramelessWindowHint &
                ~QtCore.Qt.WindowStaysOnTopHint
            )
        self._framless = flag

    def run(self):
        self.main_window.show()
        self._event_folder()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    sc = Screenshot()
    sc.run()