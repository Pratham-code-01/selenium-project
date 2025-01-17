import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def navigate_to_trending_products():
    driver.get('https://www.radiustheme.com/demo/wordpress/themes/zilly/')
    time.sleep(4)

    x = 0
    y = 3300
    driver.execute_script("window.scrollTo("+str(x)+","+str(y)+")")
    time.sleep(2)
    
    trending_section = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div[8]/div')))
    items = trending_section.find_elements(By.CLASS_NAME, 'rtsb-product-content')

    category_counts = {}
    for item in items:
        category = item.find_element(By.CLASS_NAME, 'rtsb-category-list-item').text.strip()
        category_counts[category] = category_counts.get(category, 0) + 1

    print('Trending Products (Grouped by Category) : ', category_counts)
    print('Total Count : ', sum(category_counts.values()))

    see_more = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div[8]/div/div/div[1]/div/div/div/div/div/a')))
    see_more.click()
    time.sleep(2)

def see_more():
    while True:
        while True:
            load_more = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[3]')))            
            break
        try:
            wait.until(EC.element_to_be_clickable(load_more))
            ActionChains(driver).move_to_element(load_more).click(load_more).perform()
            time.sleep(3)
        except Exception:
            driver.execute_script('window.scrollBy(0, 500);')
            print('Unable to click the LOAD MORE')
            time.sleep(1)
            break

    category_count = {}
    items = driver.find_elements(By.CLASS_NAME, 'rtwpvg-product')
    for item in items:
        category = item.find_element(By.CLASS_NAME, 'product-cat').text.strip()
        category_count[category] = category_count.get(category, 0) + 1
    
    print('All Products (Grouped by Category) : ', category_count)
    print('Total Count : ', sum(category_count.values()))

def add_to_cart():
    add_cart = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[2]/div/div/div[2]/ul/li[11]/div/div[3]/div/div/a')))
    wait.until(EC.element_to_be_clickable(add_cart))
    ActionChains(driver).move_to_element(add_cart).click(add_cart).perform()
    time.sleep(5)

    view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/p/a[1]')))
    view_cart.click()
    time.sleep(4)

    add_quantity = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/div/div/div/form/table/tbody/tr/td[5]/div/div/div/button[2]')))
    add_quantity.click()
    time.sleep(4)

    driver.save_screenshot('add_quantity.png')

    remove_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/div/div/div/form/table/tbody/tr/td[1]/div/a')))
    remove_cart.click()
    time.sleep(4)

    driver.save_screenshot('empty_cart.png')

def return_to_home():
    return_home = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/div/div/div/p/a')))
    return_home.click()
    time.sleep(4)

    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div/div[3]/form/div/div/input')))
    search_word = 'organic'
    search_box.send_keys(search_word)
    time.sleep(4)

    driver.save_screenshot('search_suggestion.png')

    suggestions = driver.find_elements(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div/div[3]/div/div/ul')
    suggestions_count = len(suggestions)
    suggestions_names = [s.text.strip() for s in suggestions]

    print('Search Suggestions (Count) : ', suggestions_count)
    print('Search Suggestions (Items) : ', suggestions_names)

def main():
    navigate_to_trending_products()
    see_more()
    add_to_cart()
    return_to_home()

main()

