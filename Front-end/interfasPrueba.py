import sys
import requests
import json
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from interfaz import Ui_Dialog  # Importa la clase generada desde el archivo interfaz.py
from sistemareglas import *  # Importa la clase que contiene el sistema de reglas


class MiApp(QDialog):
    def __init__(self):
        super().__init__()
        
        # Configura la interfaz de usuario
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

         # Conectar la señal clicked del botón "Aceptar" del buttonBox a la función ejecutar_sistema
        self.ui.buttonBox.button(self.ui.buttonBox.Ok).clicked.connect(self.ejecutar_sistema)

    def ejecutar_sistema(self):
        # Crear una instancia del motor de reglas
        engine = sistemadereglas()
        engine.reset()

        # Obtener las respuestas de la interfaz de usuario
        nombre = self.ui.lineEdit.text()


        v_tos_persistente = "si" if self.ui.checkBox.isChecked() else ("no" if self.ui.checkBox_2.isChecked() else "")
        print("Respuesta Tos Persistente:", v_tos_persistente)

        v_dificultad_respirar = "si" if self.ui.checkBox_3.isChecked() else ("no" if self.ui.checkBox_4.isChecked() else "")
        print("Respuesta Dificultad para Respirar:", v_dificultad_respirar)

        v_fiebre_reciente = "si" if self.ui.checkBox_5.isChecked() else ("no" if self.ui.checkBox_6.isChecked() else "")
        print("Respuesta Fiebre Reciente:", v_fiebre_reciente)

        v_dolor_pecho = "si" if self.ui.checkBox_7.isChecked() else ("no" if self.ui.checkBox_8.isChecked() else "")
        print("Respuesta Dolor en el Pecho:", v_dolor_pecho)

        v_congestion_nasal = "si" if self.ui.checkBox_9.isChecked() else ("no" if self.ui.checkBox_10.isChecked() else "")
        print("Respuesta Congestión Nasal o Secreción Nasal:", v_congestion_nasal)


        # Agregar los hechos al motor de reglas
        engine.declare(reglas(
            tos_persistente=v_tos_persistente,
            dificultad_respirar=v_dificultad_respirar,
            fiebre_reciente=v_fiebre_reciente,
            dolor_pecho=v_dolor_pecho,
            congestion_nasal=v_congestion_nasal
        ))

        # Crear un diccionario con los datos del resultado actual
        resultado_dict = {
            "Nombre": nombre,
            "¿Tiene tos persistente?": v_tos_persistente,
            "¿Experimenta dificultad para respirar?": v_dificultad_respirar,
            "¿Ha tenido fiebre recientemente?": v_fiebre_reciente,
            "¿Ha experimentado dolor en el pecho?": v_dolor_pecho,
            "¿Ha tenido congestión nasal o secreción nasal?": v_congestion_nasal,
            #"respuestas": engine.respuestas
        }

        # Ejecutar el sistema de reglas
        engine.run()

        """""
        # Agregar las respuestas del motor de reglas al diccionario
        resultado_dict["respuestas"] = engine.respuestas

        url = 'http://localhost:5000/guardar_historial'
        try:
             # Realizar la solicitud GET
             response = requests.get(url)

            # Verificar si la solicitud fue exitosa
             if response.status_code == 200:
                historial_data = response.json()
                for registro in historial_data:
                    print(registro)
                QMessageBox.information(self, "Consulta Exitosa", "Historial consultado correctamente.")
             else:
                QMessageBox.warning(self, "Error", f"Error al obtener los datos del historial: {response.status_code}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error durante la solicitud GET: {e}")       
        
         """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    ventana.show()
    sys.exit(app.exec_())
