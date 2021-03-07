class App:
    def __init__(self, soup):
        self.Age = soup.select_one('#roundup_infobox_age .data').getText()
        self.OverallRatings = soup.select_one('#roundup_infobox_rating .data').getText()
        self.GlobalRanking = soup.select_one('#roundup_infobox_ranking .data').getText()
        self.Description = soup.select_one('div[itemprop="description"]').getText()[:50]
        sElem = soup.select('img[class="primary_screenshots"]')
        self.Urls = [ i.get('src') for i in sElem]
        

       
