from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QLabel,
    QTextBrowser,
    QHBoxLayout,
    QFrame,
    QComboBox,
    QLineEdit,
    QTextEdit,
    QMessageBox,
    QListWidget,
    QListWidgetItem,
    QAbstractItemView,
    QDialog,
    QPlainTextEdit,
)
from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QChartView,
    QValueAxis,
)
from PySide6.QtCore import Qt, QSize, QRect, QTimer, QIntValidator
from PySide6.QtGui import QFont, QPixmap, QAction, QIcon, QPainter, QBrush, QColor
from handlers import procs
from config import (
    small_image,
    big_image,
    image_path,
    blockedBuzzerColor,
    pressedBuzzerColor,
    playerColor,
    roundTopColor,
    background_color,
    main_color,
    active_button_color,
    question_color,
    question_bg_color,
    hwindowsize,
    vwindowsize,
    roundPlayoffColor,
)
from py_toggle import pyToggle
import sys
import os

# disable pygame support prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import subprocess
import time
import random

pygame.mixer.init()


class QuestionAdd(QDialog):
    def __init__(self, round_id, parent):
        super().__init__(parent)
        self.setWindowTitle("Add Question")
        self.resize(600, 300)
        self.label = QLabel(self)

        self.MainLayout = QWidget(self)
        self.setGeometry(QRect(20, 20, 760, 760))
        self.VLayout = QVBoxLayout(self.MainLayout)
        self.VLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MainLayout.setLayout(self.VLayout)

        self.LabelQuestionTitle = QLabel()
        self.LabelQuestionTitle.setText("Frage:")
        self.LabelQuestionAnswer = QLabel()
        self.LabelQuestionAnswer.setText("Antwort:")
        self.LabelQuestionRound = QLabel()
        self.LabelQuestionRound.setText("Runde:")
        self.LabelQuestionSeq = QLabel()
        self.LabelQuestionSeq.setText("Sequenz:")
        self.LabelQuestionPlayed = QLabel()
        self.LabelQuestionPlayed.setText("Gespielt:")
        self.LabelQuestionComment = QLabel()
        self.LabelQuestionComment.setText("Kommentar:")
        self.LabelQuestionImage = QLabel()
        self.LabelQuestionImage.setText("Bild:")

        # count Questions in round for default seq value
        countQuestions = procs.count_questions_by_round(round_id)

        self.questionQuestion = QLineEdit()
        self.questionQuestion.setFixedSize(400, 30)
        self.questionQuestion.setText("Frage")
        self.questionAnswer = QLineEdit()
        self.questionAnswer.setFixedSize(400, 30)
        self.questionAnswer.setText("Antwort")
        self.questionRound = QLineEdit()
        self.questionRound.setFixedSize(400, 30)
        self.questionRound.setText(str(round_id))
        self.questionSeq = QLineEdit()
        self.questionSeq.setFixedSize(400, 30)
        self.questionSeq.setText(str(countQuestions + 1))
        self.questionPlayed = QLineEdit()
        self.questionPlayed.setFixedSize(400, 30)
        self.questionPlayed.setText("0")
        self.questionComment = QTextEdit()
        self.questionComment.setFixedSize(400, 200)
        self.questionComment.setTabChangesFocus(True)
        self.questionComment.setText("Kommentar")
        self.questionImage = QLineEdit()
        self.questionImage.setFixedSize(400, 30)
        self.questionImage.setText("standard.jpg")

        self.LineQuestionTitle = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionTitle)
        self.LineQuestionTitle.addWidget(
            self.LabelQuestionTitle, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionTitle.addWidget(self.questionQuestion, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionAnswer = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionAnswer)
        self.LineQuestionAnswer.addWidget(
            self.LabelQuestionAnswer, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionAnswer.addWidget(self.questionAnswer, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionRound = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionRound)
        self.LineQuestionRound.addWidget(
            self.LabelQuestionRound, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionRound.addWidget(self.questionRound, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionSeq = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionSeq)
        self.LineQuestionSeq.addWidget(self.LabelQuestionSeq, 0, Qt.AlignmentFlag.AlignRight)
        self.LineQuestionSeq.addWidget(self.questionSeq, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionPlayed = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionPlayed)
        self.LineQuestionPlayed.addWidget(
            self.LabelQuestionPlayed, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionPlayed.addWidget(self.questionPlayed, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionComment = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionComment)
        self.LineQuestionComment.addWidget(
            self.LabelQuestionComment, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionComment.addWidget(self.questionComment, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionImage = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionImage)
        self.LineQuestionImage.addWidget(
            self.LabelQuestionImage, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionImage.addWidget(self.questionImage, 0, Qt.AlignmentFlag.AlignLeft)

        self.ChangeButton = QPushButton()
        self.ChangeButton.setText("Hinzufügen")
        self.ChangeButton.clicked.connect(lambda: self.AddNewQuestion())
        self.ChangeButton.clicked.connect(self.close)
        self.VLayout.addWidget(self.ChangeButton)
        self.ExitButton = QPushButton()
        self.ExitButton.setText("Schließen")
        self.ExitButton.clicked.connect(self.close)
        self.VLayout.addWidget(self.ExitButton)

        self.VLayout.addWidget(self.label)

    def AddNewQuestion(self):
        procs.add_question_to_database(
            self.questionQuestion.text(),
            self.questionAnswer.text(),
            self.questionRound.text(),
            self.questionSeq.text(),
            self.questionPlayed.text(),
            self.questionComment.toPlainText(),
            self.questionImage.text(),
        )


class QuestionEditor(QDialog):
    def __init__(self, id, parent):
        super().__init__(parent)
        self.setWindowTitle("Frage bearbeiten")
        self.setGeometry(QRect(20, 20, 530, 660))
        self.label = QLabel(self)

        self.MainLayout = QWidget(self)
        self.VLayout = QVBoxLayout(self.MainLayout)
        self.VLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VLayout.setContentsMargins(10, 10, 10, 10)
        self.VLayout.setSpacing(6)
        self.MainLayout.setLayout(self.VLayout)

        questionDetails = procs.get_question_details(id)

        self.LabelQuestionTitle = QLabel()
        self.LabelQuestionTitle.setText("Frage:")
        self.LabelQuestionTitle.setFixedWidth(100)
        self.LabelQuestionAnswer = QLabel()
        self.LabelQuestionAnswer.setText("Antwort:")
        self.LabelQuestionAnswer.setFixedWidth(100)
        self.LabelQuestionRound = QLabel()
        self.LabelQuestionRound.setText("Runde:")
        self.LabelQuestionRound.setFixedWidth(100)
        self.LabelQuestionSeq = QLabel()
        self.LabelQuestionSeq.setText("Sequenz:")
        self.LabelQuestionSeq.setFixedWidth(100)
        self.LabelQuestionPlayed = QLabel()
        self.LabelQuestionPlayed.setText("Gespielt:")
        self.LabelQuestionPlayed.setFixedWidth(100)
        self.LabelQuestionComment = QLabel()
        self.LabelQuestionComment.setText("Kommentar:")
        self.LabelQuestionComment.setFixedWidth(100)
        self.LabelQuestionImage = QLabel()
        self.LabelQuestionImage.setText("Bild:")
        self.LabelQuestionImage.setFixedWidth(100)

        self.questionQuestion = QLineEdit()
        self.questionQuestion.setFixedSize(400, 30)
        self.questionQuestion.setText(questionDetails["question"])
        self.questionAnswer = QLineEdit()
        self.questionAnswer.setFixedSize(400, 30)
        self.questionAnswer.setText(questionDetails["answer"])
        self.questionRound = QLineEdit()
        self.questionRound.setFixedSize(400, 30)
        self.questionRound.setText(str(questionDetails["round"]))
        self.questionSeq = QLineEdit()
        self.questionSeq.setFixedSize(400, 30)
        self.questionSeq.setText(str(questionDetails["seq"]))
        self.questionPlayed = QLineEdit()
        self.questionPlayed.setFixedSize(400, 30)
        self.questionPlayed.setText(str(questionDetails["played"]))
        self.questionComment = QTextEdit()
        self.questionComment.setFixedSize(400, 200)
        self.questionComment.setTabChangesFocus(True)
        self.questionComment.setText(questionDetails["comment"])
        self.questionImage = QLineEdit()
        self.questionImage.setFixedSize(400, 30)
        self.questionImage.setText(questionDetails["image"])

        self.LineQuestionTitle = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionTitle)
        self.LineQuestionTitle.addWidget(
            self.LabelQuestionTitle, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionTitle.addWidget(self.questionQuestion, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionAnswer = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionAnswer)
        self.LineQuestionAnswer.addWidget(
            self.LabelQuestionAnswer, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionAnswer.addWidget(self.questionAnswer, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionRound = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionRound)
        self.LineQuestionRound.addWidget(
            self.LabelQuestionRound, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionRound.addWidget(self.questionRound, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionSeq = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionSeq)
        self.LineQuestionSeq.addWidget(self.LabelQuestionSeq, 0, Qt.AlignmentFlag.AlignRight)
        self.LineQuestionSeq.addWidget(self.questionSeq, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionPlayed = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionPlayed)
        self.LineQuestionPlayed.addWidget(
            self.LabelQuestionPlayed, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionPlayed.addWidget(self.questionPlayed, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionComment = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionComment)
        self.LineQuestionComment.addWidget(
            self.LabelQuestionComment, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionComment.addWidget(self.questionComment, 0, Qt.AlignmentFlag.AlignLeft)

        self.LineQuestionImage = QHBoxLayout()
        self.VLayout.addLayout(self.LineQuestionImage)
        self.LineQuestionImage.addWidget(
            self.LabelQuestionImage, 0, Qt.AlignmentFlag.AlignRight
        )
        self.LineQuestionImage.addWidget(self.questionImage, 0, Qt.AlignmentFlag.AlignLeft)

        self.ChangeButton = QPushButton()
        self.ChangeButton.setText("Ändern/speichern")
        self.ChangeButton.clicked.connect(lambda: self.changeQuestionDetails(id))
        self.VLayout.addWidget(self.ChangeButton)
        self.ExitButton = QPushButton()
        self.ExitButton.setText("Schließen")
        self.ExitButton.clicked.connect(self.close)
        self.VLayout.addWidget(self.ExitButton)

        self.VLayout.addWidget(self.label)

    def changeQuestionDetails(self, id):
        procs.change_question_details(
            id,
            self.questionQuestion.text(),
            self.questionAnswer.text(),
            self.questionRound.text(),
            self.questionSeq.text(),
            self.questionPlayed.text(),
            self.questionComment.toPlainText(),
            self.questionImage.text(),
        )


class QuestionsWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QuestionsWindow, self).__init__(parent)
        self.setWindowTitle("Fragen")
        self.setGeometry(100, 100, 800, 800)

        round_1_name = procs.get_round_name(1)
        round_2_name = procs.get_round_name(2)
        round_3_name = procs.get_round_name(3)
        round_4_name = procs.get_round_name(4)
        round_5_name = procs.get_round_name(5)
        round_6_name = procs.get_round_name(6)
        round_7_name = procs.get_round_name(7)

        self.FontTop = QFont()
        self.FontTop.setPointSize(40)
        self.FontTop.setBold(True)

        self.MainLayout = QWidget(self)
        self.MainLayout.setObjectName("MainLayout")
        self.MainLayout.setGeometry(QRect(20, 20, 760, 760))

        self.VLayoutQuestions = QVBoxLayout(self.MainLayout)
        self.VLayoutQuestions.setContentsMargins(10, 10, 10, 10)
        self.VLayoutQuestions.setSpacing(6)
        self.VLayoutQuestions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MainLayout.setLayout(self.VLayoutQuestions)

        self.HLayoutMenu = QHBoxLayout()

        self.QuestionEditRoundId = 0
        self.pBQuestionsRound1 = QPushButton()
        self.pBQuestionsRound1.setText(round_1_name)
        self.pBQuestionsRound1.clicked.connect(lambda: self.GetQuestions(1))
        self.pBQuestionsRound1.clicked.connect(lambda: setMyRoundId(1))
        self.pBQuestionsRound1.clicked.connect(lambda: self.DeactivateButton(self.pBQuestionsRound1))
        self.HLayoutMenu.addWidget(self.pBQuestionsRound1)
        self.pBQuestionsRound2 = QPushButton()
        self.pBQuestionsRound2.setText(round_2_name)
        self.pBQuestionsRound2.clicked.connect(lambda: self.GetQuestions(2))
        self.pBQuestionsRound2.clicked.connect(lambda: setMyRoundId(2))
        self.pBQuestionsRound2.clicked.connect(lambda: self.DeactivateButton(self.pBQuestionsRound2))
        self.HLayoutMenu.addWidget(self.pBQuestionsRound2)
        self.pBQuestionsRound3 = QPushButton()
        self.pBQuestionsRound3.setText(round_3_name)
        self.pBQuestionsRound3.clicked.connect(lambda: self.GetQuestions(3))
        self.pBQuestionsRound3.clicked.connect(lambda: setMyRoundId(3))
        self.pBQuestionsRound3.clicked.connect(lambda: self.DeactivateButton(self.pBQuestionsRound3))
        self.HLayoutMenu.addWidget(self.pBQuestionsRound3)
        self.pBQuestionsRound4 = QPushButton()
        self.pBQuestionsRound4.setText(round_4_name)
        self.pBQuestionsRound4.clicked.connect(lambda: self.GetQuestions(4))
        self.pBQuestionsRound4.clicked.connect(lambda: setMyRoundId(4))
        self.pBQuestionsRound4.clicked.connect(lambda: self.DeactivateButton(self.pBQuestionsRound4))
        self.HLayoutMenu.addWidget(self.pBQuestionsRound4)
        self.pBQuestionsRound5 = QPushButton()
        self.pBQuestionsRound5.setText(round_5_name)
        self.pBQuestionsRound5.clicked.connect(lambda: self.GetQuestions(5))
        self.pBQuestionsRound5.clicked.connect(lambda: setMyRoundId(5))
        self.pBQuestionsRound5.clicked.connect(lambda: self.DeactivateButton(self.pBQuestionsRound5))
        self.HLayoutMenu.addWidget(self.pBQuestionsRound5)
        self.pBQuestionsRound6 = QPushButton()
        self.pBQuestionsRound6.setText(round_6_name)
        self.pBQuestionsRound6.clicked.connect(lambda: self.GetQuestions(6))
        self.pBQuestionsRound6.clicked.connect(lambda: setMyRoundId(6))
        self.pBQuestionsRound6.clicked.connect(lambda: self.DeactivateButton(self.pBQuestionsRound6))
        self.HLayoutMenu.addWidget(self.pBQuestionsRound6)
        self.pBQuestionsRound7 = QPushButton()
        self.pBQuestionsRound7.setText(round_7_name)
        self.pBQuestionsRound7.clicked.connect(lambda: self.GetQuestions(7))
        self.pBQuestionsRound7.clicked.connect(lambda: setMyRoundId(7))
        self.pBQuestionsRound7.clicked.connect(lambda: self.DeactivateButton(self.pBQuestionsRound7))
        self.HLayoutMenu.addWidget(self.pBQuestionsRound7)

        def setMyRoundId(round_id):
            # print(f"setMyRoundId: {round_id}")
            self.QuestionEditRoundId = round_id

        # print(f"QuestionEditRoundId: {self.QuestionEditRoundId}")

        self.TopTitle = QLabel()
        self.TopTitle.setText("Questions")
        self.TopTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TopTitle.setFont(self.FontTop)

        self.VLayoutQuestions.addWidget(self.TopTitle)

        self.MainLayout = QWidget(self)
        self.MainLayout.setObjectName("MainLayout")

        self.QuestionList = QListWidget(self.MainLayout)
        self.QuestionList.setAlternatingRowColors(True)
        self.QuestionList.setDragDropMode(QAbstractItemView.InternalMove)

        self.QuestionList.itemDoubleClicked.connect(
            lambda: self.EditQuestion(self.QuestionList.currentItem())
        )

        self.VLayoutQuestions.addLayout(self.HLayoutMenu)
        self.VLayoutQuestions.addWidget(self.QuestionList)

        self.HLayoutMaximumValues = QHBoxLayout()
        self.HLayoutMaximumValues.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelMaxQuestions = QLabel()
        self.LabelMaxQuestions.setText("Maximale Fragen:")
        self.LabelMaxQuestions.setFixedWidth(150)
        self.MaxQuestions = QLineEdit()
        self.MaxQuestions.setFixedWidth(50)
        self.MaxQuestions.setText("15")
        self.MaxQuestions.setMaxLength(2)
        self.MaxQuestions.setValidator(QIntValidator(0, 99))
        self.MaxQuestions.setFixedWidth(50)
        self.MaxQuestionsButton = QPushButton()
        self.MaxQuestionsButton.setText("Speichern")
        self.MaxQuestionsButton.setFixedWidth(100)
        self.MaxQuestionsButton.clicked.connect(lambda: procs.set_round_max_questions(self.QuestionEditRoundId, self.MaxQuestions.text()))
        self.HLayoutMaximumValues.addWidget(self.LabelMaxQuestions)
        self.HLayoutMaximumValues.addWidget(self.MaxQuestions)
        self.HLayoutMaximumValues.addWidget(self.MaxQuestionsButton)
        
        
        self.VLayoutQuestions.addLayout(self.HLayoutMaximumValues)


        self.HLayoutButtons = QHBoxLayout()
        self.VLayoutQuestions.addLayout(self.HLayoutButtons)

        self.AddQuestionButton = QPushButton()
        self.AddQuestionButton.setFixedSize(180, 30)
        self.AddQuestionButton.setText("Frage hinzufügen")
        self.AddQuestionButton.clicked.connect(lambda: self.AddQuestion(self.QuestionEditRoundId))
        self.RemoveQuestionButton = QPushButton()
        self.RemoveQuestionButton.setFixedSize(180, 30)
        self.RemoveQuestionButton.setText("Frage löschen")
        self.RemoveQuestionButton.clicked.connect(self.RemoveQuestion)
        self.RemoveQuestionButton.clicked.connect(
            lambda: self.GetQuestions(self.QuestionEditRoundId)
        )
        self.ChangeOrderButton = QPushButton()
        self.ChangeOrderButton.setFixedSize(180, 30)
        self.ChangeOrderButton.setText("Reihenfolge speichern")
        self.ChangeOrderButton.clicked.connect(self.SaveChangedOrder)
        self.ChangeOrderButton.clicked.connect(
            lambda: self.GetQuestions(self.QuestionEditRoundId)
        )
        self.ExitButton = QPushButton()
        self.ExitButton.setFixedSize(180, 30)
        self.ExitButton.setText("Schließen")
        self.ExitButton.clicked.connect(self.closeQuestionsWindow)
        self.HLayoutButtons.addWidget(self.AddQuestionButton)
        self.HLayoutButtons.addWidget(self.RemoveQuestionButton)
        self.HLayoutButtons.addWidget(self.ChangeOrderButton)
        self.HLayoutButtons.addWidget(self.ExitButton)

        self.QuestionEditRoundId = 1

        self.GetQuestions(self.QuestionEditRoundId)
        self.DeactivateButton(self.pBQuestionsRound1)

    def GetQuestions(self, round_id):
        print(f"----- GET QUESTIONS ROUND {round_id} -----")
        maxQuestions = procs.get_round_maximum_questions(round_id)
        self.MaxQuestions.setText(str(maxQuestions))
        self.QuestionList.clear()
        questions = procs.get_questions_for_round(round_id)
        for xquestion in questions:
            item = QListWidgetItem()
            id = xquestion[0]
            seq = xquestion[1]
            question = xquestion[2]
            answer = xquestion[3]
            questionName = "".join(
                [str(seq), " - ", question, " - ", answer]
            )
            # for debug:
            # print(questionName)
            item.setText(questionName)
            item.setData(Qt.UserRole, xquestion[0])
            self.QuestionList.addItem(item)

    def RemoveQuestion(self):
        print("----- REMOVE QUESTION -----")
        listItems = self.QuestionList.selectedItems()
        if not listItems:
            return
        for item in listItems:
            self.QuestionList.takeItem(self.QuestionList.row(item))
            # print(f"removed question: ID {item.data(Qt.UserRole)}")
            procs.remove_question_from_database(item.data(Qt.UserRole))

    def SaveChangedOrder(self):
        print("----- SAVED CHANGED ORDER -----")
        for i in range(self.QuestionList.count()):
            item = self.QuestionList.item(i)
            seq = i + 1
            # print(f"changed question sequence: ID {item.data(Qt.UserRole)} - SEQ {seq}")
            procs.change_question_seq(item.data(Qt.UserRole), seq)

    def EditQuestion(self, item):
        QuestionId = item.data(Qt.UserRole)
        print(f"----- EDIT QUESTION {QuestionId} -----")
        pop = QuestionEditor(QuestionId, self)
        pop.show()

    def AddQuestion(self, round_id):
        pop = QuestionAdd(round_id, self)
        pop.show()

    def DeactivateButton(self, button):
        #enable all buttons:
        self.pBQuestionsRound1.setDisabled(False)
        self.pBQuestionsRound2.setDisabled(False)
        self.pBQuestionsRound3.setDisabled(False)
        self.pBQuestionsRound4.setDisabled(False)
        self.pBQuestionsRound5.setDisabled(False)
        self.pBQuestionsRound6.setDisabled(False)
        self.pBQuestionsRound7.setDisabled(False)
        button.setDisabled(True)


    def closeQuestionsWindow(self):
        print("----- CLOSE QUESTIONS WINDOW -----")
        self.close()


class SettingsWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setWindowTitle("Statistik")
        self.setGeometry(100, 100, 800, 600)
        play_mode = procs.get_play_mode()

        self.FontTop = QFont()
        self.FontTop.setPointSize(40)
        self.FontTop.setBold(True)

        self.MainLayout = QWidget(self)
        self.MainLayout.setObjectName("MainLayout")
        self.MainLayout.setGeometry(QRect(20, 20, 760, 560))

        self.VLayoutStatistics = QVBoxLayout(self.MainLayout)
        self.VLayoutStatistics.setContentsMargins(10, 10, 10, 10)
        self.VLayoutStatistics.setSpacing(6)
        self.VLayoutStatistics.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MainLayout.setLayout(self.VLayoutStatistics)

        self.TopTitle = QLabel()
        self.TopTitle.setText("Einstellungen")
        self.TopTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TopTitle.setFont(self.FontTop)

        self.PlaymodeLayout = QHBoxLayout()

        self.PlaymodeToggle = pyToggle()
        self.PlayModeText = QLabel()
        self.PlayModeText.setText("Playoff-Mode")
        if play_mode == "2":
            self.PlaymodeToggle.setChecked(True)
        else:
            self.PlaymodeToggle.setChecked(False)
        self.PlaymodeToggle.stateChanged.connect(self.togglePlaymode)

        self.PlaymodeLayout.addWidget(self.PlayModeText, 0, Qt.AlignmentFlag.AlignLeft)
        self.PlaymodeLayout.addWidget(
            self.PlaymodeToggle, 0, Qt.AlignmentFlag.AlignRight
        )

        self.PlayModeWarning = QLabel()
        self.PlayModeWarning.setText(
            "\nAchtung: Bei Änderung des Play-Off-Modus\nwerden alle Spielergebnisse zurückgesetzt!\n"
        )


        self.FakeNamesButton = QPushButton()
        self.FakeNamesButton.setText("Namen generieren")
        self.FakeNamesButton.clicked.connect(self.GenerateFakeNames)


        self.ResetButton = QPushButton()
        self.ResetButton.setText("Spiel zurücksetzen")
        self.ResetButton.clicked.connect(self.resetGame)

        self.ExitButton = QPushButton()
        self.ExitButton.setText("Schließen")
        self.ExitButton.clicked.connect(self.closeNewWindow)

        self.VLayoutStatistics.addWidget(self.TopTitle)
        self.VLayoutStatistics.addLayout(self.PlaymodeLayout)
        self.VLayoutStatistics.addWidget(
            self.PlayModeWarning, 0, Qt.AlignmentFlag.AlignCenter
        )
        self.VLayoutStatistics.addWidget(self.FakeNamesButton)
        self.VLayoutStatistics.addWidget(self.ResetButton)
        self.VLayoutStatistics.addWidget(self.ExitButton)

    def togglePlaymode(self):
        print("Toggle Playmode")
        if self.PlaymodeToggle.isChecked():
            print("Playoff-Mode aktiviert")
            procs.change_play_mode_silent(2)
            dlgEnd = QMessageBox(self)
            dlgEnd.setWindowTitle("Playoff-Mode aktiviert!")
            dlgEnd.setText("Playoff-Mode wurde aktiviert!\nAlle Spielstände wurden zurückgesetzt!")
            dlgEnd.setIcon(QMessageBox.Information)
            dlgEnd.setStandardButtons(QMessageBox.Ok)
            dlgEnd.exec()
        else:
            print("Playoff-Mode deaktiviert")
            procs.change_play_mode_silent(1)
            dlgEnd = QMessageBox(self)
            dlgEnd.setWindowTitle("Playoff-Mode deaktiviert!")
            dlgEnd.setText("Playoff-Mode wurde deaktiviert!\nAlle Spielstände wurden zurückgesetzt!")
            dlgEnd.setIcon(QMessageBox.Information)
            dlgEnd.setStandardButtons(QMessageBox.Ok)
            dlgEnd.exec()

    def GenerateFakeNames(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Namen generieren!")
        dlg.setText("Sollen wirklich Fake-Namen generiert werden?\nAlle Spielstände werden dabei zurückgesetzt!")
        dlg.setIcon(QMessageBox.Question)
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            print("----- GENERATE FAKE NAMES -----")
            procs.generate_fake_names()
            procs.reset_player_points_silent()
            procs.set_play_round_by_round_id(1)
            dlgEnd = QMessageBox(self)
            dlgEnd.setWindowTitle("Fake Namen gespeichert!")
            dlgEnd.setText("Fake Namen wurden generiert und gespeichert!")
            dlgEnd.setIcon(QMessageBox.Information)
            dlgEnd.setStandardButtons(QMessageBox.Ok)
            dlgEnd.exec()
        else:
            print("----- CANCELD GENERATE FAKE NAMES -----")

    def resetGame(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Spiel zurücksetzen!")
        dlg.setText("Soll das Spiel wirklich zurückgesetzt werden?")
        dlg.setIcon(QMessageBox.Question)
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            print("----- RESET GAME -----")
            procs.reset_player_points_silent()
            procs.set_play_round_by_round_id(1)
            dlgEnd = QMessageBox(self)
            dlgEnd.setWindowTitle("Spiel zurückgesetzt!")
            dlgEnd.setText("Alle Spielstände wurden zurückgesetzt!")
            dlgEnd.setIcon(QMessageBox.Information)
            dlgEnd.setStandardButtons(QMessageBox.Ok)
            dlgEnd.exec()
        else:
            print("----- CANCELD RESET GAME -----")

    def closeNewWindow(self):
        print("----- CLOSE SETTINGS WINDOW -----")
        self.close()


class TournamentWindow(QMainWindow):
    def __init__(self, parent=None):
        super(TournamentWindow, self).__init__(parent)
        self.setWindowTitle("Turnier")
        self.setGeometry(100, 100, 800, 600)

        self.FontTop = QFont()
        self.FontTop.setPointSize(40)
        # self.FontTop.setFamily("Verdana")
        self.FontTop.setBold(True)

        self.FontWinner = QFont()
        self.FontWinner.setPointSize(18)
        self.FontWinner.setBold(True)
        self.font1 = QFont()
        self.font1.setPointSize(11)
        self.font1.setBold(True)

        play_mode = procs.get_play_mode()
        if play_mode == "2":
            procs.get_play_off_players_to_round()
        round_name_1 = procs.get_round_name(1)
        round_name_2 = procs.get_round_name(2)
        round_name_3 = procs.get_round_name(3)
        round_name_4 = procs.get_round_name(4)
        round_name_5 = procs.get_round_name(5)
        round_name_6 = procs.get_round_name(6)
        round_name_7 = procs.get_round_name(7)
        ranks1 = procs.round_ranking(1)
        keys1 = list(ranks1.keys())
        ranks2 = procs.round_ranking(2)
        keys2 = list(ranks2.keys())
        ranks3 = procs.round_ranking(3)
        keys3 = list(ranks3.keys())
        ranks4 = procs.round_ranking(4)
        keys4 = list(ranks4.keys())
        ranks5 = procs.round_ranking(5)
        keys5 = list(ranks5.keys())
        ranks6 = procs.round_ranking(6)
        keys6 = list(ranks6.keys())
        ranks7 = procs.round_ranking(7)
        keys7 = list(ranks7.keys())

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 760, 560))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopLabel = QLabel(self.verticalLayoutWidget)
        self.TopLabel.setObjectName("TopLabel")
        self.TopLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TopLabel.setFont(self.FontTop)

        self.verticalLayout.addWidget(self.TopLabel)

        self.HLine1 = QFrame(self.verticalLayoutWidget)
        self.HLine1.setFrameShape(QFrame.Shape.HLine)
        self.HLine1.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout.addWidget(self.HLine1)

        self.HLVorrunde = QHBoxLayout()

        self.TableRound1 = QVBoxLayout()
        self.TopRound1 = QLabel(self.verticalLayoutWidget)
        font = QFont()
        font.setPointSize(14)
        self.TopRound1.setFont(font)
        self.TopRound1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableRound1.addWidget(self.TopRound1)
        self.TopRound1.setFixedWidth(150)

        self.lineRound1 = QFrame(self.verticalLayoutWidget)
        self.lineRound1.setFrameShape(QFrame.Shape.HLine)
        self.lineRound1.setFrameShadow(QFrame.Shadow.Sunken)
        # self.lineRound1.setStyleSheet(f"background-color: {roundTopColor}")

        self.TableRound1.addWidget(self.lineRound1)
        self.lineRound1.setFixedWidth(150)

        self.HLRound1 = QHBoxLayout()
        self.Round1Names = QVBoxLayout()
        self.Round1Player1 = QLabel(self.verticalLayoutWidget)
        self.Round1Player1.setFont(self.font1)
        self.Round1Player1.setStyleSheet(f"color: {roundTopColor}")
        self.Round1Names.addWidget(self.Round1Player1)
        self.Round1Player1.setFixedWidth(120)

        self.Round1Player2 = QLabel(self.verticalLayoutWidget)
        self.Round1Player2.setFont(self.font1)
        self.Round1Player2.setStyleSheet(f"color: {roundTopColor}")
        self.Round1Names.addWidget(self.Round1Player2)
        self.Round1Player2.setFixedWidth(120)

        self.Round1Player3 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round1Player3.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round1Names.addWidget(self.Round1Player3)
        self.Round1Player3.setFixedWidth(120)

        self.Round1Player4 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round1Player4.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round1Names.addWidget(self.Round1Player4)
        self.Round1Player4.setFixedWidth(120)

        self.HLRound1.addLayout(self.Round1Names)

        self.Round1Score = QVBoxLayout()
        self.Round1ScorePlayer1 = QLabel(self.verticalLayoutWidget)
        self.Round1ScorePlayer1.setFont(self.font1)
        self.Round1ScorePlayer1.setStyleSheet(f"color: {roundTopColor}")
        self.Round1ScorePlayer1.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round1Score.addWidget(self.Round1ScorePlayer1)
        self.Round1ScorePlayer1.setFixedWidth(30)

        self.Round1ScorePlayer2 = QLabel(self.verticalLayoutWidget)
        self.Round1ScorePlayer2.setFont(self.font1)
        self.Round1ScorePlayer2.setStyleSheet(f"color: {roundTopColor}")
        self.Round1ScorePlayer2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round1Score.addWidget(self.Round1ScorePlayer2)
        self.Round1ScorePlayer2.setFixedWidth(30)

        self.Round1ScorePlayer3 = QLabel(self.verticalLayoutWidget)
        self.Round1ScorePlayer3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        if play_mode == "2":
            self.Round1ScorePlayer3.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round1Score.addWidget(self.Round1ScorePlayer3)
        self.Round1ScorePlayer3.setFixedWidth(30)

        self.Round1ScorePlayer4 = QLabel(self.verticalLayoutWidget)
        self.Round1ScorePlayer4.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        if play_mode == "2":
            self.Round1ScorePlayer4.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round1Score.addWidget(self.Round1ScorePlayer4)
        self.Round1ScorePlayer4.setFixedWidth(30)

        self.HLRound1.addLayout(self.Round1Score)

        self.TableRound1.addLayout(self.HLRound1)

        self.HLVorrunde.addLayout(self.TableRound1)

        self.line_8 = QFrame(self.verticalLayoutWidget)
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.HLVorrunde.addWidget(self.line_8)

        self.TableRound2 = QVBoxLayout()
        self.TopRound2 = QLabel(self.verticalLayoutWidget)
        self.TopRound2.setFont(font)
        self.TopRound2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableRound2.addWidget(self.TopRound2)
        self.TopRound2.setFixedWidth(150)

        self.lineRound2 = QFrame(self.verticalLayoutWidget)
        self.lineRound2.setFrameShape(QFrame.Shape.HLine)
        self.lineRound2.setFrameShadow(QFrame.Shadow.Sunken)
        self.TableRound2.addWidget(self.lineRound2)
        self.lineRound2.setFixedWidth(150)

        self.HLRound2 = QHBoxLayout()
        self.Round2Names = QVBoxLayout()
        self.Round2Player1 = QLabel(self.verticalLayoutWidget)
        self.Round2Player1.setFont(self.font1)
        self.Round2Player1.setStyleSheet(f"color: {roundTopColor}")
        self.Round2Names.addWidget(self.Round2Player1)
        self.Round2Player1.setFixedWidth(120)

        self.Round2Player2 = QLabel(self.verticalLayoutWidget)
        self.Round2Player2.setFont(self.font1)
        self.Round2Player2.setStyleSheet(f"color: {roundTopColor}")
        self.Round2Names.addWidget(self.Round2Player2)
        self.Round2Player2.setFixedWidth(120)

        self.Round2Player3 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round2Player3.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round2Names.addWidget(self.Round2Player3)
        self.Round2Player3.setFixedWidth(120)

        self.Round2Player4 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round2Player4.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round2Names.addWidget(self.Round2Player4)
        self.Round2Player4.setFixedWidth(120)

        self.HLRound2.addLayout(self.Round2Names)

        self.Round2Score = QVBoxLayout()
        self.Round2ScorePlayer1 = QLabel(self.verticalLayoutWidget)
        self.Round2ScorePlayer1.setFont(self.font1)
        self.Round2ScorePlayer1.setStyleSheet(f"color: {roundTopColor}")
        self.Round2ScorePlayer1.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round2Score.addWidget(self.Round2ScorePlayer1)
        self.Round2ScorePlayer1.setFixedWidth(30)

        self.Round2ScorePlayer2 = QLabel(self.verticalLayoutWidget)
        self.Round2ScorePlayer2.setFont(self.font1)
        self.Round2ScorePlayer2.setStyleSheet(f"color: {roundTopColor}")
        self.Round2ScorePlayer2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round2Score.addWidget(self.Round2ScorePlayer2)
        self.Round2ScorePlayer2.setFixedWidth(30)

        self.Round2ScorePlayer3 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round2ScorePlayer3.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round2ScorePlayer3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round2Score.addWidget(self.Round2ScorePlayer3)
        self.Round2ScorePlayer3.setFixedWidth(30)

        self.Round2ScorePlayer4 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round2ScorePlayer4.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round2ScorePlayer4.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round2Score.addWidget(self.Round2ScorePlayer4)
        self.Round2ScorePlayer4.setFixedWidth(30)

        self.HLRound2.addLayout(self.Round2Score)
        self.TableRound2.addLayout(self.HLRound2)
        self.HLVorrunde.addLayout(self.TableRound2)

        self.line_9 = QFrame(self.verticalLayoutWidget)
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.HLVorrunde.addWidget(self.line_9)

        self.TableRound3 = QVBoxLayout()
        self.TopRound3 = QLabel(self.verticalLayoutWidget)
        self.TopRound3.setFont(font)
        self.TopRound3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableRound3.addWidget(self.TopRound3)
        self.TopRound3.setFixedWidth(150)

        self.lineRound3 = QFrame(self.verticalLayoutWidget)
        self.lineRound3.setFrameShape(QFrame.Shape.HLine)
        self.lineRound3.setFrameShadow(QFrame.Shadow.Sunken)
        self.TableRound3.addWidget(self.lineRound3)
        self.lineRound3.setFixedWidth(150)

        self.HLRound3 = QHBoxLayout()
        self.Round3Names = QVBoxLayout()
        self.Round3Player1 = QLabel(self.verticalLayoutWidget)
        self.Round3Player1.setFont(self.font1)
        self.Round3Player1.setStyleSheet(f"color: {roundTopColor}")
        self.Round3Names.addWidget(self.Round3Player1)
        self.Round3Player1.setFixedWidth(120)

        self.Round3Player2 = QLabel(self.verticalLayoutWidget)
        self.Round3Player2.setFont(self.font1)
        self.Round3Player2.setStyleSheet(f"color: {roundTopColor}")
        self.Round3Names.addWidget(self.Round3Player2)
        self.Round3Player2.setFixedWidth(120)

        self.Round3Player3 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round3Player3.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round3Names.addWidget(self.Round3Player3)
        self.Round3Player3.setFixedWidth(120)

        self.Round3Player4 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round3Player4.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round3Names.addWidget(self.Round3Player4)
        self.Round3Player4.setFixedWidth(120)

        self.HLRound3.addLayout(self.Round3Names)

        self.Round3Score = QVBoxLayout()
        self.Round3ScorePlayer1 = QLabel(self.verticalLayoutWidget)
        self.Round3ScorePlayer1.setFont(self.font1)
        self.Round3ScorePlayer1.setStyleSheet(f"color: {roundTopColor}")
        self.Round3ScorePlayer1.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round3Score.addWidget(self.Round3ScorePlayer1)
        self.Round3ScorePlayer1.setFixedWidth(30)

        self.Round3ScorePlayer2 = QLabel(self.verticalLayoutWidget)
        self.Round3ScorePlayer2.setFont(self.font1)
        self.Round3ScorePlayer2.setStyleSheet(f"color: {roundTopColor}")
        self.Round3ScorePlayer2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round3Score.addWidget(self.Round3ScorePlayer2)
        self.Round3ScorePlayer2.setFixedWidth(30)

        self.Round3ScorePlayer3 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round3ScorePlayer3.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round3ScorePlayer3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round3Score.addWidget(self.Round3ScorePlayer3)
        self.Round3ScorePlayer3.setFixedWidth(30)

        self.Round3ScorePlayer4 = QLabel(self.verticalLayoutWidget)
        if play_mode == "2":
            self.Round3ScorePlayer4.setStyleSheet(f"color: {roundPlayoffColor}")
        self.Round3ScorePlayer4.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round3Score.addWidget(self.Round3ScorePlayer4)
        self.Round3ScorePlayer4.setFixedWidth(30)

        self.HLRound3.addLayout(self.Round3Score)
        self.TableRound3.addLayout(self.HLRound3)
        self.HLVorrunde.addLayout(self.TableRound3)

        self.line_10 = QFrame(self.verticalLayoutWidget)
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.HLVorrunde.addWidget(self.line_10)

        self.TableRound4 = QVBoxLayout()
        self.TopRound4 = QLabel(self.verticalLayoutWidget)
        self.TopRound4.setFont(font)
        self.TopRound4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableRound4.addWidget(self.TopRound4)
        self.TopRound4.setFixedWidth(150)

        self.lineRound4 = QFrame(self.verticalLayoutWidget)
        self.lineRound4.setFrameShape(QFrame.Shape.HLine)
        self.lineRound4.setFrameShadow(QFrame.Shadow.Sunken)
        self.TableRound4.addWidget(self.lineRound4)
        self.lineRound4.setFixedWidth(150)

        self.HLRound4 = QHBoxLayout()
        self.Round4Names = QVBoxLayout()
        self.Round4Player1 = QLabel(self.verticalLayoutWidget)
        self.Round4Player1.setFont(self.font1)
        self.Round4Player1.setStyleSheet(f"color: {roundTopColor}")
        self.Round4Names.addWidget(self.Round4Player1)
        self.Round4Player1.setFixedWidth(120)

        self.Round4Player2 = QLabel(self.verticalLayoutWidget)
        self.Round4Player2.setFont(self.font1)
        self.Round4Player2.setStyleSheet(f"color: {roundTopColor}")
        self.Round4Names.addWidget(self.Round4Player2)
        self.Round4Player2.setFixedWidth(120)

        self.Round4Player3 = QLabel(self.verticalLayoutWidget)
        self.Round4Names.addWidget(self.Round4Player3)
        self.Round4Player3.setFixedWidth(120)

        self.Round4Player4 = QLabel(self.verticalLayoutWidget)
        self.Round4Names.addWidget(self.Round4Player4)
        self.Round4Player4.setFixedWidth(120)

        self.HLRound4.addLayout(self.Round4Names)

        self.Round4Score = QVBoxLayout()
        self.Round4ScorePlayer1 = QLabel(self.verticalLayoutWidget)
        self.Round4ScorePlayer1.setFont(self.font1)
        self.Round4ScorePlayer1.setStyleSheet(f"color: {roundTopColor}")
        self.Round4ScorePlayer1.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round4Score.addWidget(self.Round4ScorePlayer1)
        self.Round4ScorePlayer1.setFixedWidth(30)

        self.Round4ScorePlayer2 = QLabel(self.verticalLayoutWidget)
        self.Round4ScorePlayer2.setFont(self.font1)
        self.Round4ScorePlayer2.setStyleSheet(f"color: {roundTopColor}")
        self.Round4ScorePlayer2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round4Score.addWidget(self.Round4ScorePlayer2)
        self.Round4ScorePlayer2.setFixedWidth(30)

        self.Round4ScorePlayer3 = QLabel(self.verticalLayoutWidget)
        self.Round4ScorePlayer3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round4Score.addWidget(self.Round4ScorePlayer3)
        self.Round4ScorePlayer3.setFixedWidth(30)

        self.Round4ScorePlayer4 = QLabel(self.verticalLayoutWidget)
        self.Round4ScorePlayer4.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round4Score.addWidget(self.Round4ScorePlayer4)
        self.Round4ScorePlayer4.setFixedWidth(30)

        self.HLRound4.addLayout(self.Round4Score)
        self.TableRound4.addLayout(self.HLRound4)
        self.HLVorrunde.addLayout(self.TableRound4)
        self.verticalLayout.addLayout(self.HLVorrunde)

        if play_mode == "2":
            self.PlayoffMessage = QLabel()
            self.PlayoffMessage.setText(
                "* Die besten 4 von 6 qualifiziert für das Playoff"
            )
            self.PlayoffMessage.setStyleSheet(f"color: {roundPlayoffColor}")
            self.PlayoffMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.verticalLayout.addWidget(self.PlayoffMessage)
            self.PlayoffMessage.setFixedHeight(30)

        self.HLine2 = QFrame(self.verticalLayoutWidget)
        self.HLine2.setFrameShape(QFrame.Shape.HLine)
        self.HLine2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.HLine2)

        self.HLHalbFinale = QHBoxLayout()
        self.TableRound5 = QVBoxLayout()
        self.TopRound5 = QLabel(self.verticalLayoutWidget)
        self.TopRound5.setFont(font)
        self.TopRound5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableRound5.addWidget(self.TopRound5)
        self.TopRound5.setFixedWidth(150)

        self.lineRound5 = QFrame(self.verticalLayoutWidget)
        self.lineRound5.setFrameShape(QFrame.Shape.HLine)
        self.lineRound5.setFrameShadow(QFrame.Shadow.Sunken)
        self.TableRound5.addWidget(self.lineRound5)
        self.lineRound5.setFixedWidth(150)

        self.HLRound5 = QHBoxLayout()
        self.Round5Names = QVBoxLayout()
        self.Round5Player1 = QLabel(self.verticalLayoutWidget)
        self.Round5Player1.setFont(self.font1)
        self.Round5Player1.setStyleSheet(f"color: {roundTopColor}")
        self.Round5Names.addWidget(self.Round5Player1)
        self.Round5Player1.setFixedWidth(120)

        self.Round5Player2 = QLabel(self.verticalLayoutWidget)
        self.Round5Player2.setFont(self.font1)
        self.Round5Player2.setStyleSheet(f"color: {roundTopColor}")
        self.Round5Names.addWidget(self.Round5Player2)
        self.Round5Player2.setFixedWidth(120)

        self.Round5Player3 = QLabel(self.verticalLayoutWidget)
        self.Round5Names.addWidget(self.Round5Player3)
        self.Round5Player3.setFixedWidth(120)

        self.Round5Player4 = QLabel(self.verticalLayoutWidget)
        self.Round5Names.addWidget(self.Round5Player4)
        self.Round5Player4.setFixedWidth(120)

        self.HLRound5.addLayout(self.Round5Names)

        self.Round5Score = QVBoxLayout()
        self.Round5ScorePlayer1 = QLabel(self.verticalLayoutWidget)
        self.Round5ScorePlayer1.setFont(self.font1)
        self.Round5ScorePlayer1.setStyleSheet(f"color: {roundTopColor}")
        self.Round5ScorePlayer1.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round5Score.addWidget(self.Round5ScorePlayer1)
        self.Round5ScorePlayer1.setFixedWidth(30)

        self.Round5ScorePlayer2 = QLabel(self.verticalLayoutWidget)
        self.Round5ScorePlayer2.setFont(self.font1)
        self.Round5ScorePlayer2.setStyleSheet(f"color: {roundTopColor}")
        self.Round5ScorePlayer2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round5Score.addWidget(self.Round5ScorePlayer2)
        self.Round5ScorePlayer2.setFixedWidth(30)

        self.Round5ScorePlayer3 = QLabel(self.verticalLayoutWidget)
        self.Round5ScorePlayer3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round5Score.addWidget(self.Round5ScorePlayer3)
        self.Round5ScorePlayer3.setFixedWidth(30)

        self.Round5ScorePlayer4 = QLabel(self.verticalLayoutWidget)
        self.Round5ScorePlayer4.setObjectName("Round5ScorePlayer4")
        self.Round5ScorePlayer4.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round5Score.addWidget(self.Round5ScorePlayer4)
        self.Round5ScorePlayer4.setFixedWidth(30)

        self.HLRound5.addLayout(self.Round5Score)
        self.TableRound5.addLayout(self.HLRound5)
        self.HLHalbFinale.addLayout(self.TableRound5)

        self.line_7 = QFrame(self.verticalLayoutWidget)
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.HLHalbFinale.addWidget(self.line_7)

        self.TableRound6 = QVBoxLayout()
        self.TopRound6 = QLabel(self.verticalLayoutWidget)
        self.TopRound6.setFont(font)
        self.TopRound6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableRound6.addWidget(self.TopRound6)
        self.TopRound6.setFixedWidth(150)

        self.lineRound6 = QFrame(self.verticalLayoutWidget)
        self.lineRound6.setFrameShape(QFrame.Shape.HLine)
        self.lineRound6.setFrameShadow(QFrame.Shadow.Sunken)
        self.TableRound6.addWidget(self.lineRound6)
        self.lineRound6.setFixedWidth(150)

        self.HLRound6 = QHBoxLayout()
        self.Round6Names = QVBoxLayout()
        self.Round6Player1 = QLabel(self.verticalLayoutWidget)
        self.Round6Player1.setFont(self.font1)
        self.Round6Player1.setStyleSheet(f"color: {roundTopColor}")
        self.Round6Names.addWidget(self.Round6Player1)
        self.Round6Player1.setFixedWidth(120)

        self.Round6Player2 = QLabel(self.verticalLayoutWidget)
        self.Round6Player2.setFont(self.font1)
        self.Round6Player2.setStyleSheet(f"color: {roundTopColor}")
        self.Round6Names.addWidget(self.Round6Player2)
        self.Round6Player2.setFixedWidth(120)

        self.Round6Player3 = QLabel(self.verticalLayoutWidget)
        self.Round6Names.addWidget(self.Round6Player3)
        self.Round6Player3.setFixedWidth(120)

        self.Round6Player4 = QLabel(self.verticalLayoutWidget)
        self.Round6Names.addWidget(self.Round6Player4)
        self.Round6Player4.setFixedWidth(120)

        self.HLRound6.addLayout(self.Round6Names)

        self.Round6Score = QVBoxLayout()
        self.Round6ScorePlayer1 = QLabel(self.verticalLayoutWidget)
        self.Round6ScorePlayer1.setFont(self.font1)
        self.Round6ScorePlayer1.setStyleSheet(f"color: {roundTopColor}")
        self.Round6ScorePlayer1.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round6Score.addWidget(self.Round6ScorePlayer1)
        self.Round6ScorePlayer1.setFixedWidth(30)

        self.Round6ScorePlayer2 = QLabel(self.verticalLayoutWidget)
        self.Round6ScorePlayer2.setFont(self.font1)
        self.Round6ScorePlayer2.setStyleSheet(f"color: {roundTopColor}")
        self.Round6ScorePlayer2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round6Score.addWidget(self.Round6ScorePlayer2)
        self.Round6ScorePlayer2.setFixedWidth(30)

        self.Round6ScorePlayer3 = QLabel(self.verticalLayoutWidget)
        self.Round6ScorePlayer3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round6Score.addWidget(self.Round6ScorePlayer3)
        self.Round6ScorePlayer3.setFixedWidth(30)

        self.Round6ScorePlayer4 = QLabel(self.verticalLayoutWidget)
        self.Round6ScorePlayer4.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round6Score.addWidget(self.Round6ScorePlayer4)
        self.Round6ScorePlayer4.setFixedWidth(30)

        self.HLRound6.addLayout(self.Round6Score)
        self.TableRound6.addLayout(self.HLRound6)
        self.HLHalbFinale.addLayout(self.TableRound6)
        self.verticalLayout.addLayout(self.HLHalbFinale)

        self.HLine3 = QFrame(self.verticalLayoutWidget)
        self.HLine3.setFrameShape(QFrame.Shape.HLine)
        self.HLine3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.HLine3)

        self.HLFinale = QHBoxLayout()
        self.TableRound7 = QVBoxLayout()
        self.TopRound7 = QLabel(self.verticalLayoutWidget)
        self.TopRound7.setFont(font)
        self.TopRound7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableRound7.addWidget(self.TopRound7)
        self.TopRound7.setFixedWidth(150)

        self.lineRound7 = QFrame(self.verticalLayoutWidget)
        self.lineRound7.setFrameShape(QFrame.Shape.HLine)
        self.lineRound7.setFrameShadow(QFrame.Shadow.Sunken)
        self.TableRound7.addWidget(self.lineRound7)
        self.lineRound7.setFixedWidth(150)

        self.HLRound7 = QHBoxLayout()
        self.Round7Names = QVBoxLayout()
        self.Round7Player1 = QLabel(self.verticalLayoutWidget)
        self.Round7Player1.setFont(self.font1)
        self.Round7Player1.setStyleSheet(f"color: {roundTopColor}")
        self.Round7Names.addWidget(self.Round7Player1)
        self.Round7Player1.setFixedWidth(120)

        self.Round7Player2 = QLabel(self.verticalLayoutWidget)
        self.Round7Player2.setFont(self.font1)
        self.Round7Names.addWidget(self.Round7Player2)
        self.Round7Player2.setFixedWidth(120)

        self.Round7Player3 = QLabel(self.verticalLayoutWidget)
        self.Round7Names.addWidget(self.Round7Player3)
        self.Round7Player3.setFixedWidth(120)

        self.Round7Player4 = QLabel(self.verticalLayoutWidget)
        self.Round7Names.addWidget(self.Round7Player4)
        self.Round7Player4.setFixedWidth(120)

        self.HLRound7.addLayout(self.Round7Names)

        self.Round7Score = QVBoxLayout()
        self.Round7ScorePlayer1 = QLabel(self.verticalLayoutWidget)
        self.Round7ScorePlayer1.setFont(self.font1)
        self.Round7ScorePlayer1.setStyleSheet(f"color: {roundTopColor}")
        self.Round7ScorePlayer1.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round7Score.addWidget(self.Round7ScorePlayer1)
        self.Round7ScorePlayer1.setFixedWidth(30)

        self.Round7ScorePlayer2 = QLabel(self.verticalLayoutWidget)
        self.Round7ScorePlayer2.setFont(self.font1)
        self.Round7ScorePlayer2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round7Score.addWidget(self.Round7ScorePlayer2)
        self.Round7ScorePlayer2.setFixedWidth(30)

        self.Round7ScorePlayer3 = QLabel(self.verticalLayoutWidget)
        self.Round7ScorePlayer3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round7Score.addWidget(self.Round7ScorePlayer3)
        self.Round7ScorePlayer3.setFixedWidth(30)

        self.Round7ScorePlayer4 = QLabel(self.verticalLayoutWidget)
        self.Round7ScorePlayer4.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.Round7Score.addWidget(self.Round7ScorePlayer4)
        self.Round7ScorePlayer4.setFixedWidth(30)

        self.HLRound7.addLayout(self.Round7Score)

        self.TableRound7.addLayout(self.HLRound7)

        self.HLFinale.addLayout(self.TableRound7)

        self.verticalLayout.addLayout(self.HLFinale)

        self.WinnerLabel = QLabel(self.verticalLayoutWidget)
        self.WinnerLabel.setFont(self.FontWinner)
        self.WinnerLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.WinnerLabel, 0, Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QSize(200, 0))
        self.pushButton.setMaximumSize(QSize(2000, 200))

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.centralwidget)

        self.TopLabel.setText(f"Turnierbaum")
        self.TopRound1.setText(f"{round_name_1}")
        self.Round1Player1.setText(f"{keys1[0]}")
        self.Round1Player2.setText(f"{keys1[1]}")
        self.Round1Player3.setText(f"{keys1[2]}")
        self.Round1Player4.setText(f"{keys1[3]}")
        self.Round1ScorePlayer1.setText(f"{ranks1[keys1[0]]}")
        self.Round1ScorePlayer2.setText(f"{ranks1[keys1[1]]}")
        self.Round1ScorePlayer3.setText(f"{ranks1[keys1[2]]}")
        self.Round1ScorePlayer4.setText(f"{ranks1[keys1[3]]}")
        self.TopRound2.setText(f"{round_name_2}")
        self.Round2Player1.setText(f"{keys2[0]}")
        self.Round2Player2.setText(f"{keys2[1]}")
        self.Round2Player3.setText(f"{keys2[2]}")
        self.Round2Player4.setText(f"{keys2[3]}")
        self.Round2ScorePlayer1.setText(f"{ranks2[keys2[0]]}")
        self.Round2ScorePlayer2.setText(f"{ranks2[keys2[1]]}")
        self.Round2ScorePlayer3.setText(f"{ranks2[keys2[2]]}")
        self.Round2ScorePlayer4.setText(f"{ranks2[keys2[3]]}")
        self.TopRound3.setText(f"{round_name_3}")
        self.Round3Player1.setText(f"{keys3[0]}")
        self.Round3Player2.setText(f"{keys3[1]}")
        self.Round3Player3.setText(f"{keys3[2]}")
        self.Round3Player4.setText(f"{keys3[3]}")
        self.Round3ScorePlayer1.setText(f"{ranks3[keys3[0]]}")
        self.Round3ScorePlayer2.setText(f"{ranks3[keys3[1]]}")
        self.Round3ScorePlayer3.setText(f"{ranks3[keys3[2]]}")
        self.Round3ScorePlayer4.setText(f"{ranks3[keys3[3]]}")
        self.TopRound4.setText(f"{round_name_4}")
        self.Round4Player1.setText(f"{keys4[0]}")
        self.Round4Player2.setText(f"{keys4[1]}")
        self.Round4Player3.setText(f"{keys4[2]}")
        self.Round4Player4.setText(f"{keys4[3]}")
        self.Round4ScorePlayer1.setText(f"{ranks4[keys4[0]]}")
        self.Round4ScorePlayer2.setText(f"{ranks4[keys4[1]]}")
        self.Round4ScorePlayer3.setText(f"{ranks4[keys4[2]]}")
        self.Round4ScorePlayer4.setText(f"{ranks4[keys4[3]]}")
        self.TopRound5.setText(f"{round_name_5}")
        self.Round5Player1.setText(f"{keys5[0]}")
        self.Round5Player2.setText(f"{keys5[1]}")
        self.Round5Player3.setText(f"{keys5[2]}")
        self.Round5Player4.setText(f"{keys5[3]}")
        self.Round5ScorePlayer1.setText(f"{ranks5[keys5[0]]}")
        self.Round5ScorePlayer2.setText(f"{ranks5[keys5[1]]}")
        self.Round5ScorePlayer3.setText(f"{ranks5[keys5[2]]}")
        self.Round5ScorePlayer4.setText(f"{ranks5[keys5[3]]}")
        self.TopRound6.setText(f"{round_name_6}")
        self.Round6Player1.setText(f"{keys6[0]}")
        self.Round6Player2.setText(f"{keys6[1]}")
        self.Round6Player3.setText(f"{keys6[2]}")
        self.Round6Player4.setText(f"{keys6[3]}")
        self.Round6ScorePlayer1.setText(f"{ranks6[keys6[0]]}")
        self.Round6ScorePlayer2.setText(f"{ranks6[keys6[1]]}")
        self.Round6ScorePlayer3.setText(f"{ranks6[keys6[2]]}")
        self.Round6ScorePlayer4.setText(f"{ranks6[keys6[3]]}")
        self.TopRound7.setText(f"{round_name_7}")
        self.Round7Player1.setText(f"{keys7[0]}")
        self.Round7Player2.setText(f"{keys7[1]}")
        self.Round7Player3.setText(f"{keys7[2]}")
        self.Round7Player4.setText(f"{keys7[3]}")
        self.Round7ScorePlayer1.setText(f"{ranks7[keys7[0]]}")
        self.Round7ScorePlayer2.setText(f"{ranks7[keys7[1]]}")
        self.Round7ScorePlayer3.setText(f"{ranks7[keys7[2]]}")
        self.Round7ScorePlayer4.setText(f"{ranks7[keys7[3]]}")

        self.winner = procs.get_player_name(1, 8)

        self.WinnerLabel.setText(f"Gewinner:\n{self.winner}")
        self.pushButton.setText(f"Schließen")
        self.pushButton.clicked.connect(self.closeTournamentWindow)

    def closeTournamentWindow(self):
        print("----- CLOSE TOURNAMENT WINDOW -----")
        self.close()


# class StatisticsWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(StatisticsWindow, self).__init__(parent)
#         self.setWindowTitle("Statistik")
#         self.setGeometry(100, 100, 1750, 900)

#         self.FontTop = QFont()
#         self.FontTop.setPointSize(40)
#         self.FontTop.setBold(True)

#         self.MainLayout = QWidget(self)
#         self.MainLayout.setObjectName("MainLayout")
#         self.MainLayout.setGeometry(QRect(0, 0, 1750, 860))

#         self.VLayoutStatistics = QVBoxLayout(self.MainLayout)
#         self.VLayoutStatistics.setContentsMargins(10, 10, 10, 10)
#         self.VLayoutStatistics.setSpacing(6)
#         self.VLayoutStatistics.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         self.MainLayout.setLayout(self.VLayoutStatistics)

#         self.TopTitle = QLabel()
#         self.TopTitle.setText("Statistik")
#         self.TopTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.TopTitle.setFont(self.FontTop)
#         self.VLayoutStatistics.addWidget(self.TopTitle)

#         # menu hinzufügen
#         self.CBRoundMenu = QComboBox(self)
#         self.VLayoutStatistics.addWidget(
#             self.CBRoundMenu, 0, Qt.AlignmentFlag.AlignCenter
#         )
#         self.CBRoundMenu.setObjectName("CBRoundMenu")
#         self.CBRoundMenu.setMinimumSize(QSize(200, 0))
#         self.CBRoundMenu.setMaximumSize(QSize(200, 250))
#         self.CBRoundMenu.addItem("Gesamt")
#         self.CBRoundMenu.addItem("Round 1")
#         self.CBRoundMenu.addItem("Round 2")
#         self.CBRoundMenu.addItem("Round 3")
#         self.CBRoundMenu.addItem("Round 4")
#         self.CBRoundMenu.addItem("Round 5")
#         self.CBRoundMenu.addItem("Round 6")
#         self.CBRoundMenu.addItem("Round 7")
#         self.CBRoundMenu.currentIndexChanged.connect(
#             lambda: self.initStatistics(self.CBRoundMenu.currentIndex())
#         )

#         # tops hinzufügen

#         self.HLayoutStatisticsTop = QHBoxLayout()
#         self.HLayoutStatisticsTop.setContentsMargins(10, 10, 10, 10)
#         self.HLayoutStatisticsTop.setSpacing(6)
#         self.HLayoutStatisticsTop.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.VLayoutStatistics.addLayout(self.HLayoutStatisticsTop)
#         self.pBOldestSong = QPushButton()
#         self.pBOldestSong.setEnabled(False)
#         self.pBOldestSong.setStyleSheet("padding: 10px")
#         self.HLayoutStatisticsTop.addWidget(self.pBOldestSong)
#         self.pBNewestSong = QPushButton()
#         self.pBNewestSong.setEnabled(False)
#         self.pBNewestSong.setStyleSheet("padding: 10px")
#         self.HLayoutStatisticsTop.addWidget(self.pBNewestSong)
#         self.pBTopYear = QPushButton()
#         self.pBTopYear.setEnabled(False)
#         self.pBTopYear.setStyleSheet("padding: 10px")
#         self.HLayoutStatisticsTop.addWidget(self.pBTopYear)
#         self.TopArtist = QPushButton()
#         self.TopArtist.setEnabled(False)
#         self.TopArtist.setStyleSheet("padding: 10px")
#         self.HLayoutStatisticsTop.addWidget(self.TopArtist)

#         # VLayout (chart/subtitle) hinzufügen

#         self.HLayoutStatisticsChart = QHBoxLayout()
#         self.HLayoutStatisticsChart.setContentsMargins(10, 10, 10, 10)
#         self.HLayoutStatisticsChart.setSpacing(6)
#         self.HLayoutStatisticsChart.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.VLayoutStatistics.addLayout(self.HLayoutStatisticsChart)

#         self.closeButton = QPushButton()
#         self.closeButton.setText("Schließen")
#         self.closeButton.clicked.connect(self.closeStatisticsWindow)
#         self.closeButton.setMinimumSize(QSize(200, 0))
#         self.closeButton.setMaximumSize(QSize(200, 200))
#         self.VLayoutStatistics.addWidget(
#             self.closeButton, 0, Qt.AlignmentFlag.AlignCenter
#         )

#         self.initStatistics(0)

#     def closeStatisticsWindow(self):
#         print("----- CLOSE STATISTICS WINDOW -----")
#         self.close()

#     def initStatistics(self, round_id):
#         print("----- RELOAD STATISTICS WINDOW -----")
#         round_1_name = procs.get_round_name(1)
#         round_2_name = procs.get_round_name(2)
#         round_3_name = procs.get_round_name(3)
#         round_4_name = procs.get_round_name(4)
#         round_5_name = procs.get_round_name(5)
#         round_6_name = procs.get_round_name(6)
#         round_7_name = procs.get_round_name(7)

#         self.CBRoundMenu.setItemText(1, round_1_name)
#         self.CBRoundMenu.setItemText(2, round_2_name)
#         self.CBRoundMenu.setItemText(3, round_3_name)
#         self.CBRoundMenu.setItemText(4, round_4_name)
#         self.CBRoundMenu.setItemText(5, round_5_name)
#         self.CBRoundMenu.setItemText(6, round_6_name)
#         self.CBRoundMenu.setItemText(7, round_7_name)

#         oldest_song = procs.get_oldest_song()
#         youngest_song = procs.get_youngest_song()
#         top_year = procs.get_most_songs_year()
#         top_artist = procs.get_most_songs_artist()

#         # years_result = procs.count_years()

#         # min_year = oldest_song['year']
#         # max_year = youngest_song['year']
#         if int(round_id) == 0:
#             print("Gesamt")
#             years_result = procs.count_years()
#             min_year = oldest_song["year"]
#             max_year = youngest_song["year"]
#         else:
#             print(f"Round {round_id}")
#             years_result = procs.count_years_by_round(round_id)
#             min_year = oldest_song["year"]
#             max_year = youngest_song["year"]

#         self.chart = QChart()
#         self.chart.setTitle("Anzahl der Songs pro Jahr")
#         self.chart.setTitleFont(self.FontTop)
#         self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
#         self.chart.legend().setVisible(False)
#         self.chart.setBackgroundBrush(QBrush(QColor("black")))
#         self.chart.setBackgroundVisible(False)
#         self.BarSeries = QBarSeries()
#         self.BarSeries.setLabelsVisible(True)
#         self.BarSeries.setBarWidth(1)

#         self.years = list(range(min_year, max_year + 1))
#         for year in self.years:
#             # print(year, years_result[year])
#             BarYear = "".join("Bar" + str(year))
#             BarYear = QBarSet(str(year))
#             BarYear.append(years_result[year])
#             BarYear.setColor(Qt.GlobalColor.darkGreen)
#             BarYear.setLabel(f"{year}: {years_result[year]}")
#             BarYear.setLabelColor(Qt.GlobalColor.black)
#             # BarYear.replace(0, year)
#             # print(BarYear.label())
#             self.BarSeries.append(BarYear)

#         self.chart.addSeries(self.BarSeries)

#         list_count = float((len(self.years)) + 1)

#         font_axis = QFont()
#         font_axis.setPointSize(8)

#         axisX = QValueAxis()
#         axisX.setTitleText("Jahr")
#         axisX.setLabelsAngle(90)
#         axisX.setLabelsVisible(True)
#         axisX.setRange(min_year, max_year + 1)
#         axisX.setTickCount(int(list_count))
#         axisX.setLabelFormat(" %i")
#         axisX.setLabelsFont(font_axis)
#         axisX.setLabelsColor(Qt.GlobalColor.white)

#         axisX.setGridLineVisible(False)
#         # print(self.years)

#         axisY = QValueAxis()
#         axisY.setTitleText("Anzahl Songs")
#         axisY.setLabelsColor(Qt.GlobalColor.white)
#         axisY.setRange(0, max(years_result.values()))
#         axisY.applyNiceNumbers()
#         axisY.setLabelFormat("%i")
#         axisY.setGridLineVisible(False)

#         # self.BarSeries.attachAxis(axisY)

#         self.chart.addAxis(axisX, Qt.AlignmentFlag.AlignBottom)
#         self.chart.addAxis(axisY, Qt.AlignmentFlag.AlignLeft)

#         self.chart.legend().setVisible(False)

#         chartview = QChartView(self.chart)
#         chartview.setRenderHint(QPainter.RenderHint.Antialiasing)
#         chartview.setChart(self.chart)
#         chartview.setContentsMargins(10, 10, 10, 10)

#         self.HLayoutStatisticsChart.removeWidget(chartview)
#         print("Chartview removed")
#         self.HLayoutStatisticsChart.addWidget(chartview)
#         print("Chartview added")

#         self.pBOldestSong.setText(
#             f"Ältester Song:\n{oldest_song['title']} - {oldest_song['artist']} ({oldest_song['year']})"
#         )
#         self.pBNewestSong.setText(
#             f"Neuester Song:\n{youngest_song['title']} - {youngest_song['artist']} ({youngest_song['year']})"
#         )
#         self.pBTopYear.setText(
#             f"Top Jahr:\n{top_year['year']} ({top_year['count']} Songs)"
#         )
#         self.TopArtist.setText(
#             f"Top Künstler:\n{top_artist['artist']} ({top_artist['count']} Songs)"
#         )


class PlayerNamesWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PlayerNamesWindow, self).__init__(parent)
        self.setWindowTitle("Spieler Namen")
        self.setGeometry(100, 100, 800, 800)

        round_1_name = procs.get_round_name(1)
        round_2_name = procs.get_round_name(2)
        round_3_name = procs.get_round_name(3)
        round_4_name = procs.get_round_name(4)

        player_1_name = procs.get_player_name(1, 1)
        player_2_name = procs.get_player_name(2, 1)
        player_3_name = procs.get_player_name(3, 1)
        player_4_name = procs.get_player_name(4, 1)
        player_5_name = procs.get_player_name(1, 2)
        player_6_name = procs.get_player_name(2, 2)
        player_7_name = procs.get_player_name(3, 2)
        player_8_name = procs.get_player_name(4, 2)
        player_9_name = procs.get_player_name(1, 3)
        player_10_name = procs.get_player_name(2, 3)
        player_11_name = procs.get_player_name(3, 3)
        player_12_name = procs.get_player_name(4, 3)
        player_13_name = procs.get_player_name(1, 4)
        player_14_name = procs.get_player_name(2, 4)
        player_15_name = procs.get_player_name(3, 4)
        player_16_name = procs.get_player_name(4, 4)

        self.MainLayout = QWidget(self)
        self.MainLayout.setGeometry(0, 0, 800, 800)

        self.VLayoutPlayerNames = QVBoxLayout(self.MainLayout)
        self.VLayoutPlayerNames.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow1 = QHBoxLayout()
        self.HLayoutPlayerNamesRow1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow2 = QHBoxLayout()
        self.HLayoutPlayerNamesRow2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow3 = QHBoxLayout()
        self.HLayoutPlayerNamesRow3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow4 = QHBoxLayout()
        self.HLayoutPlayerNamesRow4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow5 = QHBoxLayout()
        self.HLayoutPlayerNamesRow5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow6 = QHBoxLayout()
        self.HLayoutPlayerNamesRow6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow7 = QHBoxLayout()
        self.HLayoutPlayerNamesRow7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow8 = QHBoxLayout()
        self.HLayoutPlayerNamesRow8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow9 = QHBoxLayout()
        self.HLayoutPlayerNamesRow9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow10 = QHBoxLayout()
        self.HLayoutPlayerNamesRow10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow11 = QHBoxLayout()
        self.HLayoutPlayerNamesRow11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow12 = QHBoxLayout()
        self.HLayoutPlayerNamesRow12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow13 = QHBoxLayout()
        self.HLayoutPlayerNamesRow13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow14 = QHBoxLayout()
        self.HLayoutPlayerNamesRow14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow15 = QHBoxLayout()
        self.HLayoutPlayerNamesRow15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HLayoutPlayerNamesRow16 = QHBoxLayout()
        self.HLayoutPlayerNamesRow16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.FontTop = QFont()
        self.FontTop.setPointSize(40)
        self.FontTop.setBold(True)

        self.TopLabel = QLabel()
        self.TopLabel.setText("Spielernamen")
        self.TopLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TopLabel.setFont(self.FontTop)

        self.ChangeAllButton = QPushButton()
        self.ChangeAllButton.setText("Alle speichern")
        self.ChangeAllButton.setFixedSize(200, 30)
        self.ChangeAllButton.clicked.connect(self.ChangeAllPlayerNames)

        self.ShuffleButton = QPushButton()
        self.ShuffleButton.setText("Zufällig mischen")
        self.ShuffleButton.setFixedSize(200, 30)
        self.ShuffleButton.clicked.connect(self.ShufflePlayers)

        self.CloseButton = QPushButton()
        self.CloseButton.setText("Schließen")
        self.CloseButton.setFixedSize(200, 30)
        self.CloseButton.clicked.connect(self.closePlayerNameWindow)

        self.VLayoutPlayerNames.addWidget(self.TopLabel)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow1)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow2)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow3)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow4)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow5)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow6)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow7)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow8)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow9)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow10)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow11)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow12)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow13)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow14)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow15)
        self.VLayoutPlayerNames.addLayout(self.HLayoutPlayerNamesRow16)

        self.HLayoutButtons = QHBoxLayout()
        self.HLayoutButtons.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VLayoutPlayerNames.addLayout(self.HLayoutButtons)

        self.HLayoutButtons.addWidget(self.ChangeAllButton)
        self.HLayoutButtons.addWidget(self.ShuffleButton)
        self.HLayoutButtons.addWidget(self.CloseButton)

        self.lEplayer1Name = QLineEdit()
        self.lEplayer1Name.setFixedSize(250, 30)
        self.lEplayer2Name = QLineEdit()
        self.lEplayer2Name.setFixedSize(250, 30)
        self.lEplayer3Name = QLineEdit()
        self.lEplayer3Name.setFixedSize(250, 30)
        self.lEplayer4Name = QLineEdit()
        self.lEplayer4Name.setFixedSize(250, 30)
        self.lEplayer5Name = QLineEdit()
        self.lEplayer5Name.setFixedSize(250, 30)
        self.lEplayer6Name = QLineEdit()
        self.lEplayer6Name.setFixedSize(250, 30)
        self.lEplayer7Name = QLineEdit()
        self.lEplayer7Name.setFixedSize(250, 30)
        self.lEplayer8Name = QLineEdit()
        self.lEplayer8Name.setFixedSize(250, 30)
        self.lEplayer9Name = QLineEdit()
        self.lEplayer9Name.setFixedSize(250, 30)
        self.lEplayer10Name = QLineEdit()
        self.lEplayer10Name.setFixedSize(250, 30)
        self.lEplayer11Name = QLineEdit()
        self.lEplayer11Name.setFixedSize(250, 30)
        self.lEplayer12Name = QLineEdit()
        self.lEplayer12Name.setFixedSize(250, 30)
        self.lEplayer13Name = QLineEdit()
        self.lEplayer13Name.setFixedSize(250, 30)
        self.lEplayer14Name = QLineEdit()
        self.lEplayer14Name.setFixedSize(250, 30)
        self.lEplayer15Name = QLineEdit()
        self.lEplayer15Name.setFixedSize(250, 30)
        self.lEplayer16Name = QLineEdit()
        self.lEplayer16Name.setFixedSize(250, 30)
        self.labelPlayer1Round = QLabel()
        self.labelPlayer1Round.setFixedSize(150, 30)
        self.labelPlayer2Round = QLabel()
        self.labelPlayer2Round.setFixedSize(150, 30)
        self.labelPlayer3Round = QLabel()
        self.labelPlayer3Round.setFixedSize(150, 30)
        self.labelPlayer4Round = QLabel()
        self.labelPlayer4Round.setFixedSize(150, 30)
        self.labelPlayer5Round = QLabel()
        self.labelPlayer5Round.setFixedSize(150, 30)
        self.labelPlayer6Round = QLabel()
        self.labelPlayer6Round.setFixedSize(150, 30)
        self.labelPlayer7Round = QLabel()
        self.labelPlayer7Round.setFixedSize(150, 30)
        self.labelPlayer8Round = QLabel()
        self.labelPlayer8Round.setFixedSize(150, 30)
        self.labelPlayer9Round = QLabel()
        self.labelPlayer9Round.setFixedSize(150, 30)
        self.labelPlayer10Round = QLabel()
        self.labelPlayer10Round.setFixedSize(150, 30)
        self.labelPlayer11Round = QLabel()
        self.labelPlayer11Round.setFixedSize(150, 30)
        self.labelPlayer12Round = QLabel()
        self.labelPlayer12Round.setFixedSize(150, 30)
        self.labelPlayer13Round = QLabel()
        self.labelPlayer13Round.setFixedSize(150, 30)
        self.labelPlayer14Round = QLabel()
        self.labelPlayer14Round.setFixedSize(150, 30)
        self.labelPlayer15Round = QLabel()
        self.labelPlayer15Round.setFixedSize(150, 30)
        self.labelPlayer16Round = QLabel()
        self.labelPlayer16Round.setFixedSize(150, 30)
        self.pBchangePlayer1Name = QPushButton()
        self.pBchangePlayer1Name.setFixedSize(200, 30)
        self.pBchangePlayer2Name = QPushButton()
        self.pBchangePlayer2Name.setFixedSize(200, 30)
        self.pBchangePlayer3Name = QPushButton()
        self.pBchangePlayer3Name.setFixedSize(200, 30)
        self.pBchangePlayer4Name = QPushButton()
        self.pBchangePlayer4Name.setFixedSize(200, 30)
        self.pBchangePlayer5Name = QPushButton()
        self.pBchangePlayer5Name.setFixedSize(200, 30)
        self.pBchangePlayer6Name = QPushButton()
        self.pBchangePlayer6Name.setFixedSize(200, 30)
        self.pBchangePlayer7Name = QPushButton()
        self.pBchangePlayer7Name.setFixedSize(200, 30)
        self.pBchangePlayer8Name = QPushButton()
        self.pBchangePlayer8Name.setFixedSize(200, 30)
        self.pBchangePlayer9Name = QPushButton()
        self.pBchangePlayer9Name.setFixedSize(200, 30)
        self.pBchangePlayer10Name = QPushButton()
        self.pBchangePlayer10Name.setFixedSize(200, 30)
        self.pBchangePlayer11Name = QPushButton()
        self.pBchangePlayer11Name.setFixedSize(200, 30)
        self.pBchangePlayer12Name = QPushButton()
        self.pBchangePlayer12Name.setFixedSize(200, 30)
        self.pBchangePlayer13Name = QPushButton()
        self.pBchangePlayer13Name.setFixedSize(200, 30)
        self.pBchangePlayer14Name = QPushButton()
        self.pBchangePlayer14Name.setFixedSize(200, 30)
        self.pBchangePlayer15Name = QPushButton()
        self.pBchangePlayer15Name.setFixedSize(200, 30)
        self.pBchangePlayer16Name = QPushButton()
        self.pBchangePlayer16Name.setFixedSize(200, 30)
        self.pBchangePlayer1Name.setText("Spielername speichern")
        self.pBchangePlayer2Name.setText("Spielername speichern")
        self.pBchangePlayer3Name.setText("Spielername speichern")
        self.pBchangePlayer4Name.setText("Spielername speichern")
        self.pBchangePlayer5Name.setText("Spielername speichern")
        self.pBchangePlayer6Name.setText("Spielername speichern")
        self.pBchangePlayer7Name.setText("Spielername speichern")
        self.pBchangePlayer8Name.setText("Spielername speichern")
        self.pBchangePlayer9Name.setText("Spielername speichern")
        self.pBchangePlayer10Name.setText("Spielername speichern")
        self.pBchangePlayer11Name.setText("Spielername speichern")
        self.pBchangePlayer12Name.setText("Spielername speichern")
        self.pBchangePlayer13Name.setText("Spielername speichern")
        self.pBchangePlayer14Name.setText("Spielername speichern")
        self.pBchangePlayer15Name.setText("Spielername speichern")
        self.pBchangePlayer16Name.setText("Spielername speichern")
        self.labelPlayer1Round.setText(f"{round_1_name}:")
        self.labelPlayer2Round.setText(f"{round_1_name}:")
        self.labelPlayer3Round.setText(f"{round_1_name}:")
        self.labelPlayer4Round.setText(f"{round_1_name}:")
        self.labelPlayer5Round.setText(f"{round_2_name}:")
        self.labelPlayer6Round.setText(f"{round_2_name}:")
        self.labelPlayer7Round.setText(f"{round_2_name}:")
        self.labelPlayer8Round.setText(f"{round_2_name}:")
        self.labelPlayer9Round.setText(f"{round_3_name}:")
        self.labelPlayer10Round.setText(f"{round_3_name}:")
        self.labelPlayer11Round.setText(f"{round_3_name}:")
        self.labelPlayer12Round.setText(f"{round_3_name}:")
        self.labelPlayer13Round.setText(f"{round_4_name}:")
        self.labelPlayer14Round.setText(f"{round_4_name}:")
        self.labelPlayer15Round.setText(f"{round_4_name}:")
        self.labelPlayer16Round.setText(f"{round_4_name}:")
        self.pBchangePlayer1Name.clicked.connect(
            lambda: procs.update_player_name(1, self.lEplayer1Name.text())
        )
        self.pBchangePlayer2Name.clicked.connect(
            lambda: procs.update_player_name(2, self.lEplayer2Name.text())
        )
        self.pBchangePlayer3Name.clicked.connect(
            lambda: procs.update_player_name(3, self.lEplayer3Name.text())
        )
        self.pBchangePlayer4Name.clicked.connect(
            lambda: procs.update_player_name(4, self.lEplayer4Name.text())
        )
        self.pBchangePlayer5Name.clicked.connect(
            lambda: procs.update_player_name(5, self.lEplayer5Name.text())
        )
        self.pBchangePlayer6Name.clicked.connect(
            lambda: procs.update_player_name(6, self.lEplayer6Name.text())
        )
        self.pBchangePlayer7Name.clicked.connect(
            lambda: procs.update_player_name(7, self.lEplayer7Name.text())
        )
        self.pBchangePlayer8Name.clicked.connect(
            lambda: procs.update_player_name(8, self.lEplayer8Name.text())
        )
        self.pBchangePlayer9Name.clicked.connect(
            lambda: procs.update_player_name(9, self.lEplayer9Name.text())
        )
        self.pBchangePlayer10Name.clicked.connect(
            lambda: procs.update_player_name(10, self.lEplayer10Name.text())
        )
        self.pBchangePlayer11Name.clicked.connect(
            lambda: procs.update_player_name(11, self.lEplayer11Name.text())
        )
        self.pBchangePlayer12Name.clicked.connect(
            lambda: procs.update_player_name(12, self.lEplayer12Name.text())
        )
        self.pBchangePlayer13Name.clicked.connect(
            lambda: procs.update_player_name(13, self.lEplayer13Name.text())
        )
        self.pBchangePlayer14Name.clicked.connect(
            lambda: procs.update_player_name(14, self.lEplayer14Name.text())
        )
        self.pBchangePlayer15Name.clicked.connect(
            lambda: procs.update_player_name(15, self.lEplayer15Name.text())
        )
        self.pBchangePlayer16Name.clicked.connect(
            lambda: procs.update_player_name(16, self.lEplayer16Name.text())
        )
        self.lEplayer1Name.setText(player_1_name)
        self.lEplayer2Name.setText(player_2_name)
        self.lEplayer3Name.setText(player_3_name)
        self.lEplayer4Name.setText(player_4_name)
        self.lEplayer5Name.setText(player_5_name)
        self.lEplayer6Name.setText(player_6_name)
        self.lEplayer7Name.setText(player_7_name)
        self.lEplayer8Name.setText(player_8_name)
        self.lEplayer9Name.setText(player_9_name)
        self.lEplayer10Name.setText(player_10_name)
        self.lEplayer11Name.setText(player_11_name)
        self.lEplayer12Name.setText(player_12_name)
        self.lEplayer13Name.setText(player_13_name)
        self.lEplayer14Name.setText(player_14_name)
        self.lEplayer15Name.setText(player_15_name)
        self.lEplayer16Name.setText(player_16_name)

        self.HLayoutPlayerNamesRow1.addWidget(self.labelPlayer1Round)
        self.HLayoutPlayerNamesRow2.addWidget(self.labelPlayer2Round)
        self.HLayoutPlayerNamesRow3.addWidget(self.labelPlayer3Round)
        self.HLayoutPlayerNamesRow4.addWidget(self.labelPlayer4Round)
        self.HLayoutPlayerNamesRow5.addWidget(self.labelPlayer5Round)
        self.HLayoutPlayerNamesRow6.addWidget(self.labelPlayer6Round)
        self.HLayoutPlayerNamesRow7.addWidget(self.labelPlayer7Round)
        self.HLayoutPlayerNamesRow8.addWidget(self.labelPlayer8Round)
        self.HLayoutPlayerNamesRow9.addWidget(self.labelPlayer9Round)
        self.HLayoutPlayerNamesRow10.addWidget(self.labelPlayer10Round)
        self.HLayoutPlayerNamesRow11.addWidget(self.labelPlayer11Round)
        self.HLayoutPlayerNamesRow12.addWidget(self.labelPlayer12Round)
        self.HLayoutPlayerNamesRow13.addWidget(self.labelPlayer13Round)
        self.HLayoutPlayerNamesRow14.addWidget(self.labelPlayer14Round)
        self.HLayoutPlayerNamesRow15.addWidget(self.labelPlayer15Round)
        self.HLayoutPlayerNamesRow16.addWidget(self.labelPlayer16Round)

        self.HLayoutPlayerNamesRow1.addWidget(self.lEplayer1Name)
        self.HLayoutPlayerNamesRow2.addWidget(self.lEplayer2Name)
        self.HLayoutPlayerNamesRow3.addWidget(self.lEplayer3Name)
        self.HLayoutPlayerNamesRow4.addWidget(self.lEplayer4Name)
        self.HLayoutPlayerNamesRow5.addWidget(self.lEplayer5Name)
        self.HLayoutPlayerNamesRow6.addWidget(self.lEplayer6Name)
        self.HLayoutPlayerNamesRow7.addWidget(self.lEplayer7Name)
        self.HLayoutPlayerNamesRow8.addWidget(self.lEplayer8Name)
        self.HLayoutPlayerNamesRow9.addWidget(self.lEplayer9Name)
        self.HLayoutPlayerNamesRow10.addWidget(self.lEplayer10Name)
        self.HLayoutPlayerNamesRow11.addWidget(self.lEplayer11Name)
        self.HLayoutPlayerNamesRow12.addWidget(self.lEplayer12Name)
        self.HLayoutPlayerNamesRow13.addWidget(self.lEplayer13Name)
        self.HLayoutPlayerNamesRow14.addWidget(self.lEplayer14Name)
        self.HLayoutPlayerNamesRow15.addWidget(self.lEplayer15Name)
        self.HLayoutPlayerNamesRow16.addWidget(self.lEplayer16Name)

        self.HLayoutPlayerNamesRow1.addWidget(self.pBchangePlayer1Name)
        self.HLayoutPlayerNamesRow2.addWidget(self.pBchangePlayer2Name)
        self.HLayoutPlayerNamesRow3.addWidget(self.pBchangePlayer3Name)
        self.HLayoutPlayerNamesRow4.addWidget(self.pBchangePlayer4Name)
        self.HLayoutPlayerNamesRow5.addWidget(self.pBchangePlayer5Name)
        self.HLayoutPlayerNamesRow6.addWidget(self.pBchangePlayer6Name)
        self.HLayoutPlayerNamesRow7.addWidget(self.pBchangePlayer7Name)
        self.HLayoutPlayerNamesRow8.addWidget(self.pBchangePlayer8Name)
        self.HLayoutPlayerNamesRow9.addWidget(self.pBchangePlayer9Name)
        self.HLayoutPlayerNamesRow10.addWidget(self.pBchangePlayer10Name)
        self.HLayoutPlayerNamesRow11.addWidget(self.pBchangePlayer11Name)
        self.HLayoutPlayerNamesRow12.addWidget(self.pBchangePlayer12Name)
        self.HLayoutPlayerNamesRow13.addWidget(self.pBchangePlayer13Name)
        self.HLayoutPlayerNamesRow14.addWidget(self.pBchangePlayer14Name)
        self.HLayoutPlayerNamesRow15.addWidget(self.pBchangePlayer15Name)
        self.HLayoutPlayerNamesRow16.addWidget(self.pBchangePlayer16Name)

    def ChangeAllPlayerNames(self):
        print("----- CHANGED ALL PLAYER NAMES -----")
        procs.new_player_names(
            self.lEplayer1Name.text(),
            self.lEplayer2Name.text(),
            self.lEplayer3Name.text(),
            self.lEplayer4Name.text(),
            self.lEplayer5Name.text(),
            self.lEplayer6Name.text(),
            self.lEplayer7Name.text(),
            self.lEplayer8Name.text(),
            self.lEplayer9Name.text(),
            self.lEplayer10Name.text(),
            self.lEplayer11Name.text(),
            self.lEplayer12Name.text(),
            self.lEplayer13Name.text(),
            self.lEplayer14Name.text(),
            self.lEplayer15Name.text(),
            self.lEplayer16Name.text(),
        )

    def closePlayerNameWindow(self):
        print("----- CLOSE PLAYER NAME WINDOW -----")
        self.close()

    def ShufflePlayers(self):
        print("----- SHUFFLED ALL PLAYERS -----")
        # get players from database
        players = []

        for i in range(1, 17):
            players.append(procs.get_player_name_from_global_id(i))
        # shuffle players
        random.shuffle(players)

        # write players to database in new order
        for i in range(1, 17):
            procs.update_player_name(i, players[i - 1])
        # update text fields
        self.lEplayer1Name.setText(players[0])
        self.lEplayer2Name.setText(players[1])
        self.lEplayer3Name.setText(players[2])
        self.lEplayer4Name.setText(players[3])
        self.lEplayer5Name.setText(players[4])
        self.lEplayer6Name.setText(players[5])
        self.lEplayer7Name.setText(players[6])
        self.lEplayer8Name.setText(players[7])
        self.lEplayer9Name.setText(players[8])
        self.lEplayer10Name.setText(players[9])
        self.lEplayer11Name.setText(players[10])
        self.lEplayer12Name.setText(players[11])
        self.lEplayer13Name.setText(players[12])
        self.lEplayer14Name.setText(players[13])
        self.lEplayer15Name.setText(players[14])
        self.lEplayer16Name.setText(players[15])

        # print shuffled list:
        # print(players)


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)
        self.setWindowTitle("Spielen")
        self.setGeometry(100, 100, 1500, 1000)

        font_top = QFont()
        font_top.setPointSize(40)
        font = QFont()
        font.setPointSize(45)
        font1 = QFont()
        font1.setPointSize(30)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font3 = QFont()
        font3.setPointSize(14)

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 50, 1400, 900))
        self.VLayoutMain = QVBoxLayout(self.verticalLayoutWidget)
        self.VLayoutMain.setObjectName("VLayoutMain")
        self.VLayoutMain.setContentsMargins(0, 0, 0, 0)
        self.TopLayout = QVBoxLayout()
        self.TopLayout.setObjectName("TopLayout")
        self.TopLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.TopLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.RoundLabel = QLabel(self)
        self.TopLayout.addWidget(self.RoundLabel)
        self.TopLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.RoundLabel.setText("RUNDE")
        self.RoundLabel.setFont(font_top)
        self.CBRoundMenu = QComboBox(self)
        self.TopLayout.addWidget(self.CBRoundMenu)
        self.CBRoundMenu.setObjectName("CBRoundMenu")
        self.CBRoundMenu.setMinimumSize(QSize(200, 0))
        self.CBRoundMenu.setMaximumSize(QSize(200, 250))
        self.CBRoundMenu.addItem("Round 1")
        self.CBRoundMenu.addItem("Round 2")
        self.CBRoundMenu.addItem("Round 3")
        self.CBRoundMenu.addItem("Round 4")
        self.CBRoundMenu.addItem("Round 5")
        self.CBRoundMenu.addItem("Round 6")
        self.CBRoundMenu.addItem("Round 7")
        self.CBRoundMenu.currentIndexChanged.connect(
            lambda: procs.set_play_round_by_round_id(
                self.CBRoundMenu.currentIndex() + 1
            )
        )
        self.CBRoundMenu.currentIndexChanged.connect(self.initGame)

        self.VLayoutMain.addLayout(self.TopLayout)

        self.GridScoreLayout = QGridLayout()
        self.GridScoreLayout.setObjectName("GridScoreLayout")

        self.labelPlayer1Name = QLabel(self.verticalLayoutWidget)
        self.labelPlayer1Name.setObjectName("labelPlayer1Name")
        self.labelPlayer1Name.setFont(font1)
        self.labelPlayer1Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer1Name, 0, 0, 1, 1)

        self.labelPlayer2Name = QLabel(self.verticalLayoutWidget)
        self.labelPlayer2Name.setObjectName("labelPlayer2Name")
        self.labelPlayer2Name.setFont(font1)
        self.labelPlayer2Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer2Name, 0, 1, 1, 1)

        self.labelPlayer3Name = QLabel(self.verticalLayoutWidget)
        self.labelPlayer3Name.setObjectName("labelPlayer3Name")
        self.labelPlayer3Name.setFont(font1)
        self.labelPlayer3Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer3Name, 0, 2, 1, 1)

        self.labelPlayer4Name = QLabel(self.verticalLayoutWidget)
        self.labelPlayer4Name.setObjectName("labelPlayer4Name")
        self.labelPlayer4Name.setFont(font1)
        self.labelPlayer4Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer4Name, 0, 3, 1, 1)

        self.labelPlayer1Points = QLabel(self.verticalLayoutWidget)
        self.labelPlayer1Points.setObjectName("labelPlayer1Points")
        self.labelPlayer1Points.setMaximumSize(QSize(250, 16777215))
        self.labelPlayer1Points.setFont(font)
        self.labelPlayer1Points.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer1Points, 1, 0, 1, 1)

        self.labelPlayer3Points = QLabel(self.verticalLayoutWidget)
        self.labelPlayer3Points.setObjectName("labelPlayer3Points")
        self.labelPlayer3Points.setMaximumSize(QSize(250, 16777215))
        self.labelPlayer3Points.setFont(font)
        self.labelPlayer3Points.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer3Points, 1, 2, 1, 1)

        self.labelPlayer4Points = QLabel(self.verticalLayoutWidget)
        self.labelPlayer4Points.setObjectName("labelPlayer4Points")
        self.labelPlayer4Points.setMaximumSize(QSize(250, 16777215))
        self.labelPlayer4Points.setFont(font)
        self.labelPlayer4Points.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer4Points, 1, 3, 1, 1)

        self.labelPlayer2Points = QLabel(self.verticalLayoutWidget)
        self.labelPlayer2Points.setObjectName("labelPlayer2Points")
        self.labelPlayer2Points.setMaximumSize(QSize(250, 16777215))
        self.labelPlayer2Points.setFont(font)
        self.labelPlayer2Points.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GridScoreLayout.addWidget(self.labelPlayer2Points, 1, 1, 1, 1)

        self.pBPlayer1Correct = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer1Correct.setObjectName("pBPlayer1Correct")
        self.pBPlayer1Correct.setMinimumSize(QSize(0, 40))
        self.pBPlayer1Correct.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer1Correct.setFont(font2)
        self.pBPlayer1Correct.setStyleSheet(
            "background-color: rgb(0, 255, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer1Correct.clicked.connect(lambda: self.answer(1, "correct"))
        self.pBPlayer1Correct.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer1Correct, 2, 0, 1, 1)

        self.pBPlayer2Correct = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer2Correct.setObjectName("pBPlayer2Correct")
        self.pBPlayer2Correct.setMinimumSize(QSize(0, 40))
        self.pBPlayer2Correct.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer2Correct.setFont(font2)
        self.pBPlayer2Correct.setStyleSheet(
            "background-color: rgb(0, 255, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer2Correct.clicked.connect(lambda: self.answer(2, "correct"))
        self.pBPlayer2Correct.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer2Correct, 2, 1, 1, 1)

        self.pBPlayer3Correct = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer3Correct.setObjectName("pBPlayer3Correct")
        self.pBPlayer3Correct.setMinimumSize(QSize(0, 40))
        self.pBPlayer3Correct.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer3Correct.setFont(font2)
        self.pBPlayer3Correct.setStyleSheet(
            "background-color: rgb(0, 255, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer3Correct.clicked.connect(lambda: self.answer(3, "correct"))
        self.pBPlayer3Correct.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer3Correct, 2, 2, 1, 1)

        self.pBPlayer4Correct = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer4Correct.setObjectName("pBPlayer4Correct")
        self.pBPlayer4Correct.setMinimumSize(QSize(0, 40))
        self.pBPlayer4Correct.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer4Correct.setFont(font2)
        self.pBPlayer4Correct.setStyleSheet(
            "background-color: rgb(0, 255, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer4Correct.clicked.connect(lambda: self.answer(4, "correct"))
        self.pBPlayer4Correct.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer4Correct, 2, 3, 1, 1)

        self.pBPlayer1Wrong = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer1Wrong.setObjectName("pBPlayer1Wrong")
        self.pBPlayer1Wrong.setMinimumSize(QSize(0, 40))
        self.pBPlayer1Wrong.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer1Wrong.setFont(font2)
        self.pBPlayer1Wrong.setStyleSheet(
            "background-color: rgb(255,0, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer1Wrong.clicked.connect(lambda: self.answer(1, "wrong"))
        self.pBPlayer1Wrong.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer1Wrong, 3, 0, 1, 1)

        self.pBPlayer2Wrong = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer2Wrong.setObjectName("pBPlayer2Wrong")
        self.pBPlayer2Wrong.setMinimumSize(QSize(0, 40))
        self.pBPlayer2Wrong.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer2Wrong.setFont(font2)
        self.pBPlayer2Wrong.setStyleSheet(
            "background-color: rgb(255,0, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer2Wrong.clicked.connect(lambda: self.answer(2, "wrong"))
        self.pBPlayer2Wrong.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer2Wrong, 3, 1, 1, 1)

        self.pBPlayer3Wrong = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer3Wrong.setObjectName("pBPlayer3Wrong")
        self.pBPlayer3Wrong.setMinimumSize(QSize(0, 40))
        self.pBPlayer3Wrong.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer3Wrong.setFont(font2)
        self.pBPlayer3Wrong.setStyleSheet(
            "background-color: rgb(255,0, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer3Wrong.clicked.connect(lambda: self.answer(3, "wrong"))
        self.pBPlayer3Wrong.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer3Wrong, 3, 2, 1, 1)

        self.pBPlayer4Wrong = QPushButton(self.verticalLayoutWidget)
        self.pBPlayer4Wrong.setObjectName("pBPlayer4Wrong")
        self.pBPlayer4Wrong.setMinimumSize(QSize(0, 40))
        self.pBPlayer4Wrong.setMaximumSize(QSize(250, 16777215))
        self.pBPlayer4Wrong.setFont(font2)
        self.pBPlayer4Wrong.setStyleSheet(
            "background-color: rgb(255,0, 0); color: rgb(0,0,0);"
        )
        self.pBPlayer4Wrong.clicked.connect(lambda: self.answer(4, "wrong"))
        self.pBPlayer4Wrong.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBPlayer4Wrong, 3, 3, 1, 1)

        self.pBQuizControls = QPushButton(self.verticalLayoutWidget)
        self.pBQuizControls.setObjectName("pBQuizControls")
        self.pBQuizControls.setMinimumSize(QSize(0, 40))
        self.pBQuizControls.setMaximumSize(QSize(250, 16777215))
        self.pBQuizControls.setFont(font2)
        self.pBQuizControls.setStyleSheet("color: rgb(249, 240, 107);")
        self.GridScoreLayout.addWidget(self.pBQuizControls, 5, 0, 1, 1)
        
        self.pBQuizControls.clicked.connect(lambda: procs.mark_all_questions_played_for_round(procs.get_play_round()))
        self.pBQuizControls.clicked.connect(self.initGame)

        self.pBTikTak = QPushButton(self.verticalLayoutWidget)
        self.pBTikTak.setObjectName("pBTikTak")
        self.pBTikTak.setMinimumSize(QSize(0, 40))
        self.pBTikTak.setMaximumSize(QSize(250, 16777215))
        self.pBTikTak.setFont(font2)
        self.pBTikTak.clicked.connect(lambda: procs.play_clock())
        self.GridScoreLayout.addWidget(self.pBTikTak, 5, 1, 1, 1)

        self.pBSkipQuestionQuiz = QPushButton(self.verticalLayoutWidget)
        self.pBSkipQuestionQuiz.setObjectName("pBSkipQuestionQuiz")
        self.pBSkipQuestionQuiz.setMinimumSize(QSize(0, 40))
        self.pBSkipQuestionQuiz.setMaximumSize(QSize(250, 16777215))
        self.pBSkipQuestionQuiz.setFont(font2)
        self.pBSkipQuestionQuiz.clicked.connect(lambda: self.answer(1, "skip"))
        self.pBSkipQuestionQuiz.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBSkipQuestionQuiz, 5, 2, 1, 1)

        self.pBResetBuzzer = QPushButton(self.verticalLayoutWidget)
        self.pBResetBuzzer.setObjectName("pBResetBuzzer")
        self.pBResetBuzzer.setMinimumSize(QSize(0, 40))
        self.pBResetBuzzer.setMaximumSize(QSize(250, 16777215))
        self.pBResetBuzzer.setFont(font2)
        self.pBResetBuzzer.clicked.connect(lambda: procs.reset_buzzer())
        self.pBResetBuzzer.clicked.connect(self.initGame)
        self.GridScoreLayout.addWidget(self.pBResetBuzzer, 5, 3, 1, 1)

        self.VLayoutMain.addLayout(self.GridScoreLayout)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName("line")
        self.line.setMinimumSize(QSize(0, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.VLayoutMain.addWidget(self.line)

        self.HLayoutNextQuestionInfo = QHBoxLayout()

        NextQuestionCover = image_path + "standard.jpg"
        self.NextQuestionCoverPixmap = QPixmap(NextQuestionCover)
        self.NextQuestionCoverPixmap = self.NextQuestionCoverPixmap.scaled(small_image)
        self.NextQuestionCover = QLabel(self)
        self.NextQuestionCover.setPixmap(self.NextQuestionCoverPixmap)

        self.NextQuestionInfo = QVBoxLayout()

        self.NextQuestionLabelTop = QLabel(self)
        self.NextQuestionLabelTop.setText("Nächste Frage:")
        self.NextQuestionLabelTop.setFont(font2)
        self.NextQuestionLabelTop.setFixedSize(800, 30)
        self.NextQuestionLabelTitle = QLabel(self)
        self.NextQuestionLabelTitle.setText("Titel")
        self.NextQuestionLabelTitle.setFont(font2)
        self.NextQuestionLabelTitle.setFixedSize(800, 60)
        self.NextQuestionLabelTitle.setWordWrap(True)
        self.NextQuestionLabelComment = QPlainTextEdit()
        self.NextQuestionLabelComment.setStyleSheet("font-size: 20px;")
        self.NextQuestionLabelComment.setFixedWidth(800)

        self.NextQuestionInfo.addWidget(
            self.NextQuestionLabelTop, 0, Qt.AlignmentFlag.AlignCenter
        )
        self.NextQuestionInfo.addWidget(
            self.NextQuestionLabelTitle, 0, Qt.AlignmentFlag.AlignCenter
        )
        self.NextQuestionInfo.addWidget(
            self.NextQuestionLabelComment, 0, Qt.AlignmentFlag.AlignCenter
        )

        self.HLayoutNextQuestionInfo.addLayout(self.NextQuestionInfo)
        self.HLayoutNextQuestionInfo.addWidget(self.NextQuestionCover)
        self.HLayoutNextQuestionInfo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.VLayoutMain.addLayout(self.HLayoutNextQuestionInfo)


        PreviousQuestionCover = image_path + "standard.jpg"
        self.PreviousQuestionCoverPixmap = QPixmap(PreviousQuestionCover)
        self.NextQuestionCoverPixmap = self.NextQuestionCoverPixmap.scaled(small_image)
        self.PreviousQuestionCover = QLabel(self)
        self.PreviousQuestionCover.setPixmap(self.PreviousQuestionCoverPixmap)

        self.PreviousQuestionInfo = QVBoxLayout()

        self.PreviousQuestionLabelTop = QLabel(self)
        self.PreviousQuestionLabelTop.setText("Vorherige Frage:")
        self.PreviousQuestionLabelTop.setFont(font2)
        self.PreviousQuestionLabelTop.setFixedSize(800, 30)
        self.PreviousQuestionLabelTitle = QLabel(self)
        self.PreviousQuestionLabelTitle.setText("Titel")
        self.PreviousQuestionLabelTitle.setFont(font2)
        self.PreviousQuestionLabelTitle.setFixedSize(800, 60)
        self.PreviousQuestionLabelTitle.setWordWrap(True)
        self.PreviousQuestionLabelComment = QPlainTextEdit()
        self.PreviousQuestionLabelComment.setStyleSheet("font-size: 20px;")
        self.PreviousQuestionLabelComment.setFixedWidth(800)

        self.PreviousQuestionInfo.addWidget(
            self.PreviousQuestionLabelTop, 0, Qt.AlignmentFlag.AlignCenter
        )
        self.PreviousQuestionInfo.addWidget(
            self.PreviousQuestionLabelTitle, 0, Qt.AlignmentFlag.AlignCenter
        )
        self.PreviousQuestionInfo.addWidget(
            self.PreviousQuestionLabelComment, 0, Qt.AlignmentFlag.AlignCenter
        )

        self.HLayoutPreviousQuestionInfo = QHBoxLayout()
        self.HLayoutPreviousQuestionInfo.setObjectName("HLayoutPreviousQuestionInfo")

        self.HLayoutPreviousQuestionInfo.addLayout(self.PreviousQuestionInfo)
        self.HLayoutPreviousQuestionInfo.addWidget(
            self.PreviousQuestionCover, 0, Qt.AlignmentFlag.AlignCenter
        )
        self.HLayoutPreviousQuestionInfo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.VLayoutMain.addLayout(self.HLayoutPreviousQuestionInfo)

        self.HLayoutExit = QHBoxLayout()
        self.HLayoutExit.setObjectName("HLayoutExit")
        self.exit_button = QPushButton(self.verticalLayoutWidget)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setEnabled(True)
        self.exit_button.setMaximumSize(QSize(300, 16777215))
        self.exit_button.setFont(font3)
        self.exit_button.setText("Schließen")
        self.exit_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.exit_button.clicked.connect(self.closeGameWindow)

        self.HLayoutExit.addWidget(self.exit_button)

        self.VLayoutMain.addLayout(self.HLayoutExit)

        # start timer for checking player color
        self.ColorTimer = QTimer()
        self.ColorTimer.timeout.connect(self.get_player_color)
        self.ColorTimer.start(1000)


        # start subprocess for checking arduino serial signal (buzzer pressed)
        self.buzzer_checker = subprocess.Popen(["python3", "buzzer.py"])

        # init round
        self.initGame()

    def answer(self, player_id, answer):
        if answer == "correct":
            procs.play_correct()
        if answer == "wrong":
            procs.play_wrong()
        if answer == "skip":
            procs.play_hit()
        my_round_id = procs.get_play_round()
        play_mode = procs.get_play_mode()

        player_name = procs.get_player_name(player_id, my_round_id)
        player_points = procs.get_player_points(player_id, my_round_id)

        # print(f"----- {player_name} ANSWERED {answer} -----")

        procs.update_player_on_answer(player_id, my_round_id, answer)
        procs.sort_ranking(my_round_id)

        next_question = {}
        next_question = procs.get_next_question(my_round_id)
        procs.set_last_question(
            next_question["question"],
            next_question["answer"],
            next_question["image"],
            next_question["comment"],
        )

        procs.mark_question_as_played(my_round_id)

        procs.reset_buzzer()
        procs.set_buzzer_blocked(my_round_id)

        if int(play_mode) == 2:
            if int(my_round_id) != 4:
                print("sorting playoffs")
                procs.sort_ranking_playoff(my_round_id)
            procs.get_play_off_players_to_round()
        procs.send_buzzer_blocked()
        procs.set_monitor_round_by_round_id(11)
        time.sleep(1.1)

    def initGame(self):
        print("\n----- RELOAD GAME WINDOW -----")
        round_name_1 = procs.get_round_name(1)
        round_name_2 = procs.get_round_name(2)
        round_name_3 = procs.get_round_name(3)
        round_name_4 = procs.get_round_name(4)
        round_name_5 = procs.get_round_name(5)
        round_name_6 = procs.get_round_name(6)
        round_name_7 = procs.get_round_name(7)

        # get round id form database
        my_round_id = procs.get_play_round()
        print(f"ROUND ID: {my_round_id}")
        # getround name from database
        round_name = procs.get_round_name(my_round_id)
        print(f"ROUND NAME: {round_name}")
        # get playmode from database
        play_mode = procs.get_play_mode()
        print(f"PLAYMODE {play_mode} (1=16 players / 2= 12 players)")
        # set buzzer blocked from player status in round
        procs.set_buzzer_blocked(my_round_id)
        # get buzzer blocked from database
        buzzer_blocked = procs.get_buzzer_blocked()
        if int(buzzer_blocked) == 4:
            print("NO BUZZER BLOCKED")
        # send buzzer blocked to arduino
        procs.send_buzzer_blocked()
        # reset pressed buzzer
        procs.set_buzzer_pressed("4")
        # get player names, points and global ids

        player_count = [1, 2, 3, 4]
        players = {}
        for player in player_count:
            player_name = procs.get_player_name(player, my_round_id)
            player_points = procs.get_player_points(player, my_round_id)
            players[player_name] = player_points

        player_1_name = list(players.keys())[0]
        player_2_name = list(players.keys())[1]
        player_3_name = list(players.keys())[2]
        player_4_name = list(players.keys())[3]
        player_1_points = list(players.values())[0]
        player_2_points = list(players.values())[1]
        player_3_points = list(players.values())[2]
        player_4_points = list(players.values())[3]

        procs.set_monitor_round_by_round_id(my_round_id)

        print(f"Player {player_1_name} has {player_1_points} points")  # noqa: F821
        print(f"Player {player_2_name} has {player_2_points} points")  # noqa: F821
        print(f"Player {player_3_name} has {player_3_points} points")  # noqa: F821
        print(f"Player {player_4_name} has {player_4_points} points")  # noqa: F821

        next_question = {}
        next_question = procs.get_next_question(my_round_id)

        # spotify_song, spotify_artist = procs.get_song_infos()

        previous_question = {}
        previous_question = procs.get_last_question()
        maximum_questions = procs.get_round_maximum_questions(my_round_id)
        maximum_questions_db = next_question.get("total", maximum_questions)
        played_questions = procs.get_played_questions_for_round(my_round_id)
        reserve_questions = 0
        no_questions = False
        if played_questions == int(maximum_questions_db):
            no_questions = True
        if maximum_questions > int(maximum_questions_db):
            maximum_questions = int(maximum_questions_db)
        if maximum_questions < int(maximum_questions_db):
            reserve_questions = int(maximum_questions_db) - maximum_questions
        questionsToPlay = maximum_questions - next_question.get("seq", 0) + 1
        question_count = (
            f"Frage: {next_question.get('seq',0)} / {maximum_questions} (+{reserve_questions}) / {questionsToPlay}"
        )
        self.labelPlayer1Name.setText(player_1_name)
        self.labelPlayer2Name.setText(player_2_name)
        self.labelPlayer3Name.setText(player_3_name)
        self.labelPlayer4Name.setText(player_4_name)
        self.labelPlayer1Points.setText(str(player_1_points))
        self.labelPlayer2Points.setText(str(player_2_points))
        self.labelPlayer3Points.setText(str(player_3_points))
        self.labelPlayer4Points.setText(str(player_4_points))

        self.pBPlayer1Correct.setText("\u2713")
        self.pBPlayer2Correct.setText("\u2713")
        self.pBPlayer3Correct.setText("\u2713")
        self.pBPlayer4Correct.setText("\u2713")
        self.pBPlayer1Wrong.setText("X")
        self.pBPlayer2Wrong.setText("X")
        self.pBPlayer3Wrong.setText("X")
        self.pBPlayer4Wrong.setText("X")
        # print(f"DEBUG: no_questions: {no_questions}")
        # print(f"DEBUG: questions to play: {questionsToPlay}")
        # self.pBPreviousSongSpotify.setText("\u23ee")
        # self.pBPlaySpotify.setText("\u23f5")
        # self.pBPauseSpotify.setText("\u23f8")
        # self.pBNextSongSpotify.setText("\u23ed")
        self.pBQuizControls.setText(question_count)

        if not no_questions:
            self.pBPlayer1Correct.setEnabled(True)
            self.pBPlayer1Correct.setStyleSheet("background-color: rgb(0, 255, 0); color: rgb(0,0,0);")
            self.pBPlayer1Wrong.setEnabled(True)
            self.pBPlayer1Wrong.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0,0,0);")
            self.pBPlayer2Correct.setEnabled(True)
            self.pBPlayer2Correct.setStyleSheet("background-color: rgb(0, 255, 0); color: rgb(0,0,0);")
            self.pBPlayer2Wrong.setEnabled(True)
            self.pBPlayer2Wrong.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0,0,0);")
            self.pBPlayer3Correct.setEnabled(True)
            self.pBPlayer3Correct.setStyleSheet("background-color: rgb(0, 255, 0); color: rgb(0,0,0);")
            self.pBPlayer3Wrong.setEnabled(True)
            self.pBPlayer3Wrong.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0,0,0);")
            self.pBPlayer4Correct.setEnabled(True)
            self.pBPlayer4Correct.setStyleSheet("background-color: rgb(0, 255, 0); color: rgb(0,0,0);")
            self.pBPlayer4Wrong.setEnabled(True)
            self.pBPlayer4Wrong.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0,0,0);")
            self.pBTikTak.setEnabled(True)
            self.pBSkipQuestionQuiz.setEnabled(True)
            self.pBResetBuzzer.setEnabled(True)

            if questionsToPlay < 1:
                stechen = int(next_question.get('seq', 0)) - maximum_questions
                self.pBQuizControls.setStyleSheet("color: rgb(255, 0, 0);")
                self.pBQuizControls.setText(f"Stechen: {stechen} / {reserve_questions}")
            if questionsToPlay == 1:
                self.pBQuizControls.setStyleSheet("color: rgb(255, 165, 0);")
                self.pBQuizControls.setText(f"Letzte Frage! (+{reserve_questions})")
            if questionsToPlay in range(2, 6):
                self.pBQuizControls.setStyleSheet("color: rgb(255, 165, 0);")
                self.pBQuizControls.setText(f"noch {questionsToPlay} Fragen! (+{reserve_questions})")
            # if questionsToPlay in range(2, 5):
            #     self.pBQuizControls.setStyleSheet("color: rgb(255, 165, 0);")
            if questionsToPlay > 5:
                self.pBQuizControls.setStyleSheet("color: rgb(0, 255, 0);")
                self.pBQuizControls.setText(f"noch {questionsToPlay} Fragen! (+{reserve_questions})")
        if no_questions:
            self.pBQuizControls.setStyleSheet("color: rgb(0, 255, 0);")
            self.pBQuizControls.setText("Runde beendet!")
            self.pBPlayer1Correct.setEnabled(False)
            self.pBPlayer1Correct.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBPlayer1Wrong.setEnabled(False)
            self.pBPlayer1Wrong.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBPlayer2Correct.setEnabled(False)
            self.pBPlayer2Correct.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBPlayer2Wrong.setEnabled(False)
            self.pBPlayer2Wrong.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBPlayer3Correct.setEnabled(False)
            self.pBPlayer3Correct.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBPlayer3Wrong.setEnabled(False)
            self.pBPlayer3Wrong.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBPlayer4Correct.setEnabled(False)
            self.pBPlayer4Correct.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBPlayer4Wrong.setEnabled(False)
            self.pBPlayer4Wrong.setStyleSheet("color: rgb(0, 0, 0);")
            self.pBTikTak.setEnabled(False)
            self.pBSkipQuestionQuiz.setEnabled(False)




        self.pBTikTak.setText("\u23f2 - ticking")
        self.pBSkipQuestionQuiz.setText("skip question")
        self.pBResetBuzzer.setText("reset buzzer")

        self.NextQuestionLabelTitle.setText(
            f"{next_question.get('question')}\n-> {next_question.get('answer')}"
        )
        self.NextQuestionLabelComment.setPlainText(next_question.get("comment"))
        NextQuestionCover = next_question.get("image", "standard.jpg")
        NextQuestionCover = "".join(image_path + NextQuestionCover)
        self.NextQuestionCoverPixmap = QPixmap(NextQuestionCover)
        self.NextQuestionCoverPixmap = self.NextQuestionCoverPixmap.scaled(small_image)
        self.NextQuestionCover.setPixmap(self.NextQuestionCoverPixmap)

        # self.currentSpotifySong.setText(
        #     f"Spotify spielt gerade: {spotify_song} - {spotify_artist}"
        # )

        self.PreviousQuestionLabelTitle.setText(
            f"{previous_question['question']}\n-> {previous_question['answer']}"
        )
        self.PreviousQuestionLabelComment.setPlainText(previous_question["comment"])
        PreviousQuestionCover = previous_question["image"]
        PreviousQuestionCover = "".join(image_path + PreviousQuestionCover)
        self.PreviousQuestionCoverPixmap = QPixmap(PreviousQuestionCover)
        self.PreviousQuestionCoverPixmap = self.PreviousQuestionCoverPixmap.scaled(small_image)
        self.PreviousQuestionCover.setPixmap(self.PreviousQuestionCoverPixmap)

        self.exit_button.setText: window("Schließen")

        self.CBRoundMenu.setItemText(0, round_name_1)
        self.CBRoundMenu.setItemText(1, round_name_2)
        self.CBRoundMenu.setItemText(2, round_name_3)
        self.CBRoundMenu.setItemText(3, round_name_4)
        self.CBRoundMenu.setItemText(4, round_name_5)
        self.CBRoundMenu.setItemText(5, round_name_6)
        self.CBRoundMenu.setItemText(6, round_name_7)

        self.RoundLabel.setText(round_name)

    def get_player_color(self):
        # for debugging:
        # print("----- GET PLAYER COLOR -----")
        # print(f"COLORTIMER ISACTIVE: {self.ColorTimer.isActive()}")
        buzzer_blocked = procs.get_buzzer_blocked()
        buzzer_pressed = procs.get_buzzer_pressed_from_db()
        if buzzer_blocked == "0":
            self.labelPlayer1Name.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer1Points.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer2Name.setStyleSheet("")
            self.labelPlayer2Points.setStyleSheet("")
            self.labelPlayer3Name.setStyleSheet("")
            self.labelPlayer3Points.setStyleSheet("")
            self.labelPlayer4Name.setStyleSheet("")
            self.labelPlayer4Points.setStyleSheet("")
        elif buzzer_blocked == "1":
            self.labelPlayer2Name.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer2Points.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer1Name.setStyleSheet("")
            self.labelPlayer1Points.setStyleSheet("")
            self.labelPlayer3Name.setStyleSheet("")
            self.labelPlayer3Points.setStyleSheet("")
            self.labelPlayer4Name.setStyleSheet("")
            self.labelPlayer4Points.setStyleSheet("")
        elif buzzer_blocked == "2":
            self.labelPlayer3Name.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer3Points.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer1Name.setStyleSheet("")
            self.labelPlayer1Points.setStyleSheet("")
            self.labelPlayer2Name.setStyleSheet("")
            self.labelPlayer2Points.setStyleSheet("")
            self.labelPlayer4Name.setStyleSheet("")
            self.labelPlayer4Points.setStyleSheet("")
        elif buzzer_blocked == "3":
            self.labelPlayer4Name.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer4Points.setStyleSheet(f"color: {blockedBuzzerColor};")
            self.labelPlayer1Name.setStyleSheet("")
            self.labelPlayer1Points.setStyleSheet("")
            self.labelPlayer2Name.setStyleSheet("")
            self.labelPlayer2Points.setStyleSheet("")
            self.labelPlayer3Name.setStyleSheet("")
            self.labelPlayer3Points.setStyleSheet("")
        if buzzer_pressed == "0":
            self.labelPlayer1Name.setStyleSheet(f"color: {pressedBuzzerColor};")
            self.labelPlayer1Points.setStyleSheet(f"color: {pressedBuzzerColor};")
        elif buzzer_pressed == "1":
            self.labelPlayer2Name.setStyleSheet(f"color: {pressedBuzzerColor};")
            self.labelPlayer2Points.setStyleSheet(f"color: {pressedBuzzerColor};")
        elif buzzer_pressed == "2":
            self.labelPlayer3Name.setStyleSheet(f"color: {pressedBuzzerColor};")
            self.labelPlayer3Points.setStyleSheet(f"color: {pressedBuzzerColor};")
        elif buzzer_pressed == "3":
            self.labelPlayer4Name.setStyleSheet(f"color: {pressedBuzzerColor};")
            self.labelPlayer4Points.setStyleSheet(f"color: {pressedBuzzerColor};")
        elif buzzer_blocked == "4" and buzzer_pressed == "4":
            self.labelPlayer1Name.setStyleSheet("")
            self.labelPlayer1Points.setStyleSheet("")
            self.labelPlayer2Name.setStyleSheet("")
            self.labelPlayer2Points.setStyleSheet("")
            self.labelPlayer3Name.setStyleSheet("")
            self.labelPlayer3Points.setStyleSheet("")
            self.labelPlayer4Name.setStyleSheet("")
            self.labelPlayer4Points.setStyleSheet("")

    def closeGameWindow(self):
        procs.set_monitor_to_pause()
        print("----- CLOSE GAME WINDOW -----")
        self.ColorTimer.stop()
        self.buzzer_checker.kill()
        self.close()


