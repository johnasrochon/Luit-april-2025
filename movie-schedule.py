current_movies = {"Sinners": "12:00pm", "The Accountant2": "1:00pm", "Spiderman": "2:00pm"}

print("We are showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, " is playing at", showtime)