from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido


class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listar todos los candidatos")
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        print("Crear un candidato")
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        print("Mostrando un candidato con id ", id)
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        print("Actualizando candidato con id ", id)
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.resolucion = infoCandidato["resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        print("Elimiando candidato con id ", id)
        return self.repositorioCandidato.delete(id)

    """
    Relación Partido y Candidato
    """
    def asignarPartido(self,id,id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido=partidoActual
        return self.repositorioCandidato.save(candidatoActual)