from Modelos.Candidato import Candidato


class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")

    def index(self):
        print("Listar todos los candidatos")

    def create(self, elEstudiante):
        print("Crear un candidato")

    def show(self, id):
        print("Mostrando un candidato con id ", id)

    def update(self, id, elCandidato):
        print("Actualizando candidato con id ", id)

    def delete(self, id):
        print("Elimiando candidato con id ", id)
