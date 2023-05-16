from MockDB import MockBD

import sys
sys.path.insert(0, '..')
from Prova_1.queries_professor_bd import *

class TestProfessorDB(MockBD):
    def test_professor_aula(self):

        professor_1 = "Judilena"
        retorno_1 = [('Banco_de_Dados',)]
        self.assertEqual(ler_professor_turma(self.mock_db_config.get('bd'), professor_1), retorno_1)

        professor_2 = "Joao"
        retorno_2 = []
        self.assertEqual(ler_professor_turma(self.mock_db_config.get('bd'), professor_2), retorno_2)

        professor_3 = "Guilherme"
        retorno_3 = []
        self.assertEqual(ler_professor_turma(self.mock_db_config.get('bd'), professor_3), retorno_3)
