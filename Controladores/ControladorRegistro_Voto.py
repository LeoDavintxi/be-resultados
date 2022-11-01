from Modelos.Registro_Voto import Registro_Voto
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioRegistro_Voto import RepositorioRegistro_Voto
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorRegistro_Voto():
    def __init__(self):
        self.repositorioRegistro_Voto = RepositorioRegistro_Voto()
        self.repositorioMesas = RepositorioMesa()
        self.repositorioCandidatos = RepositorioCandidato()
    def index(self):
        return self.repositorioRegistro_Voto.findAll()
    """
    Asignacion mesa y candidato a registro de votos
    """
    def create(self,infoRegistro_Voto,id_mesa,id_candidato):
        nuevoRegistro_Voto=Registro_Voto(infoRegistro_Voto)
        laMesa=Mesa(self.repositorioMesas.findById(id_mesa))
        elCandidato=Candidato(self.repositorioCandidatos.findById(id_candidato))
        nuevoRegistro_Voto.mesa=laMesa
        nuevoRegistro_Voto.candidato=elCandidato
        return self.repositorioRegistro_Voto.save(nuevoRegistro_Voto)
    def show(self,id):
        elRegistro_Voto=Registro_Voto(self.repositorioRegistro_Voto.findById(id))
        return elRegistro_Voto.__dict__
    """
    Modificación de registro de voto (mesa y candidato)
    """
    def update(self,id,infoRegistro_Voto,id_mesa,id_candidato):
        laRegistro_Voto=Registro_Voto(self.repositorioRegistro_Voto.findById(id))
        laRegistro_Voto.cant_votos=infoRegistro_Voto["cant_votos"]
        laMesa= Mesa(self.repositorioMesas.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laRegistro_Voto.mesa = laMesa
        laRegistro_Voto.candidato = elCandidato
        return self.repositorioRegistro_Voto.save(laRegistro_Voto)

    def delete(self, id):
        return self.repositorioRegistro_Voto.delete(id)

    "Obtener todos los registros de votos de un candidato"
    def listarVotosEnCandidato(self,id_candidato):
        return self.repositorioRegistro_Voto.getListadoVotosEnCandidato(id_candidato)

    "Obtener votos mas altos por candidato"
    def votosMasAltosPorCandidato(self):
        return self.repositorioRegistro_Voto.getMayorVotoPorCandidato()

    "Obtener promedio de votos en candidato"
    def promedioVotosEnCandidato(self,id_candidato):
        return self.repositorioRegistro_Voto.promedioVotosEnCandidato(id_candidato)












