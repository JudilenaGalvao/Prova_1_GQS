from Prova_1.conexaoBD import *

<<<<<<< HEAD

#1- Maior media ja vista em uma turma de codigo TAD203
def ler_aluno_Media_9(bd, codigo):
    query = "SELECT MAX(mt.media) " \
                      "FROM Media_aluno_turma mt, Turma t " \
                      "WHERE mt.id_turma = t.id AND " \
                      "t.codigo LIKE ?"
    return ler_bd(bd, query, ('%'+codigo+'%',))



#2-nomes das turmas e media que o aluno pertence
def ler_aluno_turma(bd, nome):
    query = "SELECT t.nome, mt.media " \
=======
#nomes dos alunos que estão matriculados na turma que tem o codigo ?
def ler_aluno_aula(bd, codigo):
    query = "SELECT a.nome " \
            "FROM Aluno a, Turma t, Media_aluno_turma mt " \
            "WHERE mt.id_turma = t.id AND " \
                  "mt.id_aluno = a.id AND " \
                  "t.codigo LIKE ?"
    return ler_bd(bd, query, ('%'+codigo+'%',))


#nomes dos alunos que tem a media maior ou igual a 9.0
def ler_aluno_Media_9(bd):
    return ler_bd(bd, "SELECT a.nome "
                      "FROM Aluno a, Media_aluno_turma mt "
                      "WHERE mt.id_aluno = a.id AND "
                      "mt.media >= 9.0")


#nomes das turmas que o aluno pertence
def ler_aluno_turma(bd, nome):
    query = "SELECT t.nome " \
>>>>>>> fcdcd4a6747ae1e2efec60fbc45dda452df3e1f3
            "FROM Aluno a, Turma t, Media_aluno_turma mt " \
            "WHERE mt.id_turma = t.id AND " \
            "mt.id_aluno = a.id AND " \
            "a.nome LIKE ?"
    return ler_bd(bd, query, ('%'+nome+'%',))


<<<<<<< HEAD
#3-Quantidade de turmas cursada por um aluno
def ler_quant_turma(bd, nome):
=======
#Quantidade de aluno na turma
def ler_quant_turma(bd, id_turma):
>>>>>>> fcdcd4a6747ae1e2efec60fbc45dda452df3e1f3
    query = "SELECT COUNT(*) " \
            "FROM Aluno a, Turma t, Media_aluno_turma mt " \
            "WHERE mt.id_turma = t.id AND " \
            "mt.id_aluno = a.id AND " \
<<<<<<< HEAD
            "a.nome = ?"
    return ler_bd(bd, query, (nome,))









=======
            "t.nome = ?"
    return ler_bd(bd, query, (id_turma,))
>>>>>>> fcdcd4a6747ae1e2efec60fbc45dda452df3e1f3

