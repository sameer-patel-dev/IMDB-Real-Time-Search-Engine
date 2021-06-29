import requests
import time
from graph import Graph
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        #print("Initializing Top 100 Movies Scraper...")
        self.top_movie_links = list()
        self.search_graph = Graph()
    

    def getRequest(self, url):
        try:
            r = requests.get(url)
            return r.status_code, r.text
            
        except requests.exceptions.RequestException as ex:
            print("Request Error: " + str(ex))
    

    def scrapeTopListing(self, html):
        soup = BeautifulSoup(html, "html.parser")

        movies_listing = soup.find_all("span", class_="lister-item-header")
        for movie in movies_listing:

            # extract movie links
            title = movie.find("a")
            title_text = title.text.strip().lower()
            link = title['href']

            # add the link to links list
            self.top_movie_links.append((title_text, link))


    def getTopMoviesListing(self):
        top_movies_url = "http://www.imdb.com/search/title"

        # iterate through the listings page (20) to get all the movies
        for i in range(1, 2):
            url = top_movies_url + "?groups=top_1000&sort=user_rating&view=simple&page=" + str(i) + "&ref_=adv_nxt"
            print("Scraping Top 1000 Page: " + url)
            status_code, html = self.getRequest(url)

            # scrape the page
            self.scrapeTopListing(html)

    
    
    def scrapeMoviePage(self, movie_title, html):
        soup = BeautifulSoup(html, "html.parser")
        movie_details = soup.find_all("span", class_="ipc-chip__text")
        
        print("Scraping Movie Page for: " + movie_title)
        return [(details.text.strip().lower(), movie_title) for details in movie_details]
    
    
    
    def extractAddMovieDetails(self):
        for movie_title, link in self.top_movie_links:

            # scrape the movie page for details
            status_code, html = self.getRequest("http://www.imdb.com" + link)

            # get a list of tuples for (movie detail, movie title) to add to graph
            movie_connections = self.scrapeMoviePage(movie_title, html)
            print(movie_connections)

            self.search_graph.addConnections(movie_connections)
        
        # once all movies are extracted into search graph, pickle for later use
        self.search_graph.saveGraph()

    

    def startScraper(self):
        # if the search graph has already been scraped and pickled, skip
        if self.search_graph.is_pickled == True: return

        # Request the top 1000 movies page
        self.getTopMoviesListing()

        # Extract relevant details from each movie page and add to the search graph
        self.extractAddMovieDetails()