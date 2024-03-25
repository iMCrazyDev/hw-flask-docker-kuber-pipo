from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)
global is_db_init
is_db_init = False

@app.route('/update', methods=['GET'])
def update_counter():
    global is_db_init
    if not is_db_init:
        initialize_database()
    print('update_counter', request)

    action = request.args.get('action')

    if action == 'add':
        with conn.cursor() as cur:
            cur.execute("UPDATE counter SET count = count + 1;")
            conn.commit()
    elif action == 'delete':
        with conn.cursor() as cur:
            cur.execute("UPDATE counter SET count = count - 1;")
            conn.commit()

    return jsonify({'status': 'ok'})

@app.route('/get', methods=['GET'])
def get_counter():
    print('get_counter')
    global is_db_init
    if not is_db_init:
        initialize_database()
    with conn.cursor() as cur:
        cur.execute("SELECT count FROM counter;")
        count = cur.fetchone()[0]
    return jsonify({'count': count})

def initialize_database():
    global conn 
    conn = psycopg2.connect(
        dbname='RACING',
        user='HSE',
        password='ESH822',
        host='db',
        port='5229'
    )
    try:
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS counter (
                id SERIAL PRIMARY KEY,
                count INTEGER DEFAULT 0
            );
        """)
        
        cur.execute("SELECT COUNT(*) FROM counter;")
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO counter (count) VALUES (0);")
        
        conn.commit()
        print("db init/check ok")
        global is_db_init
        is_db_init = True
    except Exception as e:
        print("db init/check error", e)

if __name__ == '__main__':
    print('starting')
    app.run(host='0.0.0.0', port=5228, debug=True)
