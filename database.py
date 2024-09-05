import sqlite3
conn = sqlite3.connect('customer_data.db')

query_to_create_table = """
CREATE TABLE CustomerDetails (
    age ING,
    flight_distance INT,
    inflight_entertainment INT,
    baggage_handling INT,
    cleanliness INT,
    departure_delay INT,
    arrival_delay INT,
    gender INT,
    customer_type INT,
    travel_type INT,
    economy INT,
    economy_plus INT,
    prediction VARCHAR(40)
)
"""

cur = conn.cursor()
cur.execute(query_to_create_table)
print("Your database and table is created")
cur.close()
conn.close()