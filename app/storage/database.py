import sqlite3

def initialise_database(

)->None:
    #connect to the database
    connection = sqlite3.connect("data/sentinel.db")
    #get cursor from connection object
    cursor =  connection.cursor()
    #execute SQL query and pass to sqlite3
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        cpu_percent REAL
        )
    """)
    #commit changes made to database
    connection.commit()
    #close connection
    connection.close()

def insert_metrics(
    metrics:str
    )->None:
    connection = sqlite3.connect("data/sentinel.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO metrics
    (timestamp, cpu_percent)
    VALUES (?, ?)
    """,
    (
    
    metrics["timestamp"],
    
    metrics["cpu_percent"]

    )
    )
    connection.commit()
    connection.close()

    
    