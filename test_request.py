import requests

TMDB_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
TMDB_API_KEY = "4a7af45dc483ea1f8ca36e39906dab4b"
TMDB_BEARER = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YTdhZjQ1ZGM0ODNlYTFmOGNhMzZlMzk5MDZkYWI0YiIsInN1YiI6IjYyZmY1ZmUxMzIzZWJhMDA4NTNhMGJkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3q2q0IAekSR1uZkgUfm16-n7r_M6z9ukj_bG8ra6NXI"
TMDB_ENDPOINT_DETAILS = "https://api.themoviedb.org/3/movie/329"

# FOR MAKING REQUESTS USING BEARER TOKEN, USE THIS THEN ADD A 'headers' PARAMETER IN THE REQUESTS.GET FUNCTION
# TMDB_PARAMS = {
#     "query": "Up"
# }
# TMDB_HEADER = {
#     "Authorization": f"Bearer {TMDB_BEARER}",
# }
# response = requests.get(url=TMDB_ENDPOINT, params=TMDB_PARAMS, headers=TMDB_HEADER)


# FOR MAKING REQUESTS USING BASIC TOKEN, USE THIS
# TMDB_PARAMS = {
#     "api_key": TMDB_API_KEY,
#     "query": "Jurassic Park"
# }

# response = requests.get(url=TMDB_ENDPOINT, params=TMDB_PARAMS)
# total_results = response.json()['total_results']
# total = 0
# print(response.json())
# for index in range(total_results):
#     data = response.json()['results'][index]['original_title']
#     print(total)
#     print(data)
#     total += 1

TMDB_PARAMS = {
    "api_key": TMDB_API_KEY
}
response = requests.get(url=TMDB_ENDPOINT_DETAILS, params=TMDB_PARAMS)
print(response.json())
