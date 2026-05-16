# Importa a funcao que VAI EXISTIR ( ainda nao existe !)
from calcu import calcula_media
import pytest

def test_media_simples () :
    # ARRANGE : tres notas conhecidas
    n1 , n2 , n3 = 8.0 , 7.0 , 9.0

    # ACT: chama a funcao
    resultado = calcula_media (n1 , n2 , n3 )
    
    # ASSERT : (8 + 7 + 2*9) / 4 = 33/4 = 8.25
    assert resultado == 8.25
