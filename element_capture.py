from selenium import webdriver
from PIL import Image
from time import sleep
from selenium.webdriver.firefox.options import Options
from io import BytesIO



def capture():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    url = 'https://www.worldometers.info/coronavirus/'
    driver.get(url)
   
    
    
    # 전체 캡쳐
    # S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    # driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment    
    # driver.save_screenshot('screenshot.png')
    # driver.close()

    

    # 전체 페이지의 사이즈를 구하여 브라우저의 창 크기를 확대하고 스크린캡처를 합니다.
    page_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(page_width, page_height)
    png = driver.get_screenshot_as_png()
    
    # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
    element = driver.find_element_by_css_selector("div.content-inner")
    image_location = element.location
    image_size = element.size
    driver.quit()
    
    # 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
    im = Image.open(BytesIO(png))
    left = image_location['x']
    top = image_location['y']
    right = image_location['x'] + image_size['width']
    bottom = image_location['y'] + image_size['height']
    im = im.crop((left, top, right, bottom))
    im.save('my_screenshot_name1.png')

    print("완료")


    
 
    # png = driver.get_screenshot_as_png()
    
    # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
    # element = driver1.find_element_by_css_selector("div.content-inner")
    
    # image_location = element.location
    # image_size = element.size

    # print("quit")
    # driver1.quit()
    
    # # 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
    # im = Image.open("my_screenshot_name0.png")
    # left = image_location['x']
    # top = image_location['y']
    # right = image_location['x'] + image_size['width']
    # bottom = image_location['y'] + image_size['height']
    # im = im.crop((left, top, right, bottom))
    # print("save1")
    # im.save("my_screenshot_name4.png")






   


#   element = driver.find_element_by_css_selector("div.content-inner")

#     driver.maximize_window()
    
#     location = element.location
#     size = element.size

    # x = location['x']
    # y = location['y']
    # width = location['x']+size['width']
    # height = location['y']+size['height']

    # im = Image.open('my_screenshot_name.png')
    # im = im.crop((int(x), int(y), int(width), int(height)))
    # im.save('my_screenshot_name.png')


   
    # Saves a .png file with name my_screenshot_name to the directory that
    # # you are running the program from.
    # screenshot_name = "my_screenshot_name.png"
    # driver.save_screenshot(screenshot_name) 
