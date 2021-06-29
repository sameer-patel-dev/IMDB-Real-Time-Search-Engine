from scraper import Scraper

class Search:

    def __init__(self):
        """Initialize the iMDB top 1000 search object
        """
        self.imdb_scraper = Scraper()
        self.imdb_scraper.startScraper()


        print("==================== WELCOME TO IMDB's Search Engine =================")
        print("Type any genre")
        print("Type 'bye' to Quit.")


    def searchQuery(self, search_terms):
        # split the search term by '&'
        search_array = search_terms.split('&')
        cleaned_array = [ word.strip().lower() for word in search_array ]
        
        return self.imdb_scraper.search_graph.findCommonNeighbors(cleaned_array)


    def startSearch(self):
        while True:
            search_words = str(input("Search: "))

            if search_words.strip() == "bye": 
                print("Bye!")
                break
            
            movie_list = self.searchQuery(search_words)

            if len(movie_list) == 0: 
            	print("Sorry we could not find anything.")
            
            else: 
            	i = 0
            	for movie in movie_list:
            		if i < 11:
            			print(str(i+1) + ". " + movie.title())
            			i+=1

            		else:
            			break




if __name__ == "__main__":
    search = Search()
    search.startSearch()