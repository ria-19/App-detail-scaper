import re

# App class representing parameters to be scraped for an app.
class App:
    def __init__(self, soup):
        self.Age = soup.select_one('#roundup_infobox_age .data').getText()
        self.OverallRatings = self.__rating__(soup)
        self.GlobalRanking = soup.select_one('#roundup_infobox_ranking .data').getText()
        self.Description = soup.select_one('div[itemprop="description"]').getText()[:50]
        sElem = soup.select('img[class="primary_screenshots"]')
        self.Urls = [ i.get('src') for i in sElem]
    
    # Helper method to modifiy the overall rating result inot required format.
    def __rating__(self, soup):
        overallratings = soup.select_one('#roundup_infobox_rating .data').getText()
        ratingRegex = re.compile(r'(.*)(with average of)')
        rating = ratingRegex.search(overallratings)
        return rating.group(1)
        
        

       
