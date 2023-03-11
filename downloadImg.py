import os
import requests

def downloadImg(img, url):
    # image_name = 'test1.jpg'
    # url = 'http://example.com/image.jpg'
    os.chdir('C:\\users\\Olorunfemi\\Desktop\\AngularProjects\\paysecure\\src\\assets\\images\\pybanks')
    r = requests.get(url, stream=True)
    with open(img, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

banks = [
    {
      "name": "Access Bank",
      "slug": "access-bank",
      "code": "044",
      "ussd": "*901#"
    },
    {
      "name": "Access Bank (Diamond)",
      "slug": "access-bank-diamond",
      "code": "063",
      "ussd": "*426#"
    },
    {
      "name": "ALAT by WEMA",
      "slug": "alat-by-wema",
      "code": "035A",
      "ussd": "*945*100#"
    },
    {
      "name": "ASO Savings and Loans",
      "slug": "asosavings",
      "code": "401",
      "ussd": ""
    },
    {
      "name": "Bowen Microfinance Bank",
      "slug": "bowen-microfinance-bank",
      "code": "50931",
      "ussd": ""
    },
    {
      "name": "CEMCS Microfinance Bank",
      "slug": "cemcs-microfinance-bank",
      "code": "50823",
      "ussd": ""
    },
    {
      "name": "Citibank Nigeria",
      "slug": "citibank-nigeria",
      "code": "023",
      "ussd": ""
    },
    {
      "name": "Ecobank Nigeria",
      "slug": "ecobank-nigeria",
      "code": "050",
      "ussd": "*326#"
    },
    {
      "name": "Ekondo Microfinance Bank",
      "slug": "ekondo-microfinance-bank",
      "code": "562",
      "ussd": "*540*178#"
    },
    {
      "name": "Fidelity Bank",
      "slug": "fidelity-bank",
      "code": "070",
      "ussd": "*770#"
    },
    {
      "name": "First Bank of Nigeria",
      "slug": "first-bank-of-nigeria",
      "code": "011",
      "ussd": "*894#"
    },
    {
      "name": "First City Monument Bank",
      "slug": "first-city-monument-bank",
      "code": "214",
      "ussd": "*329#"
    },
    {
      "name": "Globus Bank",
      "slug": "globus-bank",
      "code": "00103",
      "ussd": "*989#"
    },
    {
      "name": "Guaranty Trust Bank",
      "slug": "guaranty-trust-bank",
      "code": "058",
      "ussd": "*737#"
    },
    {
      "name": "Hasal Microfinance Bank",
      "slug": "hasal-microfinance-bank",
      "code": "50383",
      "ussd": "*322*127#"
    },
    {
      "name": "Heritage Bank",
      "slug": "heritage-bank",
      "code": "030",
      "ussd": "*322#"
    },
    {
      "name": "Jaiz Bank",
      "slug": "jaiz-bank",
      "code": "301",
      "ussd": "*389*301#"
    },
    {
      "name": "Keystone Bank",
      "slug": "keystone-bank",
      "code": "082",
      "ussd": "*7111#"
    },
    {
      "name": "Kuda Bank",
      "slug": "kuda-bank",
      "code": "50211",
      "ussd": ""
    },
    {
      "name": "One Finance",
      "slug": "one-finance",
      "code": "565",
      "ussd": "*1303#"
    },
    {
      "name": "Parallex Bank",
      "slug": "parallex-bank",
      "code": "526",
      "ussd": "*322*318*0#"
    },
    {
      "name": "PayCom",
      "slug": "paycom",
      "code": "100004",
      "ussd": "*955#"
    },
    {
      "name": "Polaris Bank",
      "slug": "polaris-bank",
      "code": "076",
      "ussd": "*833#"
    },
    {
      "name": "Providus Bank",
      "slug": "providus-bank",
      "code": "101",
      "ussd": ""
    },
    {
      "name": "Rubies MFB",
      "slug": "rubies-mfb",
      "code": "125",
      "ussd": "*7797#"
    },
    {
      "name": "Sparkle Microfinance Bank",
      "slug": "sparkle-microfinance-bank",
      "code": "51310",
      "ussd": ""
    },
    {
      "name": "Stanbic IBTC Bank",
      "slug": "stanbic-ibtc-bank",
      "code": "221",
      "ussd": "*909#"
    },
    {
      "name": "Standard Chartered Bank",
      "slug": "standard-chartered-bank",
      "code": "068",
      "ussd": ""
    },
    {
      "name": "Sterling Bank",
      "slug": "sterling-bank",
      "code": "232",
      "ussd": "*822#"
    },
    {
      "name": "Suntrust Bank",
      "slug": "suntrust-bank",
      "code": "100",
      "ussd": "*5230#"
    },
    {
      "name": "TAJ Bank",
      "slug": "taj-bank",
      "code": "302",
      "ussd": "*898#"
    },
    {
      "name": "TCF MFB",
      "slug": "tcf-mfb",
      "code": "51211",
      "ussd": "*908#"
    },
    {
      "name": "Titan Trust Bank",
      "slug": "titan-trust-bank",
      "code": "102",
      "ussd": "*922#"
    },
    {
      "name": "Union Bank of Nigeria",
      "slug": "union-bank-of-nigeria",
      "code": "032",
      "ussd": "*826#"
    },
    {
      "name": "United Bank For Africa",
      "slug": "united-bank-for-africa",
      "code": "033",
      "ussd": "*919#"
    },
    {
      "name": "Unity Bank",
      "slug": "unity-bank",
      "code": "215",
      "ussd": "*7799#"
    },
    {
      "name": "VFD",
      "slug": "vfd",
      "code": "566",
      "ussd": ""
    },
    {
      "name": "Wema Bank",
      "slug": "wema-bank",
      "code": "035",
      "ussd": "*945#"
    },
    {
      "name": "Zenith Bank",
      "slug": "zenith-bank",
      "code": "057",
      "ussd": "*966#"
    }
]

for bank in banks:
    url = f'https://github.com/ichtrojan/nigerian-banks/raw/master/logos/{bank["slug"]}.png'
    downloadImg(f'{bank["slug"]}.png',url)