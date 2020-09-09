from tinydb import TinyDB, Query

follower_list = [
    ("1a", "1b"), ("2a", "2b"), ("3a", "3b"), ("4a", "4b")

]
username = "soeren2000"
bb = "2000_66_7__13_12_23_54324"

path2 = ("./data/" + username + "_followers_" + bb + ".json")
db = TinyDB(path2)

db.insert({'name': 'apple', 'desc': 7})
print(db.all())
print(len(db))
