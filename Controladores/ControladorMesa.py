from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    #### Listar todos los partidos politicos ####
    def index(self):
        return self.repositorioMesa.findAll()

    #### Crear un partido politico ####
    def create(self,infoMesa):
        nuevoEstudiante=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoEstudiante)

    #### Listar un partido politico dado un ID ####
    def show(self,id):
        elEstudiante=Mesa(self.repositorioMesa.findById(id))
        return elEstudiante.__dict__

    #### Actualizar un partido politico dada un ID ####
    def update(self,id,infoEstudiante):
        estudianteActual=Mesa(self.repositorioMesa.findById(id))
        estudianteActual.num_cedulas_ins=infoEstudiante["num_cedulas_ins"]
        return self.repositorioMesa.save(estudianteActual)

    #### Eliminar un partido politico dado un ID ####
    def delete(self,id):
        return self.repositorioMesa.delete(id)

    """
        Otros metodos relacionales
    """