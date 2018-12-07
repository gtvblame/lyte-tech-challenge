
# Implementation notes

* As requirements were not strictly specified, I made my own decisions about how the API and data scheme would look like
* I decided to use Django Rest Framework, because it gives a lot of required functionality out of the box
* There is still much to improve, I could have written more tests and other staff, but I think I've done enough to demonstrate the approach


# Database

* I could have enabled Postgres or Mysql plugin on Heroku, but I decided to simply use sqlite, the db file is checked into
the repository.
* I also could have created a more complex data schema, but I decided to keep it very simple and created a single table
to satisfy the requirements. To make it, I aggregated ticket costs into minimum cost across all available tickets
for each event.
* The search is not optimal now, it doesn't use index, I could have used Sqlite FTS4 index or different option, but I was too lazy :(

# Time

This exercise took me 7 hours to implement. I spend:
* 1 hour researching Heroku
* 1 hour catching up with latest Django and DRF as I haven't used them for a while
* 5 hours of coding and testing