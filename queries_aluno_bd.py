from Prova_1.conexaoBD import *

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
            "FROM Aluno a, Turma t, Media_aluno_turma mt " \
            "WHERE mt.id_turma = t.id AND " \
            "mt.id_aluno = a.id AND " \
            "a.nome LIKE ?"
    return ler_bd(bd, query, ('%'+nome+'%',))


#Quantidade de aluno na turma
def ler_quant_turma(bd, id_turma):
    query = "SELECT COUNT(*) " \
            "FROM Aluno a, Turma t, Media_aluno_turma mt " \
            "WHERE mt.id_turma = t.id AND " \
            "mt.id_aluno = a.id AND " \
            "t.nome = ?"
    return ler_bd(bd, query, (id_turma,))

