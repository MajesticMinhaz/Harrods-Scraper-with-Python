def product_url_scraper(page_link: str, serial_number: int) -> None:
    try:
        driver.switch_to.window(driver.window_handles[serial_number % 2])
        driver.get(page_link)
        time.sleep(2)

        soup = BeautifulSoup(markup=driver.page_source, features='html.parser')
        script_tags = soup.find_all(name='script')  # find all existing script tags

        tags = list(filter(lambda script_tag: re.findall(condition, script_tag.text.strip()), script_tags))
        products = None
        for tag in tags:
            products = json.loads(re.sub(condition, "", tag.text.strip()).strip()).get("entities")["products"]

        for product in products.values():
            product_url = f"https://www.harrods.com/en-ae/shopping/{product.get('slug')}"
            product_id = product.get('id')
            need_check = False
            if product.get("groupedEntries") is not None:
                need_check = True
            else:
                pass

            data = {
                "product_id": product_id,
                "product_url": product_url,
                "need_check": need_check
            }
            '''
            finally, we got our desired product url. Now we need to store this link to a safe place sa that we can use it in future. But we don't want to 
            store duplicate data to our database. That's why, we have to check that this url is already exist or not. 
            if this link is already exist, we have to pass otherwise we have to store in our database called as (harrods_product_url.json)
            '''
            if not db.contains(query.product_id == data.get('product_id')):
                db.insert(data)
                print(f"Scraped Product ID : {data.get('product_id')}")
            else:
                print(f"Product ID : {data.get('product_id')} Already Exists in Database")

    except Exception as unknown_exception:
        print(unknown_exception)


if __name__ == '__main__':
    import re
    import json
    import time
    from dotenv import dotenv_values
    from tinydb import TinyDB, Query
    import undetected_chromedriver as uc
    from bs4 import BeautifulSoup

    config = dotenv_values(dotenv_path="./.env")
    db = TinyDB("./db_files/harrods_product_url.json")
    query = Query()

    base_url = config['BASE_URL']
    chrome_options = uc.ChromeOptions()
    driver = uc.Chrome(
        driver_executable_path=config['DRIVER_PATH'],
        options=chrome_options
    )
    driver.get(base_url)
    time.sleep(2)
    driver.switch_to.new_window(type_hint='tab')
    condition = re.compile(r"(window.__PRELOADED_STATE__ = )")

    from_page_number = int(config['START_PAGE'])  # From Page
    to_page_number = int(config['END_PAGE'])  # To Page

    page_url = config['PAGE_URL']

    for page_number in range(from_page_number, to_page_number + 1):
        print(f"Currently Scraping Page Number : {page_number}")
        main_link = f"{page_url}&pageindex={page_number}"
        try:
            product_url_scraper(page_link=main_link, serial_number=page_number)
        except Exception as exception:
            print(exception)

    print("Program Finished...")
