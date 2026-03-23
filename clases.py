import random

# Clase participante (sin cambios)
class Participante:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def es_mayor_edad(self):
        return self.edad >= 18


# Clase Taller
class Taller:
    # Añadimos 'costo' para saber cuánto cobrar
    def __init__(self, nombre, limite_asistentes, costo):
        self.nombre = nombre
        self.limite_asistentes = limite_asistentes
        self.costo = costo
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

    # NUEVO: Pasarela de pago simulada
    def procesar_pago(self, participante, monto):
        print(f"Procesando pago de ${monto} para {participante.nombre}...")
        # Simulamos que el 80% de las veces el pago es exitoso
        exito = random.random() < 0.8 
        if exito:
            print("Pago exitoso.")
        else:
            print("Error: Fondos insuficientes o tarjeta rechazada.")
        return exito

    # MODIFICADO: Solo inscribe si el pago es exitoso
    def registrar_participante_en_taller(self, participante, taller):
        if taller in self.talleres:
            # Verificar edad y cupos ANTES de cobrar
            if not participante.es_mayor_edad():
                print(f"{participante.nombre} no puede inscribirse: Es menor de edad.")
                return False
            
            if taller.cupos_disponibles() <= 0:
                print(f"No hay cupos disponibles en el taller '{taller.nombre}'.")
                return False

            # Si hay cupo y es mayor de edad, procesamos el pago
            if self.procesar_pago(participante, taller.costo):
                return taller.inscribir_participante(participante)
            else:
                print(f"Inscripción cancelada para {participante.nombre} por fallo en el pago.")
                return False
                
        print("El taller no existe en el sistema.")
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