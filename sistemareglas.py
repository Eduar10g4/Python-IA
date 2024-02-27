from reglas import *

class sistemadereglas(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.respuestas = []
    
    @Rule((reglas(tos_persistente="si")))
    def m1(self):
        pass

    @Rule((reglas(tos_persistente="no")))
    def m1(self):
        pass

    @Rule((reglas(dificultad_respirar="si")))
    def m2(self):
        pass

    @Rule((reglas(dificultad_respirar="no")))
    def m2(self):
        pass

    @Rule((reglas(fiebre_reciente="si")))
    def m3(self):
        pass

    @Rule((reglas(fiebre_reciente="no")))
    def m3(self):
        pass

    @Rule((reglas(dolor_pecho="si")))
    def m4(self):
        pass

    @Rule((reglas(dolor_pecho="no")))
    def m4(self):
        pass

    @Rule((reglas(congestion_nasal="si")))
    def m5(self):
        pass

    @Rule((reglas(congestion_nasal="no")))
    def m5(self):
        pass

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m11(self):
        self.respuestas.append('salud ok, no presenta ninguna enfermedad respiratoria')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m12(self):
        self.respuestas.append('posible infección viral o alergias.')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m13(self):
        self.respuestas.append('Puede ser un síntoma de una variedad de problemas respiratorios, incluyendo infecciones y problemas cardíacos, como neumonia o bronquitis')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m14(self):
        self.respuestas.append('El paciente presenta Bronquitis aguda')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m15(self):
        self.respuestas.append('Sugiere una infección respiratoria.')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m16(self):
        self.respuestas.append('El paciente presenta un resfriado')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m17(self):
        self.respuestas.append('infección renal aguda')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m18(self):
        self.respuestas.append('pielonefritis ')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m19(self):
        self.respuestas.append('Traumatismo')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m20(self):
        self.respuestas.append('Infección del tracto urinario')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m21(self):
        self.respuestas.append('Enfermedad renal poliquística')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m22(self):
        self.respuestas.append('Lesiones o traumas')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m23(self):
        self.respuestas.append('Tumores del sistema urinario')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m24(self):
        self.respuestas.append('Inflamación de la vejiga')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m25(self):
        self.respuestas.append('cáncer de riñón')

    @Rule(AND(reglas(tos_persistente="no")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m26(self):
        self.respuestas.append('cáncer de riñón grado 2')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m27(self):
        self.respuestas.append('Uretritis')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m28(self):
        self.respuestas.append('Enfermedades de Transmisión Sexual')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m29(self):
        self.respuestas.append('Infección renal / Otras afecciones')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m30(self):
        self.respuestas.append('Infección del Tracto Urinario / Otras afecciones')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m31(self):
        self.respuestas.append('Uretritis / Endometriosis')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m32(self):
        self.respuestas.append('Pielonefritis')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m33(self):
        self.respuestas.append('Infeccion en el riñon')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="no")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m34(self):
        self.respuestas.append('Cáncer de Riñón / Otras afeccione')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m35(self):
        self.respuestas.append('Traumatismo urinario')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m36(self):
        self.respuestas.append('Cálculos renales / Cistitis intersticial / Otras enfermedades renales')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m37(self):
        self.respuestas.append('Cáncer de riñón o vejiga')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="no")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m38(self):
        self.respuestas.append('Infección del tracto urinario grave / pielonefritis')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="no")))
    def m39(self):
        self.respuestas.append('ITU/cistitis')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="no")),(reglas(congestion_nasal="si")))
    def m40(self):
        self.respuestas.append('Cistitis Aguda')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="no")))
    def m41(self):
        self.respuestas.append('Enfermedad renal poliquística / Problemas de vejiga')

    @Rule(AND(reglas(tos_persistente="si")),(reglas(dificultad_respirar="si")),(reglas(fiebre_reciente="si")),(reglas(dolor_pecho="si")),(reglas(congestion_nasal="si")))
    def m42(self):
        self.respuestas.append('pielonefritis aguda')