from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import cgi

def getFoodIngredients(food, ing):
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(r'C:\Users\supri\OneDrive\Desktop\AutomatingTheBoringStuff\chromedriver.exe',options=options)
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
        CommentElem=browser.find_element_by_css_selector(CommentSelector)
        NumComments=int(CommentElem.text)
        if NumComments > MaxComments:
            MaxComments=NumComments
            ProdIndex=i
        i=i+1

    ProductElem=browser.find_element_by_css_selector(f'#search-page > div > div > div.panel-body > div > div > ul > li:nth-child({ProdIndex}) > div').click()
    IngredientsPara=browser.find_element_by_css_selector('#product-page > div > div.row > div.col-md-8 > div.ingredients.panel.panel-default > div.panel-body > p').text
    
    Ingredients=IngredientsPara.lower().split(',')
    CheckIngredients=ing.lower().split(',')
    
    print("These Ingredients seem problematic")
    for word in Ingredients:
        for checkIng in CheckIngredients:
            if(re.search(checkIng,word)):
                print(word,",")
                break

form = cgi.FieldStorage()
food =  form.getvalue('product')
ing =  form.getvalue('ingredientList')

print(getFoodIngredients(food, ingredient.lower()))