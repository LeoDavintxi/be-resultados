from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    #### Listar todos los partidos politicos ####
    def index(self):
        return self.repositorioPartido.findAll()

    #### Crear un partido politico ####
    def create(self,infoPartido):
        nuevoPartido=Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    #### Listar un partido politico dado un ID ####
    def show(self,id):
        elDepartamento=Partido(self.repositorioPartido.findById(id))
        return elDepartamento.__dict__

    #### Actualizar un partido politico dada un ID ####
    def update(self,id,infoDepartamento):
        PartidoActual=Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre=infoDepartamento["nombre"]
        PartidoActual.lema = infoDepartamento["lema"]
        return self.repositorioPartido.save(PartidoActual)

    #### Eliminar un partido politico dado un ID ####
    def delete(self,id):
        return self.repositorioPartido.delete(id)

    """
        Otros metodos relacionales
    """