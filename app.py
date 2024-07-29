import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)
pk = '@YykxvfW6PQvDPuHSEje'

def db_connect():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1024",
        database="tmp"
    )
    cursor = db.cursor()
    return cursor, db

cursor, db = db_connect()

# create task
@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.get_json()
    if task_data['pk'] != pk:
        return jsonify({'message': 'Invalid pk'})
    task_name = task_data['name']
    status = 'todo'
    insert_query = "INSERT INTO tasks (name, status) VALUES (%s, %s)"
    values = (task_name, status)
    try:
        cursor.execute(insert_query, values)
    except:
        cursor, db = db_connect()
        cursor.execute(insert_query, values)
    db.commit()
    return jsonify({'message': 'Task created successfully!'})

# distribute task
@app.route('/tasks/distribute', methods=['POST'])
def distribute_task():
    task_data = request.get_json()
    if task_data['pk'] != pk:
        return jsonify({'message': 'Invalid pk'})
    select_query = "SELECT * FROM tasks WHERE status='todo' ORDER BY id ASC LIMIT 1"
    try:
        cursor.execute(select_query)
    except:
        cursor, db = db_connect()
        cursor.execute(select_query)
    task = cursor.fetchone()
    print('- ' * 30)
    print('distribute: ', task[1])
    if task is None:
        return jsonify({'name': 'No Task'})
    update_query = "UPDATE tasks SET status='distributed' WHERE id=%s"
    values = (task[0],)
    cursor.execute(update_query, values)
    db.commit()
    return jsonify({'name': task[1].decode('utf-8'), 'id': task[0]})

# update task status
@app.route('/tasks/status', methods=['PUT'])
def update_task_status():
    task_data = request.get_json()
    if task_data['pk'] != pk:
        return jsonify({'message': 'Invalid pk'})
    task_status = task_data['status']
    if task_status not in ['todo', 'distributed', 'completed']:
        return jsonify({'message': 'Invalid status value!'})
    update_query = "UPDATE tasks SET status=%s WHERE id=%s"
    values = (task_status, task_data['id'])
    try:
        cursor.execute(update_query, values)
    except:
        cursor, db = db_connect()
        cursor.execute(update_query, values)
    db.commit()
    return jsonify({'message': 'Task status updated successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)

"""
CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2195 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
"""