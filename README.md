## IMDB Real Time Search Engine

In this problem, you have to build a small knowledge base about the top N movies listed on IMDb Charts and provide a mechanism to query the same.
Your program should accept N as an input parameter and do the following:
  - Fetch the list of top N movies from the IMDb website and build an in-memory knowledge base comprising of the names of movies, the names of the cast of each movie
  - This should be built at runtime and stored in a suitable data-structure of your choice.
  - Provide a query interface to query this knowledge base by actor’s name. For a given actor and a number M (< N), it should return the top M movies they have acted in.
