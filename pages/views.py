from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def Index_View(request):

    return render(request,'index.html', {})


def VTB_Bank_View(request):
    url = requests.get("https://vtb.ge/en/individuals/exchange-rates")
    soup = BeautifulSoup(url.content, "html.parser")
    USD = soup.find_all("tr")[1]
    info = {}
    Price_result = []
    for item in USD:
        for result in item:
            if result.isdigit:
                Price_result.append(result)


    info["VTB_bank_buy_USD"] = BuyUSD = Price_result[-2]
    info["VTB_bank_sell_USD"] = BuyUSD =  SellUSD = Price_result[-4]

    if request.POST:
        try:
            valute = request.POST['valute']

            info['USD'] = valute
            info['result_valute_vtb_bank_gel'] = float(valute) * float(info['VTB_bank_sell_USD'])
            info['result_GEL'] = "{}USD = {}GEL".format(info['USD'],info['result_valute_vtb_bank_gel'])

            info['GEL'] = valute
            info['result_valute_vtb_bank_usd'] = float(valute) / float(info['VTB_bank_buy_USD'])
            info['result_USD'] = "{}GEL = {}USD".format(info['GEL'], info['result_valute_vtb_bank_usd'])
        except:
            info['result_USD'] = "Write The Number !"

    return render(request, 'VTB_bank.html', {'info':info})

def TBC_Bank_View(request):
    url = requests.get('http://www.tbcbank.ge/web/en/exchange-rates')
    soup = BeautifulSoup(url.content, 'html.parser')
    valute = soup.find_all('div', class_='currRate')

    info = {}
    array_of_valute = [price.get_text()[8:] for price in valute]
    USD_GEL = [float(array_of_valute[0]), float(array_of_valute[1])]
    info['tbc_bank_sell_USD'] = USD_GEL[0]
    info['tbc_bank_buy_USD'] = USD_GEL[1]

    if request.POST:
        try:
            valute = request.POST['valute']

            info['USD'] = valute
            info['result_valute_tbc_bank_gel'] = float(valute) * float(info['tbc_bank_sell_USD'])
            info['result_GEL'] = "{}USD = {}GEL".format(info['USD'],info['result_valute_tbc_bank_gel'])

            info['GEL'] = valute
            info['result_valute_tbc_bank_usd'] = float(valute) / float(info['tbc_bank_buy_USD'])
            info['result_USD'] = "{}GEL = {}USD".format(info['GEL'], info['result_valute_tbc_bank_usd'])
        except:
            info['result_USD'] = "Write The Number !"
            
    return render(request, 'tbc_bank.html', {'info':info})

def Procredit_Bank_View(request):
    url = procredit_bank = requests.get('https://www.procreditbank.ge/en/exchange')
    soup_procredit_bank = BeautifulSoup(url.content, 'html.parser')

    info = {}
    info['procredit_bank_sell_USD'] = float(soup_procredit_bank.find_all('div', class_='exchange-buy')[0].get_text()[37:])
    info['procredit_bank_buy_USD'] = float(soup_procredit_bank.find_all('div', class_='exchange-sell')[0].get_text()[37:])

    if request.POST:
        try:
            valute = request.POST['valute']

            info['USD'] = valute
            info['result_valute_tbc_bank_gel'] = float(valute) * float(info['procredit_bank_sell_USD'])
            info['result_GEL'] = "{}USD = {}GEL".format(info['USD'],info['result_valute_tbc_bank_gel'])

            info['GEL'] = valute
            info['result_valute_procredit_bank_usd'] = float(valute) / float(info['procredit_bank_buy_USD'])
            info['result_USD'] = "{}GEL = {}USD".format(info['GEL'], info['result_valute_procredit_bank_usd'])
        except:
            info['result_USD'] = "Write The Number !"

    return render(request, 'procredit_bank.html', {'info':info})
