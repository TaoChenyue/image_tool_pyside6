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
from process import CLAHETransform, NoTransform, Transform
from confirm_cut_ui import Ui_Dialog as Ui_ConfirmCut
from PIL import Image, ImageQt
import time


class ConfirmCutDialog(QDialog, Ui_ConfirmCut):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        if self.output_path.text() == "":
            QMessageBox.information(self, "提示", "请输入输出路径")
            return
        return super().closeEvent(arg__1)


class ProcessWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.splitter_2.setStretchFactor(1, 5)
        self.splitter.setStretchFactor(1, 5)
        self.tab_transform.setCurrentWidget(self.tbw_size)
        self.tab_size.setCurrentWidget(self.tbw_cut)

        self.output_dir: Path | None = None
        self.image: Image.Image | None = None
        self.image_now: Image.Image | None = None
        self.current_transform: Transform = NoTransform()

        self.btn_input.clicked.connect(self.open_input_dialog)
        self.btn_output.clicked.connect(self.open_output_dialog)
        self.btn_clearfiles.clicked.connect(self.clear_files)
        self.lst_files.itemDoubleClicked.connect(self.open_selected_file)
        self.btn_last_image.clicked.connect(self.get_last_image)
        self.btn_next_image.clicked.connect(self.get_next_image)
        self.btn_origin.clicked.connect(self.set_origin)

        self.slider_rotate.valueChanged.connect(
            lambda x: self.rotate_angle.setText(f"{x-180}°")
        )
        self.slider_rotate.valueChanged.connect(self.set_image)

        self.checkBox_cut.stateChanged.connect(self.set_cut)
        self.cut_height.valueChanged.connect(self.set_cut)
        self.cut_width.valueChanged.connect(self.set_cut)
        self.view.cut_clicked.connect(self.cut_image)

        self.checkBox_CLAHE.stateChanged.connect(self.set_CLAHE)
        self.CLAHE_clip.valueChanged.connect(self.set_CLAHE)
        self.CLAHE_size.valueChanged.connect(self.set_CLAHE)

    def open_input_dialog(self):
        files, filetype = QFileDialog.getOpenFileNames(
            self,
            caption="选择输入文件",
            filter="Image Files (*.bmp *.jpg *.jpeg *.png);;All Files (*)",
        )
        self.lst_files.addItems(files)
        self.update_filesinfo()
        
    def update_filesinfo(self):
        self.lb_input_nums.setText(
            f"{self.lst_files.currentRow()+1}/{self.lst_files.count()}"
        )
        
    def clear_files(self):
        self.lst_files.clear()
        self.update_filesinfo()

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
        self.update_filesinfo()
        self.show_image()

    def apply_rotate(self, image: Image.Image):
        return image.rotate(self.slider_rotate.value()-180)

    def show_image(self):
        self.image = Image.open(self.selected_file)
        self.set_image()

    def set_image(self):
        self.image_now = self.current_transform(self.image)
        self.view.setImage(self.apply_rotate(self.image_now))

    def set_origin(self):
        self.current_transform = NoTransform()
        self.set_image()

    def set_CLAHE(self):
        if not self.checkBox_CLAHE.isChecked():
            self.current_transform = NoTransform()
        else:
            clipLimit = self.CLAHE_clip.value()
            tileGridSize = self.CLAHE_size.value()
            transform = CLAHETransform(
                clipLimit=clipLimit, tileGridSize=(tileGridSize, tileGridSize)
            )
            self.current_transform = transform
        self.set_image()

    def set_cut(self):
        if not self.checkBox_cut.isChecked():
            self.view.cut_rectangle.setVisible(False)
        else:
            self.view.cut_rectangle.setVisible(True)
            height = self.cut_height.value()
            width = self.cut_width.value()
            self.view.cut_rectangle.setCutSize(width, height)

    def cut_image(self):
        if self.output_dir is None or not self.output_dir.exists():
            QMessageBox.warning(self, "警告", "输出文件夹不存在！")
            return
        point = self.view.cursorPos
        point = point.toPoint()
        x, y = point.x(), point.y()
        w, h = self.view.cut_rectangle.cut_width, self.view.cut_rectangle.cut_height
        dialog = ConfirmCutDialog()
        if self.checkBox_cut_origin.isChecked():
            image = self.image.copy()
        else:
            image = self.image_now.copy()
        image = self.apply_rotate(image)
        image = image.crop((x - w / 2, y - h / 2, x + w / 2, y + h / 2))
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
        item = self.lst_files.item(index_now - 1)
        self.open_selected_file(item)

    def get_next_image(self):
        index_now = self.lst_files.currentRow()
        if index_now == self.lst_files.count() - 1:
            return
        item = self.lst_files.item(index_now + 1)
        self.open_selected_file(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessWindow()
    window.show()
    sys.exit(app.exec())
