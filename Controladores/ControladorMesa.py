from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Mesa import Mesa
from Modelos.Partido import Partido


class ControladorMesa():

    def __init__(self):
        print("Creando Controlador Mesa")
        self.repositorioMesa = RepositorioMesa()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listar todas las Mesas")
        return self.repositorioMesa.findAll()

    def create(self,infoMesa):
        print("Crear una Mesa")
        nuevaMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self,id):
        print("Mostrando una Mesa con id ", id)
        laMesa=Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self,id,infoMesa):
        print("Actualizando Mesa con id ", id)
        mesaActual= Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero=infoMesa["numero"]
        mesaActual.cantidadInscritos = infoMesa["cantidadInscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self,id):
        print("Elimiando Mesa  con id ", id)
        return self.repositorioMesa.delete(id)

    """
    Relación Mesa y Partido
    """
    def asignarPartido(self, id, id_partido):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        mesaActual.partido = partidoActual
        return self.repositorioMesa.save(mesaActual)
