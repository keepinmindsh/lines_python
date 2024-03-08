from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://****:****!@127.0.0.1/lines_scrap_db"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    database = client.get_database("lines_scrap_db")

    database.create_collection("dream_index")

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['dream_index']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()
