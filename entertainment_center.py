import media
import fresh_tomatoes

#initializing movies variables

inside_out = media.Movie(
  "Inside out",
  "Inside Out a comedy-adventure set inside the mind of an 11-year old",
  "http://www.impawards.com/2015/posters/inside_out_ver10_xlg.jpg",
  "https://www.youtube.com/watch?v=_MC3XuMvsDI")

finding_dory = media.Movie(
 "Finding Dory", 
 "Inside Out a comedy-adventure set inside the mind of an 11-year old",
 "http://www.impawards.com/2016/posters/finding_dory_ver8.jpg",
 "https://www.youtube.com/watch?v=_MC3XuMvsDI")

boss = media.Movie(
 "The Boss", 
 "Inside Out a comedy-adventure set inside the mind of an 11-year old",
 "http://www.impawards.com/2016/posters/boss.jpg",
 "https://www.youtube.com/watch?v=yakeigyf0vc")

toy_story = media.Movie(
 "Toy Story",
 "a story of a boy and his toys that come to life",
 "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
 # noqa
 "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
 "Avatar", 
 "A marin on an alien planet",
 "https://www.movieposter.com/posters/archive/main/101/MPW-50968",
 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

minions = media.Movie(
"Minions",
"Inside Out a comedy-adventure set inside the mind of an 11-year old",
"http://www.impawards.com/2015/posters/minions.jpg",
"https://www.youtube.com/watch?v=eisKxhjBnZ0&spfreload=10")

# create an array that hold all initialized variables 

movies = [toy_story,avatar,minions, inside_out, finding_dory, boss]

#this function opens the movies array in the browser 
#and output all movie related info

fresh_tomatoes.open_movies_page(movies)

