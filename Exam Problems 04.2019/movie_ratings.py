count_movies = int(input())
max_rating = -999999
min_rating = 999999
max_rating_move = ""
min_rating_move = ""
average_rating = 0

for i in range(count_movies):
    movie_name = input()
    rating = float(input())
    average_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_rating_move = movie_name

    elif rating < min_rating:
        min_rating = rating
        min_rating_move = movie_name


print(f"{max_rating_move} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_move} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {(average_rating/count_movies):.1f}")



