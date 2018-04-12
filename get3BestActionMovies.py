# Time Complexity O(n)

import json

bestMovie = {'imdb_score': -1}
secondBestMovie = {'imdb_score': -1}
thirdBestMovie = {'imdb_score': -1}

with open('imdb (1).json') as json_data:
	data_array = json.load(json_data)
	for movie_obj in data_array:
		genre_array = movie_obj.get("genre")
		if "Action" in genre_array:
			imdb_score = movie_obj.get("imdb_score")
			if(imdb_score > bestMovie.get('imdb_score')):
				thirdBestMovie = secondBestMovie
				secondBestMovie = bestMovie
				bestMovie = movie_obj
			elif(imdb_score>secondBestMovie.get('imdb_score')):
				thirdBestMovie = secondBestMovie
				secondBestMovie = movie_obj
			elif(imdb_score>thirdBestMovie.get('imdb_score')):
				thirdBestMovie = movie_obj
	
print(bestMovie.get("name"))
print(bestMovie.get("director"), "\n")
print(secondBestMovie.get("name"))
print(secondBestMovie.get("director"), "\n")
print(thirdBestMovie.get("name"))
print(thirdBestMovie.get("director"))		

