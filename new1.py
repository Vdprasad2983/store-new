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
    CREATE TABLE IF NOT EXISTS storedata(USERNAME VARCHAR(50),PASSWORD VARCHAR(50),DATEOFBIRTH VARCHAR(50),MAIL VARCHAR(50),MOBILE VARCHAR(50),DATE VARCHAR(50))
    """)
cur.execute("INSERT INTO storedata(USERNAME, PASSWORD, DATEOFBIRTH, MAIL, MOBILE,DATE) VALUES (%s, %s, %s, %s, %s, %s)",('hkahfkahfkh','agkfgkah','fgak','agfgakfgakf','hkakfgakgf','gakfkah'))
st.button("submit")
