from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})


all_users = list(db.users.find())

print(all_users[0])
print(all_users[1])
print(all_users[2])

user = db.users.find_one({'name':'bobby'})
print(user)

user = db.users.find_one({'name':'bobby'}, {'_id':False})
print(user)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
user = db.users.find_one({'name':'bobby'}, {'_id':False})
print(user)


db.users.delete_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'}, {'_id':False})
print(user)

