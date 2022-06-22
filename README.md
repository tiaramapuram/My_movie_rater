# My_movie_rater
Movie rater app. 

App keeps track of movies I've watched, holds ratings information and movie information.

## Roadmap:
- ~~Create database~~
- ~~Create GET, POST movies endpoint~~
- ~~Create GET, POST ratings endpoint~~
- ~~Create ability to add additional users to database~~
- Add ability to bulk import movie details
- Analysis
    - What actors and actresses do I like?
    - What directors do I like?
    - What genre do I prefer watching?



### GET ratings endpoint example:
 ```
 [{
        "Rating_ID": 1,
        "Rating_desc": "one-time watch only",
        "Ratings": 1
    },
    {
        "Rating_ID": 2,
        "Rating_desc": "watch if bored",
        "Ratings": 5
    },
    {
        "Rating_ID": 3,
        "Rating_desc": "watch multiple times",
        "Ratings": 10
    }
    .
    .
    .
]
 ```
 ### POST movie endpoint example:
  ```
 {
    "FActor": "Michelle Yeoh", 
    "MActor": "Ke Huy Quan", 
    "Movie_ID": 8, 
    "Movie_director": "Daniel Kwan", 
    "Movie_language": "English", 
    "Movie_name": "Everything, Everywhere, All at once", 
    "Movie_series": "NA"
 }
 ```
 
 ### GET Ratings and movie info example:
 ```
 [{
        "FActor": "Scarlett Johanson",
        "MActor": "NA",
        "Movie_ID": 2,
        "Movie_director": "Cate Shortland",
        "Movie_language": "English",
        "Movie_name": "Black Widow",
        "Movie_series": "Marvel",
        "Rating_ID": 2,
        "Rating_desc": "watch if bored",
        "Ratings": 5
    }
]
```
