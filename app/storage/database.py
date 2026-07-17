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
        cpu_percent REAL,
        memory_percent REAL,
        memory_used INTEGER,
        memory_available INTEGER,
        disk_percent REAL,
        disk_used INTEGER,
        disk_free INTEGER,
        bytes_sent INTEGER,
        bytes_received INTEGER
        )
    """
    )
    #commit changes made to database
    connection.commit()
    #close connection
    connection.close()

def insert_metrics(
    metrics:dict
    )->None:
    connection = sqlite3.connect("data/sentinel.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO metrics (
    timestamp,
    cpu_percent,
    memory_percent,
    memory_used,
    memory_available,
    disk_percent,
    disk_used,
    disk_free,
    bytes_sent,
    bytes_received
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
    
    metrics["timestamp"],
    
    metrics["cpu_percent"],

    metrics["memory_percent"],
    
    metrics["memory_used"],

    metrics["memory_available"],

    metrics["disk_percent"],

    metrics["disk_used"],

    metrics["disk_free"],

    metrics["bytes_sent"],

    metrics["bytes_received"]
    
    )
    )
    connection.commit()
    connection.close()

def get_latest_metric(

)->dict:
    connection = sqlite3.connect("data/sentinel.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""
    SELECT *
    FROM metrics
    ORDER BY id DESC
    LIMIT 1;
    
    """)
    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return dict(row)

def get_recent_metrics(
    limit
    )->list[dict]:
    
    connection = sqlite3.connect("data/sentinel.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM metrics
    ORDER BY id DESC
    LIMIT (?)

    """, (limit,)
    )
    rows = cursor.fetchall()
    connection.close()
    
    return [dict(row) for row in rows]
