from MockDB import MockBD

import sys
sys.path.insert(0, '..')

from Prova_1.queries_aluno_bd import *


class TestAlunoDB(MockBD):

    def test_aluno_aula(self):
        codigo = "TAD0203"
        retorno_1 = [('Maria',), ('Carla',), ('Pedro',), ('Rebeca',), ('Vinicius',)]
        self.assertEqual(ler_aluno_aula(self.mock_db_config.get('bd'), codigo), retorno_1)

        codigo = "TAD0201"
        retorno_2 = []
        self.assertEqual(ler_aluno_aula(self.mock_db_config.get('bd'), codigo), retorno_2)

        codigo = "TAD0200"
        retorno_3 = []
        self.assertEqual(ler_aluno_aula(self.mock_db_config.get('bd'), codigo), retorno_3)



    def test_aluno_Media(self):
        retorno_1 = [('Carla',), ('Pedro',), ('Maria',), ('Rebeca',)]
        self.assertEqual(ler_aluno_Media_9(self.mock_db_config.get('bd')), retorno_1)



    def test_aluno_turma(self):
        codigo = "Carla"
        retorno_1 = [('Banco_de_Dados',), ('POO',), ('Circuitos_Digitais',)]
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_1)

        codigo = "Lucas"
        retorno_2 = []
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_2)

        codigo = "Bruno"
        retorno_3 = []
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_3)



    def test_quant_turma(self):
        codigo = "Banco_de_Dados"
        retorno_1 = [(5,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), codigo), retorno_1)

        codigo = "Anatomia_Dental"
        retorno_2 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), codigo), retorno_2)

        codigo = "Biologia"
        retorno_3 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), codigo), retorno_3)

