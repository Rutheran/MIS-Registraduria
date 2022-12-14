from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido


class ControladorPartido():
    def __init__(self):
        print("Creando Controlador Partido")
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        newPartido = Partido(infoPartido)
        return self.repositorioPartido.save(newPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)
