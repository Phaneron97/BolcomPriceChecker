import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.co.uk/Panasonic-eneloop-BK-3MCCE-8BE-Batteries-White/dp/B00JZBX8DQ?pf_rd_p=0331ee17-1a3c-47df-90cc-487c0ff33fea&pd_rd_wg=NOAaI&pf_rd_r=6A2JFFFFCF47WQC1B1KK&ref_=pd_gw_cr_simh&pd_rd_w=Wq5vB&pd_rd_r=f9efbe6d-10bf-4978-b18d-2780cb8c6041"

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
