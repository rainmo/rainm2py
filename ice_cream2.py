import easygui
flavor = easygui.enterbox('what is your favorite ice cream flavor?',
                          default = 'vanilla')
easygui.msgbox('you entered ' + flavor)
