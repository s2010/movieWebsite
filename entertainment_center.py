import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story","a story of a boy and his toys that come to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710"
                        ,"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marin on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/101/MPW-50968",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

inside_out = media.Movie("Inside out", "Inside Out a comedy-adventure set inside the mind of an 11-year old",
                     "https://www.google.com.sa/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwi4xt2p3NPTAhVCRhQKHUTaArgQjRwIBw&url=http%3A%2F%2Fcollider.com%2Finside-out-french-posters-cannes-film-festival%2F&psig=AFQjCNHtC79IhkmXLRG61EzhsR4FwJ4ZaQ&ust=1493900805649187",
                     "https://www.youtube.com/watch?v=_MC3XuMvsDI")

#print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story,avatar,inside_out]
fresh_tomatoes.open_movies_page(movies)
