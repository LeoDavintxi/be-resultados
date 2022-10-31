from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositoriopartido = RepositorioPartido()

    #### Listar todos los candidatos politicos ####
    def index(self):
        return self.repositorioCandidato.findAll()

    #### Crear un candidato politico ####
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    #### Listar un candidato politico dado un ID ####
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    #### Actualizar un candidato politico dada un ID ####
    def update(self,id,infoCandidato):
        CandidatoActual=Candidato(self.repositorioCandidato.findById(id))
        CandidatoActual.nombre=infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        CandidatoActual.num_resolucion = infoCandidato["num_resolucion"]
        return self.repositorioCandidato.save(CandidatoActual)

    #### Eliminar un candidato politico dado un ID ####
    def delete(self,id):
        return self.repositorioCandidato.delete(id)

    """
    Otros metodos relacionales
    """

    #### Relación Partido y Candidato ####
    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositoriopartido.findById(id_partido))
        candidatoActual.partido= partidoActual
        return self.repositorioCandidato.save(candidatoActual)





