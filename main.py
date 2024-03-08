from pymongo import MongoClient
import datetime
import pprint


def get_client():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    connection_string = "mongodb://127.0.0.1/lines_scrap_db"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(connection_string)

    return client


def insert_database():
    client = get_client()

    database = client.get_database("lines_scrap_db")

    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }

    database_get_collection = database.get_collection("dream_index")

    database_get_collection.insert_one(post)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['dream_index']


def insert_many_database():
    client = get_client()

    database = client.get_database("lines_scrap_db")

    new_posts = [
        {
            "author": "Mike",
            "text": "Another post!",
            "tags": ["bulk", "insert"],
            "date": datetime.datetime(2009, 11, 12, 11, 14),
        },
        {
            "author": "Eliot",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45),
        },
    ]

    database_get_collection = database.get_collection("dream_index")

    database_get_collection.insert_many(
        new_posts
    )


def get_database():
    client = get_client()

    database = client.get_database("lines_scrap_db")

    database_get_collection = database.get_collection("dream_index")

    pprint.pprint(database_get_collection.find_one())


def get_data_with_filter(filter):
    client = get_client()

    database = client.get_database("lines_scrap_db")

    database_get_collection = database.get_collection("dream_index")

    pprint.pprint(database_get_collection.find_one(filter))


def create_database():
    client = get_client()

    database = client.get_database("lines_scrap_db")

    database.create_collection("dream_index")


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    get_database()

    get_data_with_filter({'author': 'Eliot'})

    # insert_many_database()

    # Get the database
    # dbname = insert_database()
