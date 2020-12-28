from bs4 import BeautifulSoup as bs 
import requests
urlopen = requests.get('https://www.bigbasket.com/pd/40125924/bb-royal-organic-fried-grambengal-gram-dal-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop').text
soup = bs(urlopen,'html.parser')
ProductInfo = soup.find("h1", {"class": "GrE04"}).text
ProductName = ProductInfo.split(' ',1)[1].split(',')[0]
ProductName
BrandName= ProductInfo.split(' ',1)[0]
BrandName
ProducQty = ProductInfo.split(' ',1)[1].split(',')[1].strip()
ProducQty
ProductPrice = soup.find("td", {"data-qa": "productPrice"}).text.strip()
ProductPrice
ProductDesc = soup.find("div", {"class": "_26MFu"}).text.strip().split('   ')[-1:]
ProductDesc
print(ProductName)
print(BrandName)
print(ProducQty)
print(ProductPrice)
print(ProductDesc)
