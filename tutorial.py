from bs4 import BeautifulSoup
import requests
import pandas

r = requests.get("https://www.jib.co.th/web/product/product_search/")

c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class", "divboxpro"})

product_list = []

for item in all:
    product_dict = {}
    product_dict["Name"] = item.find_all("span", {"class", "promo_name"})[0].text.replace("NOTEBOOK (โน้ตบุ๊ค)","")
    product_dict["Price"] = item.find_all("p")[3].text.strip()
    product_dict["Views"] = item.find_all("p")[1].text.strip()
    product_dict["Status"] = item.find_all("p")[0].text.strip()
    product_list.append(product_dict)

df = pandas.DataFrame(product_list)
df.to_csv("output.csv")
