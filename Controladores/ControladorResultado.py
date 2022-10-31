from Modelos.Resultado import Resultado
from Modelos.Partido import Partido
from Modelos.Mesa import Mesa
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorResultado():
    def __init__(self):
        print("Creando Controlador Resultado")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioPartidos = RepositorioPartido()
        self.repositorioMesas = RepositorioMesa()

    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion partido y mesa a resultados
    """
    def create(self,infoResultado,id_partido,id_mesa):
        nuevaResultado=Resultado(infoResultado)
        elPartido=Partido(self.repositorioPartidos.findById(id_partido))
        laMesa=Mesa(self.repositorioMesas.findById(id_mesa))
        nuevaResultado.partido=elPartido
        nuevaResultado.mesa=laMesa
        return self.repositorioResultado.save(nuevaResultado)

    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificación de Resultado (partido y mesa)
    """
    def update(self,id,infoResultado,id_partido,id_mesa):
        laResultado=Resultado(self.repositorioResultado.findById(id))
        #laResultado.nvotos=infoResultado["nvotos"]
        elPartido = Partido(self.repositorioPartidos.findById(id_partido))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        laResultado.partido = elPartido
        laResultado.mesa = laMesa
        return self.repositorioResultado.save(laResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)


