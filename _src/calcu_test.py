# Importa a funcao que VAI EXISTIR ( ainda nao existe !)
from calcu import calcula_media, situacao
import pytest

def test_media_simples () :
    # ARRANGE : tres notas conhecidas
    n1 , n2 , n3 = 8.0 , 7.0 , 9.0

    # ACT: chama a funcao
    resultado = calcula_media (n1 , n2 , n3 )
    
    # ASSERT : (8 + 7 + 2*9) / 4 = 33/4 = 8.25
    assert resultado == 8.25

def test_aluno_aprovado(): # Media >= 7 deve resultar em " aprovado "
    assert situacao(7.0) == "aprovado"
    assert situacao(8.5) == "aprovado"
    assert situacao(10.0) == "aprovado"

def test_aluno_em_recuperacao(): # Entre 4 e 7 ( exclusivo ): recuperacao
    assert situacao(4.0) == "recuperacao"
    assert situacao(6.9) == "recuperacao"

def test_aluno_reprovado(): # Abaixo de 4: reprovado
    assert situacao(3.9) == "reprovado"
    assert situacao(0.0) == "reprovado"
