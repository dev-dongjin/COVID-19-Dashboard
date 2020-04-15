from selenium import webdriver
from PIL import Image
from selenium.webdriver.firefox.options import Options


def capture():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    url = 'https://www.worldometers.info/coronavirus/'
    print("파이어폭스 열기")
    driver.get(url)
   
    
    
    # # 전체 캡쳐
    # # S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    # # driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment    
    # # driver.save_screenshot('screenshot.png')
    # # driver.close()

    

    # 전체 페이지의 사이즈를 구하여 브라우저의 창 크기를 확대하고 스크린캡처를 합니다.
    page_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot('screenshot.png')
    
    # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
    maincounter = driver.find_element_by_css_selector("#maincounter-wrap")
    margin = driver.find_element_by_css_selector("div[style ='margin-top:50px;']")

    # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
    margin_top = driver.find_element_by_css_selector("div[style='margin-top:40px; clear: both;']")

    # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
    main_table = driver.find_element_by_css_selector("#main_table_countries_today")
    south_korea = driver.find_element_by_css_selector('a[href="country/south-korea/"]')


    up = maincounter.location
    up_size = maincounter.size
    down = margin.location
    down_size = margin.size
    
    up2 = margin_top.location
    up_size2 = margin_top.size

    up3 = main_table.location
    up_size3 = main_table.size
    down3 = south_korea.location
    down_size3 = south_korea.size

    driver.quit()
    print("파이어폭스 닫기")

    # element Location : {'x': 148, 'y': 332}
    # element size : {'height': 149.14999389648438, 'width': 703.3333129882812}
    # bottop Location : {'x': 148, 'y': 880}
    # bottop size : {'height': 0.0, 'width': 703.3333129882812}
    #left = 148
    #top = 332
    #right = 850
    #bottom = 880
    
    # 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
    im1 = Image.open('screenshot.png')
    left = up['x']
    top = up['y']
    right = down['x'] + down_size['width']
    bottom = down['y'] + down_size['height']

    print("left = "+str(left)+", top = "+str(top)+", right = "+str(right)+", bottom = "+str(bottom))
    im1 = im1.crop((left, top, right, bottom))
    im1.save('my_screenshot_name1.png')
    print("사진1 저장")

    print(up2)
    print(up_size2)
    im2 = Image.open('screenshot.png')
    left = up2['x']
    top = up2['y']
    right = up2['x'] + up_size2['width']
    bottom = up2['y'] + 510
    print("left = "+str(left)+", top = "+str(top)+", right = "+str(right)+", bottom = "+str(bottom))
    im2 = im2.crop((left, top, right, bottom))
    # im2 = im2.crop((300, 300, 30, 30))
    im2.save('my_screenshot_name2.png')
    print("사진2 저장")

    print(up3)
    print(up_size3)
    print(down3)
    print(down_size3)
    im3 = Image.open('screenshot.png')
    left = up3['x']
    top = up3['y']
    right = down3['x'] + up_size3['width']
    bottom = down3['y'] + down_size3['height']
    print("left = "+str(left)+", top = "+str(top)+", right = "+str(right)+", bottom = "+str(bottom))
    im3 = im3.crop((left, top, right, bottom))
    im3.save('my_screenshot_name3.png')
    print("사진3 저장")

    print("capture 완료")
