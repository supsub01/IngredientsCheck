#!"C:\Users\supri\Anaconda3\python.exe"

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import cgi
import re

print("Content-Type: text/html; charset=utf-8\n\n")

#Get HTML form inputs
form = cgi.FieldStorage()
food =  form.getvalue('product')
ing =  form.getvalue('ingredientList')

print ("Content-type:text/html\n\r\n")

#Selenium webdriver  
options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(r"C:\Users\supri\OneDrive\Desktop\AutomatingTheBoringStuff\chromedriver.exe",options=options)
browser.get('https://www.fooducate.com/')

SearchElem=browser.find_element_by_css_selector('#header > nav > div > form > div > input')
SubmitElem=browser.find_element_by_css_selector('#header > nav > div > form > div > button')
SearchElem.send_keys(food)
SubmitElem.click()
    
browser.implicitly_wait(5)

i=1
CommentSelector=''
MaxComments=0
ProdIndex=0

while i<5:
    CommentSelector=f'#search-page > div > div > div.panel-body > div > div > ul > li:nth-child({i}) > div > div.details-col > div.bottom-row.row > div.comments-col.col-sm-2.col-xs-3 > span'
    try:
        CommentElem= browser.find_element_by_css_selector(CommentSelector)
    except NoSuchElementException:
        if i==1:
            print("Can't find product details, Sorry!")
            return;
        else:
            break
    NumComments=int(CommentElem.text)
    if NumComments > MaxComments:
        MaxComments=NumComments
        ProdIndex=i
    i=i+1

ProductElem=browser.find_element_by_css_selector(f'#search-page > div > div > div.panel-body > div > div > ul > li:nth-child({ProdIndex}) > div').click()
IngredientsPara=browser.find_element_by_css_selector('#product-page > div > div.row > div.col-md-8 > div.ingredients.panel.panel-default > div.panel-body > p').text
browser.quit()

print ('Hello')

Ingredients=IngredientsPara.lower().split(',')
CheckIngredients=ing.lower().split(',')

print("These Ingredients MAY be problematic")
for word in Ingredients:
    for checkIng in CheckIngredients:
        if(re.search(checkIng,word)):
            print(word,",")
            break






# #print(getFoodIngredients(food, ingr))
# print('<b>Hello World</b>')
