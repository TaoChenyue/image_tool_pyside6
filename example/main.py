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
import imgtfs
from confirm_cut_ui import Ui_Dialog as Ui_ConfirmCut
from PIL import Image, ImageQt
import time
import json


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
        self.splitter.setStretchFactor(1, 5)
        self.splitter_2.setStretchFactor(1, 5)

        self.backup = Path("backup.json")
        self.load_filesinfo()

        self.output_dir: Path | None = None
        self.image: Image.Image | None = None
        self.image_now: Image.Image | None = None
        self.current_transform: imgtfs.ImageTransform = imgtfs.ImageTransform()

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
        self.btn_rotate_left.clicked.connect(
            lambda: self.slider_rotate.setValue(self.slider_rotate.value() - 1)
        )
        self.btn_rotate_right.clicked.connect(
            lambda: self.slider_rotate.setValue(self.slider_rotate.value() + 1)
        )

        self.checkBox_cut.stateChanged.connect(self.set_cut)
        self.cut_height.valueChanged.connect(self.set_cut)
        self.cut_width.valueChanged.connect(self.set_cut)
        self.view.cut_clicked.connect(self.cut_image)
        self.cut_whole.clicked.connect(lambda: self.cut_image(None))

        self.checkBox_CLAHE.stateChanged.connect(self.set_CLAHE)
        self.CLAHE_clip.valueChanged.connect(self.set_CLAHE)
        self.CLAHE_size.valueChanged.connect(self.set_CLAHE)

        self.checkBox_HE.stateChanged.connect(self.set_HE)

        self.checkBox_LOG.stateChanged.connect(self.set_LOG)
        self.LOG_v.valueChanged.connect(self.set_LOG)

        self.checkBox_GAMMA.stateChanged.connect(self.set_GAMMA)
        self.GAMMA_c.valueChanged.connect(self.set_GAMMA)
        
        self.checkBox_AutoGamma.stateChanged.connect(self.set_AutoGamma)
        
        self.checkBox_MeanStd.stateChanged.connect(self.set_MeanStd)
        self.MeanStd_mean.valueChanged.connect(self.set_MeanStd)
        self.MeanStd_std.valueChanged.connect(self.set_MeanStd)

    def open_input_dialog(self):
        files, filetype = QFileDialog.getOpenFileNames(
            self,
            caption="选择输入文件",
            filter="Image Files (*.bmp *.jpg *.jpeg *.png);;All Files (*)",
        )
        self.save_filesinfo(files)
        self.lst_files.addItems(files)
        self.update_filesinfo()

    def save_filesinfo(self, files):
        with open(self.backup, "w", encoding="utf-8") as f:
            json.dump(files, f)

    def load_filesinfo(self):
        if self.backup.exists():
            with open(self.backup, "r", encoding="utf-8") as f:
                files = json.load(f)
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
        return image.rotate(self.slider_rotate.value() - 180)

    def show_image(self):
        self.image = Image.open(self.selected_file)
        self.set_image()

    def set_image(self):
        self.image_now = self.current_transform(self.image)
        self.view.setImage(self.apply_rotate(self.image_now))

    def set_origin(self):
        self.current_transform = imgtfs.ImageTransform()
        self.set_image()

    def set_CLAHE(self):
        if not self.checkBox_CLAHE.isChecked():
            self.current_transform = imgtfs.ImageTransform()
        else:
            clipLimit = self.CLAHE_clip.value()
            tileGridSize = self.CLAHE_size.value()
            transform = imgtfs.GrayCLAHETransform(
                clipLimit=clipLimit, tileGridSize=(tileGridSize, tileGridSize)
            )
            self.current_transform = transform
        self.set_image()

    def set_HE(self):
        if not self.checkBox_HE.isChecked():
            self.current_transform = imgtfs.ImageTransform()
        else:
            transform = imgtfs.GrayHETransform()
            self.current_transform = transform
        self.set_image()

    def set_LOG(self):
        if not self.checkBox_LOG.isChecked():
            self.current_transform = imgtfs.ImageTransform()
        else:
            v = self.LOG_v.value()
            transform = imgtfs.GrayLogTransform(value=v)
            self.current_transform = transform
        self.set_image()

    def set_GAMMA(self):
        if not self.checkBox_GAMMA.isChecked():
            self.current_transform = imgtfs.ImageTransform()
        else:
            c = self.GAMMA_c.value()
            transform = imgtfs.GrayGammaTransform(gamma=c)
            self.current_transform = transform
        self.set_image()
        
    def set_AutoGamma(self):
        if not self.checkBox_AutoGamma.isChecked():
            self.current_transform = imgtfs.ImageTransform()
        else:
            transform = imgtfs.GrayGammaAutoTransform()
            self.current_transform = transform
        self.set_image()
        
    def set_MeanStd(self):
        if not self.checkBox_MeanStd.isChecked():
            self.current_transform = imgtfs.ImageTransform()
        else:
            mean = self.MeanStd_mean.value()
            std = self.MeanStd_std.value()
            transform = imgtfs.GrayMeanStdTransform(mean=mean, std=std)
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

    def cut_image(self, point: QPointF | None):
        if self.output_dir is None or not self.output_dir.exists():
            QMessageBox.warning(self, "警告", "输出文件夹不存在！")
            return

        if self.checkBox_cut_origin.isChecked():
            image = self.image.copy()
        else:
            image = self.image_now.copy()
        image = self.apply_rotate(image)
        if point is not None:
            # point = self.view.cursorPos
            point = point.toPoint()
            x, y = point.x(), point.y()
            w, h = self.view.cut_rectangle.cut_width, self.view.cut_rectangle.cut_height
            image = image.crop((x - w / 2, y - h / 2, x + w / 2, y + h / 2))
        dialog = ConfirmCutDialog()
        dialog.image.setPixmap(ImageQt.toqpixmap(image))
        save_name = self.selected_file.name
        if (self.output_dir / save_name).exists():
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