class MusikQuiz(QMainWindow):
    def __init__(self, parent=None):
        super(MusikQuiz, self).__init__(parent)

        print("----- OPEN MAIN WINDOW -----")
        self.setWindowTitle("Musik Quiz")
        self.setGeometry(100, 100, 600, 300)

        title = "Quiz"

        version_number = procs.get_version_number()

        self.fontTop = QFont()
        self.fontTop.setPointSize(40)
        self.fontTop.setBold(True)

        self.title_label = QLabel(title, self)
        self.title_label.setFont(self.fontTop)
        self.subtitle = QLabel(f"Version {version_number}\nby Benny Schaeling\n", self)
        self.subtitle.setFont(QFont("Verdana", 10))
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.play_button = QPushButton("Spielen", self)
        self.play_button.setFixedSize(200, 30)
        self.play_button.clicked.connect(self.show_game_window)
        self.tournament_button = QPushButton("Turnierbaum", self)
        self.tournament_button.setFixedSize(200, 30)
        self.tournament_button.clicked.connect(self.tournament)
        self.pBplayerNames = QPushButton("Spielernamen", self)
        self.pBplayerNames.setFixedSize(200, 30)
        self.pBplayerNames.clicked.connect(self.PlayerNames)
        self.pBQuestions = QPushButton("Fragen", self)
        self.pBQuestions.setFixedSize(200, 30)
        self.pBQuestions.clicked.connect(self.Questions)
        # self.stats_button = QPushButton("Statistiken", self)
        # self.stats_button.setFixedSize(200, 30)
        # self.stats_button.clicked.connect(self.stats)
        self.settings_button = QPushButton("Einstellungen", self)
        self.settings_button.setFixedSize(200, 30)
        self.settings_button.clicked.connect(self.settings)
        self.close_button = QPushButton("Beenden", self)
        self.close_button.setFixedSize(200, 30)
        self.close_button.clicked.connect(self.close)

        MainLayout = QVBoxLayout()

        MainLayout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        MainLayout.addWidget(self.subtitle, alignment=Qt.AlignmentFlag.AlignCenter)
        MainLayout.addWidget(self.play_button, alignment=Qt.AlignmentFlag.AlignCenter)
        MainLayout.addWidget(self.pBplayerNames, alignment=Qt.AlignmentFlag.AlignCenter)
        MainLayout.addWidget(self.pBQuestions, alignment=Qt.AlignmentFlag.AlignCenter)
        MainLayout.addWidget(
            self.tournament_button, alignment=Qt.AlignmentFlag.AlignCenter
        )
        # MainLayout.addWidget(self.stats_button, alignment=Qt.AlignmentFlag.AlignCenter)
        MainLayout.addWidget(
            self.settings_button, alignment=Qt.AlignmentFlag.AlignCenter
        )
        MainLayout.addWidget(self.close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(MainLayout)
        widget.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.layout().setSpacing(0)
        self.setCentralWidget(widget)

    def show_game_window(self, checked):
        print("----- OPEN GAME WINDOW -----")
        self.w = GameWindow()
        self.w.show()

    def tournament(self):
        print("----- OPEN TOURNAMENT WINDOW -----")
        self.w = TournamentWindow()
        self.w.show()

    def PlayerNames(self):
        print("----- OPEN PLAYER NAMES WINDOW -----")
        self.w = PlayerNamesWindow()
        self.w.show()

    def Questions(self):
        print("----- OPEN QuestionS WINDOW -----")
        self.w = QuestionsWindow()
        self.w.show()

    def stats(self):
        print("----- OPEN STATISTICS WINDOW -----")
        self.w = StatisticsWindow()
        self.w.show()

    def settings(self):
        print("----- OPEN SETTINGS WINDOW -----")
        self.w = SettingsWindow()
        self.w.show()

    def close(self):
        print("----- CLOSE MAIN WINDOW -----")
        app.quit()


app = QApplication([])
window = MusikQuiz()
window.show()
app.exec()
