from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QListWidgetItem,
    QMessageBox,
    QDialog,
)
from PySide6.QtCore import QPointF
import sys
from main_ui import Ui_MainWindow
from pathlib import Path
from PIL import Image
from process import CLAHETransform
from CLAHE_ui import Ui_Dialog as Ui_CLAHE
from cut_ui import Ui_Dialog as Ui_Cut
from confirm_cut_ui import Ui_Dialog as Ui_ConfirmCut
from PIL import Image,ImageQt
import time

class ConfirmCutDialog(QDialog, Ui_ConfirmCut):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
    def closeEvent(self, arg__1: QCloseEvent) -> None:
        if self.output_path.text() == "":
            QMessageBox.information(self, "提示", "请输入输出路径")
            return
        return super().closeEvent(arg__1)

class CutDialog(QDialog, Ui_Cut):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)


class CLAHEDialog(QDialog, Ui_CLAHE):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class ProcessWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.output_dir: Path | None = None
        self.image: Image.Image | None = None
        self.image_now: Image.Image | None = None

        self.btn_input.clicked.connect(self.open_input_dialog)
        self.btn_output.clicked.connect(self.open_output_dialog)
        self.lst_files.itemDoubleClicked.connect(self.open_selected_file)
        self.actionOrigin.triggered.connect(self.set_origin)
        self.actionCLAHE.triggered.connect(self.set_CLAHE)
        self.actioncut.triggered.connect(self.set_cut)
        self.view.graphicsScene.cut_rectangle_clicked.connect(self.cut_image)
        self.btn_last_image.clicked.connect(self.get_last_image)
        self.btn_next_image.clicked.connect(self.get_next_image)

    def open_input_dialog(self):
        files, filetype = QFileDialog.getOpenFileNames(
            self,
            caption="选择输入文件",
            filter="Image Files (*.bmp *.jpg *.jpeg *.png);;All Files (*)",
        )
        self.lst_files.addItems(files)
        self.lb_input_nums.setText(str(len(files)))

    def open_output_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "选择输出文件夹")
        if directory == "":
            return
        self.output_dir = Path(directory)
        self.lb_output_path.setText(self.output_dir.as_posix())

    def open_selected_file(self, item: QListWidgetItem):
        self.selected_file = Path(item.text())
        if not Path(self.selected_file).exists():
            QMessageBox.warning(self, "警告", "文件不存在！")
            return
        self.lst_files.setCurrentItem(item)
        self.show_image()

    def show_image(self):
        self.image = Image.open(self.selected_file)
        self.image_now = self.image
        self.view.setImage(self.image)

    def set_origin(self):
        self.view.setImage(self.image)

    def set_CLAHE(self):
        dialog = CLAHEDialog(self)
        if dialog.exec() == QDialog.DialogCode.Rejected:
            return
        clipLimit = dialog.CLAHE_clipLimit.value()
        tileGridSize_x = dialog.CLAHE_tileGridSize_x.value()
        tileGridSize_y = dialog.CLAHE_tileGridSize_y.value()
        transform = CLAHETransform(
            clipLimit=clipLimit, tileGridSize=(tileGridSize_x, tileGridSize_y)
        )
        self.image_now = transform(self.image)
        self.view.setImage(self.image_now)
        
    def set_cut(self,checked:bool):
        if not checked:
            self.view.cut_rectangle.setVisible(False)
            return
        if self.output_dir is None or not self.output_dir.exists():
            QMessageBox.warning(self,"警告","输出文件夹不存在！")
            return 
        dialog = CutDialog(self)
        if dialog.exec() == QDialog.DialogCode.Rejected:
            return
        height = dialog.cut_height.value()
        width = dialog.cut_width.value()
        self.view.cut_rectangle.setCutSize(width, height)
        self.view.cut_rectangle.setVisible(True)
        
    def cut_image(self,point:QPointF):
        point = point.toPoint()
        x,y = point.x(),point.y()
        w,h = self.view.cut_rectangle.cut_width,self.view.cut_rectangle.cut_height
        dialog = ConfirmCutDialog()
        image = self.image_now.copy()
        image = image.crop((x-w/2,y-h/2,x+w/2,y+h/2))
        dialog.image.setPixmap(ImageQt.toqpixmap(image))
        save_name = f"{self.selected_file.stem}_{time.strftime('%Y%m%d%H%M%S',time.localtime())}{self.selected_file.suffix}"
        dialog.output_path.setText(save_name)
        if dialog.exec() == QDialog.DialogCode.Rejected:
            return 
        save_name = dialog.output_path.text()
        save_path = self.output_dir / save_name
        image.save(save_path)
        
    def get_last_image(self):
        index_now = self.lst_files.currentRow()
        if index_now == 0:
            return
        item = self.lst_files.item(index_now-1)
        self.open_selected_file(item)

    def get_next_image(self):
        index_now = self.lst_files.currentRow()
        if index_now == self.lst_files.count()-1:
            return
        item = self.lst_files.item(index_now+1)
        self.open_selected_file(item)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessWindow()
    window.show()
    sys.exit(app.exec())
