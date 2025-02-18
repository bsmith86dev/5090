from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib
from email.mime.text import MIMEText

# Set up the driver options for Chrome
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run browser in headless mode to prevent pop-ups

driver = webdriver.Chrome(executable_path='drivers/chromedriver', options=options)

# List of target item IDs and product names (customize as needed)
target_item_ids = ['B0DVCH9WJH', 'B0DS2Z8854', 'B0DV6MK91R']
product_names = ['Item 1', 'Item 2', 'Item 3']

def monitor_and_purchase():
    while True:
        for item_id in target_item_ids:
            # Replace 'page_url' with the actual URL containing availability check and add-to-cart/buy now buttons
            page_url = f'https://example.com/item?id={item_id}'
            
            driver.get(page_url)

            try:
                # Check if the "Add to Cart" button is available
                add_to_cart_button = driver.find_element(By.ID, item_id)
                cart_inner_text = add_to_cart_button.find_element(By.CLASS_NAME, 'a-button-inner').text

                if cart_inner_text == "Add to Cart":
                    print(f'{product_names[target_item_ids.index(item_id)]} is available! Adding to cart...')

                    # Simulate adding to cart
                    add_to_cart_button.click()

                    # Complete the order
                    checkout_button = driver.find_element(By.ID, 'checkout-button')
                    checkout_button.click()
                    
                    # Notify by email (customize email details)
                    send_email(product_names[target_item_ids.index(item_id)])
                else:
                    print(f'{product_names[target_item_ids.index(item_id)]} is not available.')
            except Exception as e:
                print(f'Error: {e}')
            
        # Wait for a few minutes before checking again
        time.sleep(30)

def send_email(product_name):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_password"

    message = MIMEText(f'{product_name} is now available and has been added to your cart.')
    message['Subject'] = 'Item Available for Purchase'
    message['From'] = sender_email
    message['To'] = receiver_email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == '__main__':
    monitor_and_purchase()