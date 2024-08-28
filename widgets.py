from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt



def mainWidgets(window):

    inputBar = QLineEdit(window)
    inputBar.setGeometry(16, 30, 390, 80)
    inputBar.setAlignment(Qt.AlignRight)
    inputBar.setStyleSheet("""
        font-size: 80px;
        font-weight: bold;
        color: white;
    """)
   
    #   AC Button
    ac = QPushButton("AC", window)
    ac.setGeometry(16, 130, 87, 87)
    ac.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            background-color: #A5A5A5;     
            border-radius: 40px;                 
        }
                            
          QPushButton:hover{
            background-color: #878484;
        }
    """)

        #   Change Plus or Minus Button
    changePlusMinus = QPushButton("+/-", window)
    changePlusMinus.setGeometry(119, 130, 87, 87)
    changePlusMinus.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            background-color: #A5A5A5; 
            color: black;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

        # Percent Button
    percent = QPushButton("%", window)
    percent.setGeometry(222, 130, 87, 87)
    percent.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            background-color: #A5A5A5;
            color: black;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

    #Increase button
    divide = QPushButton("/", window)
    divide.setGeometry(325, 130, 87, 87)
    divide.setStyleSheet("""
        QPushButton{
            
            font-size: 30px;
            font-weight: bold;
            background-color: #FE9F0C;
            color: white;
            border-radius: 40px;

          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

    #Increase Button
    increase = QPushButton("x", window)
    increase.setGeometry(324, 233, 87, 87)
    increase.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            font-weight: bold;
            background-color: #FE9F0C;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

    #Minus Button

    minus = QPushButton("-", window)
    minus.setGeometry(324, 336, 87, 87)
    minus.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            font-weight: bold;
            background-color: #FE9F0C;
            color: white;
            border-radius: 40px;
          
        }
                     
        QPushButton:hover{
            background-color: #878484;
        }
                     
    """)

    #Plus Button
    plus = QPushButton("+", window)
    plus.setGeometry(325, 439, 87, 87)
    plus.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            font-weight: bold;
            background-color: #FE9F0C;
            color: white;
            border-radius: 40px;
          
        }
                     
        QPushButton:hover{
            background-color: #878484;
        }

    """)

        #Equal Button
    equal = QPushButton("=", window)
    equal.setGeometry(325, 542, 87, 87)
    equal.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            font-weight: bold;
            background-color: #FE9F0C;
            color: white;
            border-radius: 40px;
          
        }
                     
        QPushButton:hover{
            background-color: #878484;
        }

    """)

    #NUMBERS:
    #seven Button
    seven = QPushButton("7", window)
    seven.setGeometry(16, 233, 87, 87)
    seven.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

        # Eight Button
    eight = QPushButton("8", window)
    eight.setGeometry(119, 233, 87, 87)
    eight.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)
    

    #Nine Button    
    nine = QPushButton("9", window)
    nine.setGeometry(222, 233, 87, 87)
    nine.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

    #Four Button
    four = QPushButton("4", window)
    four.setGeometry(16, 336, 87, 87)
    four.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

        #Five Button
    five = QPushButton("5", window)
    five.setGeometry(119, 336, 87, 87)
    five.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

        #Six Button
    six = QPushButton("6", window)
    six.setGeometry(222, 336, 87, 87)
    six.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

        #One Button
    one = QPushButton("1", window)
    one.setGeometry(16, 439, 87, 87)
    one.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

        #Two Button
    two = QPushButton("2", window)
    two.setGeometry(119, 439, 87, 87)
    two.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)

            #Three Button
    three = QPushButton("3", window)
    three.setGeometry(222, 439, 87, 87)
    three.setStyleSheet("""
        QPushButton{
            font-size: 40px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
         QPushButton:hover{
            background-color: #878484;
        }
    """)

                #Zero Button
    zero = QPushButton("0", window)
    zero.setGeometry(16, 542, 190, 87)
    zero.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)



                #Dot Button
    dot = QPushButton(".", window)
    dot.setGeometry(222, 542, 87, 87)
    dot.setStyleSheet("""
        QPushButton{
            font-size: 30px;
            font-weight: bold;
            background-color: #343434;
            color: white;
            border-radius: 40px;
          
        }
                     
          QPushButton:hover{
            background-color: #878484;
        }
    """)



    def clickOne():
        txt = inputBar.text()
        inputBar.setText(txt + '1')

    def clickTwo():
        txt = inputBar.text()
        inputBar.setText(txt + '2')

    def clickThree():
        txt = inputBar.text()
        inputBar.setText(txt + '3')

    def clickFour():
        txt = inputBar.text()
        inputBar.setText(txt + '4')

    def clickFive():
        txt = inputBar.text()
        inputBar.setText(txt + '5')

    def clickSix():
        txt = inputBar.text()
        inputBar.setText(txt + '6')

    def clickSeven():
        txt = inputBar.text()
        inputBar.setText(txt + '7')

    def clickEight():
        txt = inputBar.text()
        inputBar.setText(txt + '8')

    def clickNine():
        txt = inputBar.text()
        inputBar.setText(txt + '9')

    def clickZero():
        txt = inputBar.text()
        inputBar.setText(txt + '0')

    def clickDot():
        txt = inputBar.text()
        inputBar.setText(txt + '.')
    
    def clickPlusMinus():
        txt = inputBar.text()
        inputBar.setText(txt)
 
    
    def clickDivide():
        txt = inputBar.text()
        if txt[-1] == '/':
            return
        if txt[-1] in ['*', '-', '+', '%']:
            txt = txt[:-1]
        inputBar.setText(txt + '/')

    def clickIncrease():
        txt = inputBar.text()
        if txt[-1] == '*':
            return
        if txt[-1] in ['-', '/', '+']:
            txt = txt[:-1]
        inputBar.setText(txt + '*')

    def clickMinus():
        txt = inputBar.text()
        if txt[-1] == '-':
            return
        if txt[-1] in ['+', '/', '*']:
            txt = txt[:-1]
        inputBar.setText(txt + '-')

    def clickPlus():
        txt = inputBar.text()

        if txt[-1] == '+':
            return
        if txt[-1] in ['-', '/', '*']:
            txt = txt[:-1]
        inputBar.setText(txt + '+')

    def clickEqual():
        txt = inputBar.text()
        if txt[-1] in ['+', '-', '*', '/', '.']:
            txt = txt[:-1]
        try:
            result = str(eval(txt))
            inputBar.setText(result)
        except Exception as e:
            inputBar.setText('Error')

    def clickAc():
        inputBar.clear()
        
    def clickPercent():
        txt = inputBar.text()
        if txt[-1] == '%':
            return
        if txt[-1] in ['+', '-', '*', '/']:
            txt = txt[:-1]
        inputBar.setText(txt + '%')

    one.clicked.connect(clickOne)
    two.clicked.connect(clickTwo)
    three.clicked.connect(clickThree)
    four.clicked.connect(clickFour)
    five.clicked.connect(clickFive)
    six.clicked.connect(clickSix)
    seven.clicked.connect(clickSeven)
    eight.clicked.connect(clickEight)
    nine.clicked.connect(clickNine)
    zero.clicked.connect(clickZero)
    dot.clicked.connect(clickDot)
    changePlusMinus.clicked.connect(clickPlusMinus)
    percent.clicked.connect(clickPercent)
    divide.clicked.connect(clickDivide)
    increase.clicked.connect(clickIncrease)
    minus.clicked.connect(clickMinus)
    plus.clicked.connect(clickPlus)
    equal.clicked.connect(clickEqual)
    ac.clicked.connect(clickAc)
    
