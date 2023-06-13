import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QLinearGradient
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('User Login')
        self.setWindowIcon(QIcon("Icon.png"))
        self.setGeometry(1200, 300, 700, 700)

        # Create labels, line edits, and buttons
        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')

        # Apply style sheet to customize the look and feel
        def set_default_style(self):
            # Load the external style sheet from file
            with open('login_style.qss', 'r') as file:
                style_sheet = file.read()

            # Apply the style sheet
            self.setStyleSheet(style_sheet)

        # Create a vertical layout and add widgets with spacing
        layout = QVBoxLayout()
        layout.addWidget(self.username_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_edit)
        layout.addSpacing(20)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        # Set the layout and adjust spacing
        container = QWidget()
        container.setLayout(layout)
        layout_wrapper = QVBoxLayout()
        layout_wrapper.addStretch(1)
        layout_wrapper.addWidget(container)
        layout_wrapper.addStretch(1)
#         self.setLayout(layout_wrapper)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = LoginWindow()
#     window.show()
#     sys.exit(app.exec_())
