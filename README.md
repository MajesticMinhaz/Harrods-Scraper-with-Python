<p align="center"><img src="https://img.shields.io/badge/Version-1.0.1-blue"></p>
<p align="center">
  <a href="https://github.com/mdminhaz2003">
    <img src="https://img.shields.io/github/followers/mdminhaz2003?label=Follow&style=social">
  </a>
  <a href="https://github.com/mdminhaz2003/Telegram-Scraper">
    <img src="https://img.shields.io/github/stars/mdminhaz2003/Telegram-Scraper?style=social">
  </a>
</p>
<p align="center" style="font-family: 'Fantasy';">
  www.harrods.com website scraper
</p>
<p align="center">
</p>

---

Requirements
============
* Python
* Git

Build
=====
To build and run this application locally, you'll need latest versions of Git, and Python From your command line:


### Clone this repository
```commandline
git clone https://github.com/mdminhaz2003/Harrods-Scraper-with-Python.git
```

### Go into the repository
```commandline
cd Harrods_Scraper_with_Python
```
### .env file structure
```text
BASE_URL=https://www.harrods.com/en-ae/         # Base path should not be changed.
PAGE_URL=https://www.harrods.com/en-ae/shopping/beauty?icid=megamenu_shop_beauty_beauty_view-all-beauty     # Enter your page url here
START_PAGE=1    # Page start
END_PAGE=3      # Page End
DRIVER_PATH=./chrome_driver/linux_64/chromedriver   # Enter your chrome driver path for Mac or Linux
OUTPUT_CSV_PATH=./output_csv/harrods_product_info.csv   # Enter your output CSV file path
```
### Requirements installing
```commandline
python3 -m pip install -r requirements.txt
```
### Scrap only product URL
```commandline
python3 harrods_url_scraper.py
```
### Scrap Product Details
```commandline
python3 harrods_product_scraper.py
```
### Scrap Special Product Details
```commandline
python3 harrods_special_product_scraper.py
```
### Finally, we will get a JSON file [./db_files/harrods_product_info.json](https://github.com/mdminhaz2003/Harrods-Scraper-with-Python/blob/master/db_files/harrods_product_info.json)
```json
{
    "_default": {
        "1": {
            "Handle": [
                {
                    "value": "14790873"
                },
                {
                    "value": "14790873"
                },
                {
                    "value": "14790873"
                }
            ],
            "Title": [
                {
                    "value": "The Special Mask (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "This amazing textured mask lifts, tones and plumps skin. Providing a healthy looking skin, it refines its texture and illuminates the complexion. Skin stays fresh, clear and matte. Enriched in Triple Collagen, QAI® and lifting and purifying agents, it livens up dull and tired skin.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "EVIDENS DE BEAUTÉ"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "The Special Mask (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Skincare, Face Masks & Treatments"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/evidens-de-beaute-the-special-mask-50ml-14790873"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/14/79/08/73/14790873_27961776_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/14/79/08/73/14790873_27961778_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "702.66"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "The Special Mask (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/14/79/08/73/14790873_27961776_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "2": {
            "Handle": [
                {
                    "value": "14791300"
                },
                {
                    "value": "14791300"
                },
                {
                    "value": "14791300"
                }
            ],
            "Title": [
                {
                    "value": "Blue Sapphire Perfume (100ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Inspired by the 65th wedding anniversary of Queen Elizabeth II and Prince Philip, Blue Sapphire is an opulent pure perfume from Boadicea the Victorious.  Top notes of lemon, orange and green accord provide an exhilarating welcome before rose, cardamom and Indian jasmine give the scent a luxurious overtone – underlined by a base of oud, patchouli and soft amber to maintain a sensuous quality of indulgent luxury.  Presented in a stunning royal blue glass falcon that hints at the mysterious beauty of the gemstone, it features the signature Boadicea The Victorious pewter, this time plated in gold and adorned with a certified blue sapphire stone.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "BOADICEA THE VICTORIOUS"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Blue Sapphire Perfume (100ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Womens Perfume"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/boadicea-the-victorious-blue-sapphire-perfume-100ml-14791300"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/14/79/13/00/14791300_39730226_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/14/79/13/00/14791300_39729176_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "2572.99"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Blue Sapphire Perfume (100ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/14/79/13/00/14791300_39730226_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "3": {
            "Handle": [
                {
                    "value": "14799253"
                },
                {
                    "value": "14799253"
                }
            ],
            "Title": [
                {
                    "value": "Baccarat Rouge 540 Eau de Parfum (70ml)"
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Baccarat Rouge 540 is an eau de parfum born from the encounter between Maison Francis Kurkdjian and Baccarat, as a celebration of the 250th anniversary of the iconic crystal house. A unique oriental floral fragrance suitable for both men and women, it lays on the skin like a floral and woody breeze where the aerial notes of jasmine and the radiance of saffron carry mineral facets of ambergris and woody tones of freshly cut cedarwood.\n"
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "MAISON FRANCIS KURKDJIAN"
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Baccarat Rouge 540 Eau de Parfum (70ml)"
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Womens Perfume"
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/maison-francis-kurkdjian-baccarat-rouge-540-eau-de-parfum-70ml-14799253"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/14/79/92/53/14799253_23616468_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "885.82"
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Baccarat Rouge 540 Eau de Parfum (70ml)"
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/14/79/92/53/14799253_23616468_2048.jpg"
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                }
            ]
        },
        "4": {
            "Handle": [
                {
                    "value": "14936576"
                },
                {
                    "value": "14936576"
                }
            ],
            "Title": [
                {
                    "value": "Baccarat Rouge 540 Eau de Parfum Travel Set"
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Take the iconic Baccarat Rouge 540 fragrance on-the-go thanks to the Maison Francis Kurkdjian Baccarat Rouge 540 Travel Set containing Globe Trotter travel spray case in gold and five refills. An Eau de Parfum in which the aerial notes of jasmine and the radiance of saffron carry the mineral facets of ambergris and woody tones of freshly cut cedar. A graphic and highly condensed signature.\n"
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "MAISON FRANCIS KURKDJIAN"
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Baccarat Rouge 540 Eau de Parfum Travel Set"
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Womens Perfume"
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/maison-francis-kurkdjian-baccarat-rouge-540-eau-de-parfum-travel-set-14936576"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/14/93/65/76/14936576_24347078_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "967.22"
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Baccarat Rouge 540 Eau de Parfum Travel Set"
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/14/93/65/76/14936576_24347078_2048.jpg"
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                }
            ]
        },
        "5": {
            "Handle": [
                {
                    "value": "15064551"
                },
                {
                    "value": "15064551"
                },
                {
                    "value": "15064551"
                },
                {
                    "value": "15064551"
                },
                {
                    "value": "15064551"
                },
                {
                    "value": "15064551"
                },
                {
                    "value": "15064551"
                },
                {
                    "value": "15064551"
                }
            ],
            "Title": [
                {
                    "value": "The Serum (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Turn fatigued skin into a healthy complexion that exudes vitality and radiance with Clé de Peau Beauté's Le Sérum. Formulated with the label’s signature ingredient - Skin-Empowering Illuminator-it will enhance your skin’s intuitive ability to repair and defend itself for a radiant, youthful look.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "CLÉ DE PEAU BEAUTÉ"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "The Serum (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Skincare, Serums"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/cle-de-peau-beaute-the-serum-50ml-15064551"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39731718_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39731727_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39730165_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39731746_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39730174_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39731755_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39730197_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "885.82"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": "5"
                },
                {
                    "value": "6"
                },
                {
                    "value": "7"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "The Serum (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/15/06/45/51/15064551_39731718_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "6": {
            "Handle": [
                {
                    "value": "15086519"
                },
                {
                    "value": "15086519"
                }
            ],
            "Title": [
                {
                    "value": "Baccarat Rouge 540 Extrait de Parfum (70ml)"
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Born from the perfumer Maison Francis Kurkdjian's mastery and time-based wisdom, Baccarat Rouge 540 is composed of three breaths that capture the fragrance's power and true radiance. Jasmine Grandiflorum from Egypt evokes the skilful hand that picked the flower to the one that transformed it into an absolute, while Moroccan bitter almond and ambergris soften on contact with a woody musk accord.\n"
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "MAISON FRANCIS KURKDJIAN"
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Baccarat Rouge 540 Extrait de Parfum (70ml)"
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Womens Perfume"
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/maison-francis-kurkdjian-baccarat-rouge-540-extrait-de-parfum-70ml-15086519"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/15/08/65/19/15086519_25191304_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": "70 ml"
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "1388.76"
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Baccarat Rouge 540 Extrait de Parfum (70ml)"
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/15/08/65/19/15086519_25191304_2048.jpg"
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                }
            ]
        },
        "7": {
            "Handle": [
                {
                    "value": "15113268"
                },
                {
                    "value": "15113268"
                },
                {
                    "value": "15113268"
                },
                {
                    "value": "15113268"
                }
            ],
            "Title": [
                {
                    "value": "Re-Plasty Age Recovery Night Cream (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Always at the forefront of ground-breaking skincare research, Helena Rubinstein continues to deliver formulas set to revolutionise any modern woman's skincare ritual with the Re-Plasty Age Recovery Night Cream. Offering the highest concentration of advanced anti-ageing activator proxylane ever formulated in a night cream – 30% to be exact – this soothing formula is designed to deliver exceptionally rapid restorative results.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "HELENA RUBINSTEIN"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Re-Plasty Age Recovery Night Cream (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Skincare, Moisturisers, Night Creams, Anti-Ageing Skincare, Anti-Ageing Creams"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/helena-rubinstein-re-plasty-age-recovery-night-cream-50ml-15113268"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/15/11/32/68/15113268_25805704_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/11/32/68/15113268_25805708_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/15/11/32/68/15113268_25805716_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "1369.38"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Re-Plasty Age Recovery Night Cream (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/15/11/32/68/15113268_25805704_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "8": {
            "Handle": [
                {
                    "value": "15169217"
                },
                {
                    "value": "15169217"
                }
            ],
            "Title": [
                {
                    "value": "Aventus Eau de Parfum (100 Ml)"
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "The family-owned fragrance powerhouse Creed is renowned for its uncanny understanding of the male nature, with that ability best captured by the decadent Aventus scent. Balancing between woody and fruity accents, this intoxicating perfume celebrates visionaries that strive for success, ensuring it becomes associated only with <em>crème de la crème</em> of gentlemen."
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "CREED"
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Aventus Eau de Parfum (100 Ml)"
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Mens Perfume"
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/creed-aventus-eau-de-parfum-100-ml-15169217"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/15/16/92/17/15169217_25801904_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": "100 ml"
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "1917.33"
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Aventus Eau de Parfum (100 Ml)"
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/15/16/92/17/15169217_25801904_2048.jpg"
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                }
            ]
        },
        "9": {
            "Handle": [
                {
                    "value": "15603464"
                },
                {
                    "value": "15603464"
                }
            ],
            "Title": [
                {
                    "value": "Aventus For Her Eau de Parfum (75ml)"
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Aventus For Her is the opulent and sensual fragrance from Creed. Inspired by some of history's most influential women, this feminine fragrance blends refreshing fruits with heady florals to create a vibrant and passionate scent, perfect for the powerful modern woman.\n"
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "CREED"
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Aventus For Her Eau de Parfum (75ml)"
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Womens Perfume"
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/creed-aventus-for-her-eau-de-parfum-75ml-15603464"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/15/60/34/64/15603464_28032177_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": "75 ml"
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "1130.38"
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Aventus For Her Eau de Parfum (75ml)"
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/15/60/34/64/15603464_28032177_2048.jpg"
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                }
            ]
        },
        "10": {
            "Handle": [
                {
                    "value": "17225889"
                },
                {
                    "value": "17225889"
                },
                {
                    "value": "17225889"
                },
                {
                    "value": "17225889"
                },
                {
                    "value": "17225889"
                }
            ],
            "Title": [
                {
                    "value": "The Double Shot Blow-Dryer Brush"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "With the aim to find an at-home alternative to overpriced salon blowouts, curly-haired founder Alli Webb created Drybar. Harnessing the power and functionality of a hairdryer, and combining that with the structure of a round brush, The Double Shot blow-dryer brush creates silky smooth, voluminous locks in one single step. The ergonomic design uses Ionic technology to reduce frizz and increase shine, while the vents and oval shape ensure maximum air flow for an effective, quick dry.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "DRYBAR"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "The Double Shot Blow-Dryer Brush"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Haircare, Hair Tools & Styling, Hair Dryers"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/drybar-the-double-shot-blow-dryer-brush-17225889"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/17/22/58/89/17225889_38733532_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/17/22/58/89/17225889_38733535_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/17/22/58/89/17225889_38733536_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/17/22/58/89/17225889_38733549_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "519.51"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "The Double Shot Blow-Dryer Brush"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/17/22/58/89/17225889_38733532_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "11": {
            "Handle": [
                {
                    "value": "17649190"
                },
                {
                    "value": "17649190"
                },
                {
                    "value": "17649190"
                },
                {
                    "value": "17649190"
                },
                {
                    "value": "17649190"
                },
                {
                    "value": "17649190"
                }
            ],
            "Title": [
                {
                    "value": "Laser Starter Kit"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "LYMA has produced the world’s only 500mW laser authorised for at-home use as part of its Laser Starter Kit – allowing you to achieve expert results from the comfort of your bathroom. The kit rejuvenates your skin from the base layer to improve muscle and fat structure, while increasing collagen production and helping to reduce the appearance of wrinkles and pigmentation.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "LYMA"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Laser Starter Kit"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Skincare, Face Masks & Treatments, Beauty Gift Sets, Skincare Gift Sets"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/lyma-laser-starter-kit-17649190"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/17/64/91/90/17649190_37014775_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/17/64/91/90/17649190_37014773_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/17/64/91/90/17649190_37014776_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/17/64/91/90/17649190_37016309_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/17/64/91/90/17649190_37015767_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "8619.02"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": "5"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Laser Starter Kit"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/17/64/91/90/17649190_37014775_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "12": {
            "Handle": [
                {
                    "value": "18000910"
                },
                {
                    "value": "18000910"
                },
                {
                    "value": "18000910"
                },
                {
                    "value": "18000910"
                },
                {
                    "value": "18000910"
                },
                {
                    "value": "18000910"
                },
                {
                    "value": "18000910"
                }
            ],
            "Title": [
                {
                    "value": "All Day All Year (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Sisley’s All Day All Year is the smartest moisturiser on the block. Consider it a protective veil, not only physically shielding skin from environmental aggressors that cause premature ageing – think UVA and UVA rays, along with blue light and pollution – but boosting the skin’s self-defence power. That’s why it’s named as such: wear it every day, all year round, on top of your usual moisturiser for a stronger skin barrier ready for whatever the next 24 hours bring.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "SISLEY"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "All Day All Year (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Skincare, Moisturisers, Day Creams, Anti-Ageing Skincare, Anti-Ageing Creams"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/sisley-all-day-all-year-50ml-18000910"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/18/00/09/10/18000910_39607980_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/00/09/10/18000910_39607986_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/00/09/10/18000910_39607983_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/00/09/10/18000910_39608583_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/00/09/10/18000910_39608582_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/00/09/10/18000910_39610794_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": "50 ml"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "1319.86"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": "5"
                },
                {
                    "value": "6"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "All Day All Year (50ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/18/00/09/10/18000910_39607980_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "13": {
            "Handle": [
                {
                    "value": "18011653"
                },
                {
                    "value": "18011653"
                },
                {
                    "value": "18011653"
                },
                {
                    "value": "18011653"
                }
            ],
            "Title": [
                {
                    "value": "Sports Car Club Eau de Parfum (100ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Penhaligon's presents its latest olfactory concoction, Sports Car Club eau de parfum, just in time for the 2022 Formula One World Championships. So, before you fasten your seat belt and start your engines, apply a healthy dose of this patchouli-enhanced aroma that evokes the scent of freshly cut grass.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "PENHALIGON'S"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Sports Car Club Eau de Parfum (100ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Womens Perfume, Mens Perfume, Unisex Perfume"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/penhaligons-sports-car-club-eau-de-parfum-100ml-18011653"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/18/01/16/53/18011653_39761345_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/01/16/53/18011653_39761350_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/01/16/53/18011653_39761348_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": "100 ml"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "629.4"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Sports Car Club Eau de Parfum (100ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/18/01/16/53/18011653_39761345_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "14": {
            "Handle": [
                {
                    "value": "18037864"
                },
                {
                    "value": "18037864"
                },
                {
                    "value": "18037864"
                },
                {
                    "value": "18037864"
                },
                {
                    "value": "18037864"
                }
            ],
            "Title": [
                {
                    "value": "Wind Flowers Eau de Parfum (75ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Inspired by movement, Wind Flowers is the latest unisex perfume from the House of Creed and a scent you'll be enamoured with. With floral and fresh tones, this eau de parfum opens with hints of sweet jasmine, Tunisian orange blossom and fruity peach before adding depth with notes of sandalwood, iris and musk.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "CREED"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Wind Flowers Eau de Parfum (75ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Perfume, Womens Perfume, Mens Perfume, Unisex Perfume"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/creed-wind-flowers-eau-de-parfum-75ml-18037864"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/18/03/78/64/18037864_38401586_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/03/78/64/18037864_38401590_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/03/78/64/18037864_38401594_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/03/78/64/18037864_38399839_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": "75 ml"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "1130.38"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Wind Flowers Eau de Parfum (75ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/18/03/78/64/18037864_38401586_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "15": {
            "Handle": [
                {
                    "value": "18120745"
                },
                {
                    "value": "18120745"
                },
                {
                    "value": "18120745"
                },
                {
                    "value": "18120745"
                },
                {
                    "value": "18120745"
                },
                {
                    "value": "18120745"
                }
            ],
            "Title": [
                {
                    "value": "Pure Gold Luxury Ritual"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "La Prairie’s scientists bring to the skin their Science of Light technology with the Pure Gold Luxury Ritual. Enriched with pure gold, this set will revitalise and replenish the skin by infusing it with radiance for a more youthful appearance.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "LA PRAIRIE"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Pure Gold Luxury Ritual"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Skincare, Beauty Gift Sets, Skincare Gift Sets, Anti-Ageing Skincare, Anti-Ageing Creams"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/la-prairie-pure-gold-luxury-ritual-18120745"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/18/12/07/45/18120745_38481295_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/12/07/45/18120745_38482000_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/12/07/45/18120745_38482003_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/12/07/45/18120745_38480509_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/12/07/45/18120745_38482014_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "8352.03"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": "5"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Pure Gold Luxury Ritual"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/18/12/07/45/18120745_38481295_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "16": {
            "Handle": [
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                },
                {
                    "value": "18164304"
                }
            ],
            "Title": [
                {
                    "value": "Radiant Rani Brightening Saffron Serum (30ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "Calling on the traditions of Ayurvedic medicine, RANAVAT’s Brightening Saffron Serum harnesses nature’s golden ingredient for its antioxidant, anti-inflammatory and antimicrobial properties. Massage this oil-like formula onto a cleansed face, neck, and décolleté for brightened, glowing skin that is soothed and even-toned thanks to the addition of turmeric and liquorice root.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "RANAVAT"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Radiant Rani Brightening Saffron Serum (30ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Skincare, Serums"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/ranavat-radiant-rani-brightening-saffron-serum-30ml-18164304"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "NO COLOUR"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683007_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683265_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683009_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38681851_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38681853_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683011_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38680369_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683014_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683012_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683013_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683134_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": "30 ml"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "560.21"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": "5"
                },
                {
                    "value": "6"
                },
                {
                    "value": "7"
                },
                {
                    "value": "8"
                },
                {
                    "value": "9"
                },
                {
                    "value": "10"
                },
                {
                    "value": "11"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Radiant Rani Brightening Saffron Serum (30ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/18/16/43/04/18164304_38683007_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        },
        "17": {
            "Handle": [
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                },
                {
                    "value": "18163443"
                }
            ],
            "Title": [
                {
                    "value": "Hermèsistible Infused Care Oil (8.5ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Body (HTML)": [
                {
                    "value": "THE CREATION\n The Hermèsistible lip collection awakens the senses with a synaesthesia of colors and scents. Made from 97% natural ingredients, Color and Scent Care Oil combines a nourishing skincare action with a fresh make-up result. Hydrated and smoothed, the lips are adorned with a light touch of color, radiant shine and an addictive fruity note.\n THE COLOR\n Pourpre Camarine is a sparkling and fruity purple, which borrows its hue from crowberries.\n THE SCENT\n Hermès perfumer, Christine Nagel has created a collection of 6 unique scents, corresponding to each color.\n The scent for Pourpre Camarine is composed of the nurturing notes of sandalwood and arnica, combined with a sparkling and fruity note of crowberry.\n TEXTURE AND FORMULATION\n Enriched with a high concentration of active ingredients, the care oil is sensory, enveloping and comfortable.\n Its plant oils form a protective, nourishing film on the lips, while the complex of emollient raw materials maintains and improves their hydration.\n THE OBJECT\n The joyful and colorful object is made from glass and enhanced with a playful jumble of letters forming the name of the collection. On the cap, the Hermès ex-libris is engraved tone-on-tone.\n"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Vendor": [
                {
                    "value": "HERMÈS"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Standardized Product Type": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Custom Product Type": [
                {
                    "value": "Hermèsistible Infused Care Oil (8.5ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Tags": [
                {
                    "value": "Beauty, Make-Up, Lips, Lip Glosses, Lip Balms"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Published": [
                {
                    "value": true
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "ID": [
                {
                    "value": "https://www.harrods.com/en-ae/shopping/hermes-hermesistible-infused-care-oil-8-5ml-18163443"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Name": [
                {
                    "value": "Color"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option1 Value": [
                {
                    "value": "06 POURPRE CAMARINE"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39099100_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39101278_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39101280_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39100562_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39100563_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39099105_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39101293_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39100568_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39101304_2048.jpg"
                },
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39100573_2048.jpg"
                }
            ],
            "Option2 Name": [
                {
                    "value": "Size"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option2 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Name": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Option3 Value": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant SKU": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Grams": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Tracker": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Qty": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Inventory Policy": [
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                },
                {
                    "value": "deny"
                }
            ],
            "Variant Fulfillment Service": [
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                },
                {
                    "value": "manual"
                }
            ],
            "Variant Price": [
                {
                    "value": "189.83"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Compare At Price": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Requires Shipping": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Taxable": [
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                },
                {
                    "value": true
                }
            ],
            "Variant Barcode": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Src": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Image Position": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                },
                {
                    "value": "5"
                },
                {
                    "value": "6"
                },
                {
                    "value": "7"
                },
                {
                    "value": "8"
                },
                {
                    "value": "9"
                },
                {
                    "value": "10"
                },
                {
                    "value": ""
                }
            ],
            "Image Alt Text": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Gift Card": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Title": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "SEO Description": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Google Product Category": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Gender": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Age Group": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / MPN": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Grouping": [
                {
                    "value": "Hermèsistible Infused Care Oil (8.5ml)"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / AdWords Labels": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Condition": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Product": [
                {
                    "value": false
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 0": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 1": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 2": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 3": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Google Shopping / Custom Label 4": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Image": [
                {
                    "value": "https://image.harrods.com/18/16/34/43/18163443_39099100_2048.jpg"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Variant Weight Unit": [
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                },
                {
                    "value": "g"
                }
            ],
            "Variant Tax Code": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Cost per item": [
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ],
            "Status": [
                {
                    "value": "active"
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                },
                {
                    "value": ""
                }
            ]
        }
    }
}
```
### Convert JSON to CSV Format
```commandline
python3 json_to_csv_converter.py
```
### Now, we will get a csv file in [./output_csv/harrods_product_info.csv](https://github.com/mdminhaz2003/Harrods-Scraper-with-Python/blob/master/output_csv/harrods_product_info.csv)
[License](https://github.com/mdminhaz2003/Harrods-Scraper-with-Python/blob/master/LICENSE.md)
========
```text
The MIT License (MIT)

Copyright (c) 2016 MD. MINHAZ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[Connect with Author](https://www.github.com/mdminhaz2003/)
========

<p align="center">
    <a href="https://www.buymeacoffee.com/mdminhaz2003"><img src="https://img.shields.io/badge/-Buy me a coffee-000000?style=for-the-badge&logo=buymeacoffee&logoColor=yellow"/></a>
    <a href="https://www.youtube.com/easycoding2021/"><img src="https://img.shields.io/badge/-Easy Coding-FF0000?style=for-the-badge&logo=YouTube&logoColor=white"/></a>
    <a href="https://www.facebook.com/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-3423A6?style=for-the-badge&logo=Facebook&logoColor=white"/></a>
    <a href="https://www.linkedin.com/in/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white"/></a>
    <a href="mailto:mdm047767@gmail.com"><img src="https://img.shields.io/badge/-Mail-D14836?style=for-the-badge&logo=Gmail&logoColor=white"/></a>
    <a href="https://instagram.com/mdminhaz2003/"><img src="https://img.shields.io/badge/-Md. Minhaz-E4405F?style=for-the-badge&logo=Instagram&logoColor=white"/></a>
    <a href="https://twitter.com/easycoding2021/"><img src="https://img.shields.io/badge/-Easy Coding-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
</p>