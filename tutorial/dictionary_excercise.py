user = {}

name = input("Enter your name : ")
age = input("Enter your age : ")
movie_list = input("Enter your favourite movies separated by comma : ").split(",")
song_list = input("Enter your favourite songs separated by comma : ").split(",")

user['name'] = name
user['age'] = age
user['fav_movies'] = movie_list
user['fav_songs'] = song_list

for key, value in user.items():
    print(f"{key} : {value}")