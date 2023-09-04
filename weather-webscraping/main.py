from requests_html import HTMLSession

s = HTMLSession()

sehir = 'Çorum'
url = f'https://www.google.com/search?q={sehir}+havadurumu'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'})

temp = r.html.find('span#wob_tm', first=True).text
derece = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
durum = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
print(sehir, temp, derece, durum)

