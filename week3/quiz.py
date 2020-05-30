from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##
# quiz1
search_movie = db.movies.find_one({'title':'매트릭스'}, {'_id':False})
print(search_movie['star'])
search_point = search_movie['star']

# # quiz2
same_point_movies = db.movies.find({'star':search_point},{'_id':False})
for movie in same_point_movies:
    print(movie['title'])
    # print(movie)

# quiz3
# same_point_movies = db.movies.find({'star':search_point},{'_id':False})
# for movie in same_point_movies:
#     db.movies.update_one({'star':search_point}, {'$set':{'star':0.00}})

# same_point_movies = db.movies.find({'star':'9.39'},{'_id':False})
# for movie in same_point_movies:
#     print(movie['title'])

# quiz4, for 문을 사용하지 않고 pymongo 만을 사용해서 (검색이용)하여 9.7보다 높은 영화를 찾기
