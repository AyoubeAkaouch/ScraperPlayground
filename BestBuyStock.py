from selenium import webdriver
import time
import os
import datetime

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

if __name__ == '__main__':
    urlBestBuy30Series = 'https://www.bestbuy.ca/en-ca/collection/rtx-30-series-graphic-cards/316108?path=soldandshippedby0enrchstring%253ABest%2BBuy'
    driver.get(urlBestBuy30Series)
    class_name_item = 'div.col-xs-12_1GBy8.col-sm-4_NwItf.col-lg-3_2V2hX.x-productListItem.productLine_2N9kG'
    class_name_item_name = 'productItemName_3IZ3c'
    class_name_item_price = 'span.screenReaderOnly_3anTj.large_3aP7Z'
    class_name_item_available_instore = 'shippingAvailability_2RMa1'
    class_name_item_available_online = 'availabilityMessageSearchPickup_2eGze'
    class_name_item_url = 'link_3hcyN'  # Have to add 'https://www.bestbuy.ca' before this url

    while True:
        driver.refresh()
        # Start by finding all 30 series items listed at bestbuy
        items = driver.find_elements_by_css_selector(class_name_item)
        print(f'~~~~~~~~~~~{datetime.datetime.now()}~~~~~~~~~~~')

        for item in items:

            name = item.find_element_by_class_name(class_name_item_name).text
            price = item.find_element_by_css_selector(class_name_item_price).text

            try:
                available_instore = item.find_element_by_class_name(class_name_item_available_instore).text
            except:
                available_instore = 'Not available in store'

            try:
                available_online = item.find_element_by_class_name(class_name_item_available_online).text
            except:
                available_online = 'Not available online'

            #Printing results
            os.system('color 7')
            print (f'{name}  {price}:', end='')

            if 'sold out' in available_instore:
                os.system('color 4')
                print ('Sold out in stores // ', end='')
            else:
                os.system('color A')
                print(f'{available_instore} // ', end='')

            if 'sold out' in available_online:
                os.system('color 4')
                print ('Sold out online')
            else:
                os.system('color A')
                print(f'{available_online}')

        time.sleep(20)

    driver.quit()
