from MockDB import MockBD

import sys
sys.path.insert(0, '..')

from Prova_1.queries_aluno_bd import *


class TestAlunoDB(MockBD):

<<<<<<< HEAD
    def test_aluno_Media(self):
        codigo = "TAD0203"
        retorno_1 = [(9.8,)]
        self.assertEqual(ler_aluno_Media_9(self.mock_db_config.get('bd'), codigo), retorno_1)

        #Turma que não tem nenhum aluno cadastrado
        codigo = "TAD0201"
        retorno_2 = [(None,)]
        self.assertEqual(ler_aluno_Media_9(self.mock_db_config.get('bd'), codigo), retorno_2)

        #Turma que não existe
        codigo = "TAD0200"
        retorno_2 = [(None,)]
        self.assertEqual(ler_aluno_Media_9(self.mock_db_config.get('bd'), codigo), retorno_2)
=======
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
>>>>>>> fcdcd4a6747ae1e2efec60fbc45dda452df3e1f3



    def test_aluno_turma(self):
        codigo = "Carla"
<<<<<<< HEAD
        retorno_1 = [('Banco_de_Dados', 9.8,), ('POO', 7.7,), ('Circuitos_Digitais', 5.5)]
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_1)

        # aluno que não esta cadastra em nenhuma turma
=======
        retorno_1 = [('Banco_de_Dados',), ('POO',), ('Circuitos_Digitais',)]
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_1)

>>>>>>> fcdcd4a6747ae1e2efec60fbc45dda452df3e1f3
        codigo = "Lucas"
        retorno_2 = []
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_2)

<<<<<<< HEAD
        # aluno que não esta cadastrado
=======
>>>>>>> fcdcd4a6747ae1e2efec60fbc45dda452df3e1f3
        codigo = "Bruno"
        retorno_3 = []
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_3)



    def test_quant_turma(self):
<<<<<<< HEAD
        nome = "Carla"
        retorno_1 = [(3,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), nome), retorno_1)

        #Aluno não esta em nenhuma turma
        nome = "Lucas"
        retorno_2 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), nome), retorno_2)

        #Aluno não esta matriculado
        nome = "Felipe"
        retorno_3 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), nome), retorno_3)
=======
        codigo = "Banco_de_Dados"
        retorno_1 = [(5,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), codigo), retorno_1)

        codigo = "Anatomia_Dental"
        retorno_2 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), codigo), retorno_2)

        codigo = "Biologia"
        retorno_3 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), codigo), retorno_3)
>>>>>>> fcdcd4a6747ae1e2efec60fbc45dda452df3e1f3

