import requests
from bs4 import BeautifulSoup

def scrape():

    
    url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2 C283&ref=sr_pg_1' 
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
    response = requests.get(url, headers=headers)
   



    soup = BeautifulSoup(response.content, 'html.parser')
   

    
    products = soup.find_all('div', {'class': 'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right'})
    
    scraped_data = []
    count=0

    
    for product in products:
      if count<=2:
       url= product.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href')
       product_url='https://amazon.in/' + url
       title=product.find('span',{'class':'a-size-medium a-color-base a-text-normal'}).text.strip()
       price=product.find('span',{'class':'a-price-whole'}).text.strip()
       rating=product.find('span',{'class':'a-icon-alt'}).text.strip()
       views=product.find('span',{'class':'a-size-base s-underline-text'}).text.strip()
       scraped_data.append({'title': title, 'price': price,'rating':rating, 'views': views,'product_url':product_url})
       
       count=count+1
    


    # for product in products:
    #     title = product.find('').text.strip()
    #     price = soup.find_all('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    #     print('hello')
    #     print(product)
    #     image_url = product.find('img')['src']
        
    #     scraped_data.append({'title': title, 'price': price, 'image_url': image_url})
    
    
    return scraped_data
