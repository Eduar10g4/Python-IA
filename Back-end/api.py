from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="respiratory_system"
)

@app.route('/guardar_historial', methods=['POST', 'GET'])
def guardar_historial():
    if request.method == 'POST':
        data = request.json
        nombre = data.get('Nombre')
        apellido = data.get('Apellido')
        cedula = data.get('Cedula')
        tos_persistente = data.get('¿Tiene tos persistente?')
        dificultad_respirar = data.get('¿Experimenta dificultad para respirar?')
        fiebre_reciente = data.get('¿Ha tenido fiebre recientemente?')
        dolor_pecho = data.get('¿Ha experimentado dolor en el pecho?')
        congestion_nasal = data.get('¿Ha tenido congestión nasal o secreción nasal?')
        respuestas = data.get('respuestas')

        # Insertar datos del usuario
        mycursor = mydb.cursor()
        sql_usuario = "INSERT INTO usuario (nombre, apellido, cedula) VALUES (%s, %s, %s)"
        val_usuario = (nombre, apellido, cedula)
        mycursor.execute(sql_usuario, val_usuario)
        mydb.commit()

        # Obtener el ID del usuario insertado
        usuario_id = mycursor.lastrowid

        # Insertar datos de las preguntas
        sql_preguntas = "INSERT INTO consulta (tos_persistente, dificultad_respirar, fiebre_reciente, dolor_pecho, congestion_nasal) VALUES (%s, %s, %s, %s, %s)"
        val_preguntas = (tos_persistente, dificultad_respirar, fiebre_reciente, dolor_pecho, congestion_nasal)
        mycursor.execute(sql_preguntas, val_preguntas)
        mydb.commit()

        # Obtener el ID de las preguntas insertadas
        preguntas_id = mycursor.lastrowid

        # Insertar datos de las respuestas
        sql_respuestas = "INSERT INTO respuesta (usuario_id, preguntas_id, respuesta) VALUES (%s, %s, %s)"
        for respuesta in respuestas:
            val_respuestas = (usuario_id, preguntas_id, respuesta)
            mycursor.execute(sql_respuestas, val_respuestas)
            mydb.commit()

        mycursor.close()

        return jsonify({"message": "Historial guardado exitosamente"})
    elif request.method == 'GET':
     cedula = request.args.get('cedula')

    if cedula:
        # Consulta SQL para obtener los datos del usuario y sus respuestas
        sql = "SELECT usuario.nombre, usuario.apellido, respuesta.respuesta \
                FROM usuario \
                INNER JOIN respuesta ON usuario.id = respuesta.usuario_id \
                WHERE usuario.cedula = %s"
        val = (cedula,)
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sql, val)
        data = mycursor.fetchall()
        mycursor.close()

        return jsonify(data)
    else:
        return jsonify({"error": "Debe proporcionar el parámetro 'cedula'"}), 400

if __name__ == '__main__':
    app.run(debug=True)
