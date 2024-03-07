# coding:utf-8
# modified from https://www.cnblogs.com/zhiyiYo/p/15676079.html
import sys

from PySide6.QtCore import QRect, QRectF, QSize, Qt, Signal, QPoint, QPointF
from PySide6.QtGui import QMouseEvent, QPainter, QPixmap, QWheelEvent, QPen
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsSceneMouseEvent,
    QGraphicsView,
    QGraphicsRectItem,
)
from PIL import Image, ImageQt


class ImageScene(QGraphicsScene):
    ...


class CutRectangleItem(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.setVisible(False)
        self.setPen(QPen(Qt.red, 2))
        # self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        self.cut_width: int = 100
        self.cut_height: int = 100
        self.setRect(0, 0, self.cut_width, self.cut_height)

    def setCutSize(self, width: int, height: int):
        self.cut_width = width
        self.cut_height = height

    def setCutPoint(self, point: QPointF):
        x, y = point.x(), point.y()
        self.setRect(
            x - self.cut_width / 2,
            y - self.cut_height / 2,
            self.cut_width,
            self.cut_height,
        )


class ImageViewer(QGraphicsView):
    """图片查看器"""
    cut_clicked: Signal = Signal(QPointF)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.zoomInTimes = 0
        self.maxZoomInTimes = 22

        # 创建场景
        self.graphicsScene = ImageScene()

        # 图片
        self.pixmap = QPixmap()
        self.pixmapItem = QGraphicsPixmapItem()
        self.displayedImageSize = QSize(0, 0)
        
        # 鼠标记录
        self.cursorPos = QPointF()

        # 裁剪框
        self.cut_rectangle = CutRectangleItem()

        # 初始化小部件
        self.__initWidget()

    def __initWidget(self):
        # 隐藏滚动条
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 以鼠标所在位置为锚点进行缩放
        self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)

        # 平滑缩放
        self.pixmapItem.setTransformationMode(Qt.SmoothTransformation)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        # 设置场景
        self.setScene(self.graphicsScene)
        self.graphicsScene.addItem(self.pixmapItem)
        self.graphicsScene.addItem(self.cut_rectangle)

    def wheelEvent(self, e: QWheelEvent):
        """滚动鼠标滚轮缩放图片"""
        if e.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def resizeEvent(self, e):
        """缩放图片"""
        super().resizeEvent(e)

        if self.zoomInTimes > 0:
            return

        # 调整图片大小
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size() * ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)
        else:
            self.resetTransform()

    def setImage(self, image: Image.Image):
        """设置显示的图片"""
        self.resetTransform()
        # 刷新图片
        self.pixmap = ImageQt.toqpixmap(image)
        self.pixmapItem.setPixmap(self.pixmap)

        # 调整图片大小
        self.setSceneRect(QRectF(self.pixmap.rect()))
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size() * ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)

    def resetTransform(self):
        """重置变换"""
        super().resetTransform()
        self.zoomInTimes = 0
        self.__setDragEnabled(False)

    def __isEnableDrag(self):
        """根据图片的尺寸决定是否启动拖拽功能"""
        v = self.verticalScrollBar().maximum() > 0
        h = self.horizontalScrollBar().maximum() > 0
        return v or h

    def __setDragEnabled(self, isEnabled: bool):
        """设置拖拽是否启动"""
        self.setDragMode(
            self.DragMode.ScrollHandDrag if isEnabled else self.DragMode.NoDrag
        )

    def __getScaleRatio(self):
        """获取显示的图像和原始图像的缩放比例"""
        if self.pixmap.isNull():
            return 1

        pw = self.pixmap.width()
        ph = self.pixmap.height()
        rw = min(1, self.width() / pw)
        rh = min(1, self.height() / ph)
        return min(rw, rh)

    def fitInView(self, item: QGraphicsItem, mode=Qt.KeepAspectRatio):
        """缩放场景使其适应窗口大小"""
        super().fitInView(item, mode)
        self.displayedImageSize = self.__getScaleRatio() * self.pixmap.size()
        self.zoomInTimes = 0

    def zoomIn(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """放大图像"""
        if self.zoomInTimes == self.maxZoomInTimes:
            return

        self.setTransformationAnchor(viewAnchor)

        self.zoomInTimes += 1
        self.scale(1.1, 1.1)
        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)

    def zoomOut(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """缩小图像"""
        if self.zoomInTimes == 0 and not self.__isEnableDrag():
            return

        self.setTransformationAnchor(viewAnchor)

        self.zoomInTimes -= 1

        # 原始图像的大小
        pw = self.pixmap.width()
        ph = self.pixmap.height()

        # 实际显示的图像宽度
        w = self.displayedImageSize.width() * 1.1**self.zoomInTimes
        h = self.displayedImageSize.height() * 1.1**self.zoomInTimes

        if pw > self.width() or ph > self.height():
            # 在窗口尺寸小于原始图像时禁止继续缩小图像比窗口还小
            if w <= self.width() and h <= self.height():
                self.fitInView(self.pixmapItem)
            else:
                self.scale(1 / 1.1, 1 / 1.1)
        else:
            # 在窗口尺寸大于图像时不允许缩小的比原始图像小
            if w <= pw:
                self.resetTransform()
            else:
                self.scale(1 / 1.1, 1 / 1.1)

        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.cut_rectangle.setCutPoint(self.mapToScene(event.pos()))
        self.cursorPos = self.mapToScene(event.pos())
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            if self.cut_rectangle.isVisible():
                self.cut_clicked.emit(self.mapToScene(event.pos()))
        return super().mousePressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ImageViewer()
    w.show()
    sys.exit(app.exec_())
