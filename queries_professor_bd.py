from Prova_1.conexaoBD import *

#nomes das turmas que o professor da aula
def ler_professor_turma(bd, nome):
    query = "SELECT t.nome " \
            "FROM Turma t, Media_aluno_turma mat, Professor p" \
            "WHERE mat.id_turma = t.id AND" \
            "      = p.id AND" \
            "p.nome LIKE ?"
    return ler_bd(bd, query, ('%'+nome+'%',))