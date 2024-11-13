

from PySide6.QtWidgets import QCheckBox, QWidget
from PySide6.QtCore import Qt, QRect, QPoint, QEasingCurve, QPropertyAnimation, Property
from PySide6.QtGui import QPainter, QColor
from config import ToggleBgColor, ToggleCircleColor, ToggleActiveColor

class pyToggle(QCheckBox):
    def __init__(
        self,
        width = 50,
        bg_color = f"{ToggleBgColor}",
        circle_color = f"{ToggleCircleColor}",
        active_color = f"{ToggleActiveColor}",
        animation_curve = QEasingCurve.OutBounce
        ):
        QCheckBox.__init__(self)

        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(animation_curve)
        self.stateChanged.connect(self.start_transition)

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self):
        # print(f"State: {self.isChecked()}")
        # print(ToggleBgColor, ToggleCircleColor, ToggleActiveColor)
        self.animation.stop()
        if self.isChecked():
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)
        self.animation.start()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0, rect.width(), self.height(), self.height()/2, self.height()/2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22 , 22)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0,0, rect.width(), self.height(), self.height()/2, self.height()/2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22 , 22)

        p.end()
