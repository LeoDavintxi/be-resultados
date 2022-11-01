from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Registro_Voto import Registro_Voto

from bson import ObjectId

class RepositorioRegistro_Voto(InterfaceRepositorio[Registro_Voto]):
    def getListadoVotosEnCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    def getMayorVotoPorCandidato(self):
        query1={
                "$group": {
                    "_id": "$candidato",
                    "max": {
                        "$max": "$cant_votos"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)
    def promedioVotosEnCandidato(self,id_candidato):
        query1 = {
          "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        query2 = {
          "$group": {
            "_id": "$candidato",
            "promedio": {
              "$avg": "$cant_votos"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

