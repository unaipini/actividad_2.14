# Clase participante
class Participante:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def es_mayor_edad(self):
        return self.edad >= 18


# Clase Taller
class Taller:
    def __init__(self, nombre, limite_asistentes):
        self.nombre = nombre
        self.limite_asistentes = limite_asistentes
        self.lista_inscritos = []

    def cupos_disponibles(self):
        return self.limite_asistentes - len(self.lista_inscritos)

    def inscribir_participante(self, participante):
        if participante.es_mayor_edad() and self.cupos_disponibles() > 0:
            self.lista_inscritos.append(participante)
            return True
        return False

# Clase SistemaReservas
class SistemaReservas:
    def __init__(self):
        self.talleres = []

    def agregar_taller(self, taller):
        self.talleres.append(taller)

    def registrar_participante_en_taller(self, participante, taller):
        if taller in self.talleres:
            return taller.inscribir_participante(participante)
        return False

    def listar_participantes_taller(self, taller):
        return [p.nombre for p in taller.lista_inscritos]
    

# Clase Profesor
class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.talleres = []

    def asignar_taller(self, taller):
        if taller not in self.talleres:
            self.talleres.append(taller)
            return True
        return False