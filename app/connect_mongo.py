from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.songsdb
songs_collection = db.songs

song_dict1 = {"title": "Hey Joe", "artist": "Jimi Hendrix"}
song_dict2 = {"title": "Smells Like Teen Spirit", "artist":"Nirvana"}
song_dict3 = {"title": "Lugar ao Sol", "artist": "Charlie Brown Jr"}
song_dict4 = {"title": "Three Little Birds", "artist": "Bob Marley"}

