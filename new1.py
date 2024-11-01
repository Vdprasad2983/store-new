import psycopg2
import streamlit as st
DB_HOST="dpg-csbgohjtq21c73a07ldg-a"
DB_NAME="database_mu99"
DB_USER="database_mu99_user"
DB_PASS="RG7Kxj2eysolMAG77wRo5sJCerXVxdeq"
DB_PORT="5432"
conn=psycopg2.connect(host=DB_HOST,
                      database=DB_NAME,
                      user=DB_USER,
                      password=DB_PASS,
                      port=DB_PORT)
cur=conn.cursor()
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS storedata(USERNAME TEXT(50),PASSWORD TEXT(50),DATEOFBIRTH TEXT(50),MAIL TEXT(50),MOBILE TEXT(50),DATE TEXT(50))
    """)
cur.execute("INSERT INTO storedata VALUES (?,?,?,?,?,?)",('hkahfkahfkh','agkfgkah','fgak','agfgakfgakf','hkakfgakgf','gakfkah'))
st.button("submit")