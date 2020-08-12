from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
# News Title and Paragraph Text.

    browser = init_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(url)

    time.sleep(1)

    html = browser.html

    soup = bs(html, "html.parser")

    divs = soup.find_all('div', class_="list_text")
    news_title = divs[0].a.text
 

    divs_p = soup.find_all('div', class_="article_teaser_body")
    news_p = divs_p[0].text

    browser.quit()

# image url for the current Featured Mars Image 

    browser = init_browser()

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url)

    time.sleep(1)

    html = browser.html

    soup = bs(html, "html.parser")

    link = soup.article['style'].split("'")[1]

    base_url = "https://www.jpl.nasa.gov"

    featured_image_url = base_url + link


    browser.quit()

# Mars Weather

    browser = init_browser()

    url = "https://twitter.com/marswxreport?lang=en"

    browser.visit(url)

    time.sleep(1)


    html = browser.html

    soup = bs(html, "html.parser")

    mars_weather = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").text.split('InSight')[1]

    browser.quit()

# Mars Facts

    import pandas as pd

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df["information"] = df[0]
    df["Mars"] = df[1]
    thedf = df.drop(columns=[0, 1])
    html_table = thedf.to_html('templates/table.html', index=False)
    


# Mars Hemispheres

    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url)

    time.sleep(1)


    browser.click_link_by_partial_text('Cerberus')

    html = browser.html

    soup = bs(html, "html.parser")

    hem_cerberus_name = soup.find('h2', class_="title").text.split(' ')[0]
  
    hem_cerberus_url = soup.find('li').a['href']
  
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url)

    time.sleep(1)

    browser.click_link_by_partial_text("Schiaparelli")

    time.sleep(1)

    html = browser.html

    soup = bs(html, "html.parser")

    hem_schia_name = soup.find('h2', class_="title").text.split(' ')[0]
   
    hem_schia_url = soup.find('li').a['href']
   
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url)

    time.sleep(1)

    browser.click_link_by_partial_text("Syrtis")

    time.sleep(1)

    html = browser.html

    soup = bs(html, "html.parser")

    hem_syrtis_name = soup.find('h2', class_="title").text.split(' ')[0]
   
    hem_syrtis_url = soup.find('li').a['href']
    
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url)

    time.sleep(1)

    browser.click_link_by_partial_text("Valles")

    time.sleep(1)

    html = browser.html

    soup = bs(html, "html.parser")

    hem_valles_name = soup.find('h2', class_="title").text.split(' ')[0]
  
    hem_valles_url = soup.find('li').a['href']
    

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": hem_valles_url},
        {"title": "Cerberus Hemisphere", "img_url": hem_cerberus_url},
        {"title": "Schiaparelli Hemisphere", "img_url": hem_schia_url},
        {"title": "Syrtis Major Hemisphere", "img_url": hem_syrtis_url}
    ]

    mars_data = {"newstitle":news_title,
        "paragraph":news_p,
        "current_feature":featured_image_url,
        "weather":mars_weather,
        "facts":html_table,
        "valles":hem_valles_url,
        "cerberus":hem_cerberus_url,
        "schiaparelli":hem_schia_url,
        "syrtis":hem_syrtis_url} 
        
    

    browser.quit()

    return  mars_data