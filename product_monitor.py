from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the driver options for Chrome
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run browser in headless mode to prevent pop-ups

driver = webdriver.Chrome(executable_path='drivers/chromedriver', options=options)

# List of target SKUs and product names (customize as needed)
target_skus = ['gigabyte-gv-n5090aorusm-ice-32gd-nvidia-geforce-rtx-5090-32gb-gddr7/p/N82E16814932765']
product_names = ['Nvidia RTX 5090']

def monitor_and_purchase():
    while True:
        # Iterate through each SKU
        for sku in target_skus:
            # Replace 'page_url' with the actual URL containing availability check and add-to-cart/buy now buttons
            page_url = f'https://example.com/{sku}'
            
            driver.get(page_url)

            # Check if product is available
            # Replace 'availability_element' with the HTML element that indicates out-of-stock status
            availability_element = driver.find_element(By.CLASS_NAME,'fa-solid fa-triangle-exclamation color-msg-icon')
            
            if not availability_element:
                print(f'{product_names[target_skus.index(sku)]} is in stock! Purchasing...')
                
                # Simulate adding to cart or purchasing by interacting with the appropriate HTML elements
                add_to_cart_button = driver.find_element_by_css_selector('btn btn-primary btn-wide')
                add_to_cart_button.click()

                purchase_button = driver.find_element_by_css_selector('.buy-now-button')
                purchase_button.click()
            else:
                print(f'{product_names[target_skus.index(sku)]} is out of stock.')

        # Wait for a few minutes before checking again
        import time
        time.sleep(30)

if __name__ == '__main__':
    monitor_and_purchase()
    