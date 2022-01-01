#to do:
#analyse how tape question box works CHECK！
#try to post a question through http request CHECK！
#ROCK ON!!!!!!
from os import name
import time
import getquestion
from selenium import webdriver
tape = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
tape.get(str('https://www.tapechat.net/uu/00WED8/OJ53UOVY#focus' )) #enter the tape chat adress(with #focus)
questions = getquestion.get_content('questions.txt')
x = 0
def tapequestion():
    global x
    box = tape.find_element_by_id('textarea')
    box.send_keys(questions[x])
    question = tape.find_element_by_class_name('quiz-button')
    question.click()
    time.sleep(0.5)
    tape.back()
    x =+ 1

if __name__ == '__main__':
    for x in range(0,100):
        tapequestion()
        time.sleep(0.5)