NOTA_MIN = 0.0
NOTA_MAX = 10.0
MEDIA_APROVACAO = 7.0
MEDIA_REPROVACAO = 4.0

def _valida(nota):
    """Garante que a nota esteja no intervalo permitido."""
    if not (NOTA_MIN <= nota <= NOTA_MAX):
        raise ValueError(f"Nota fora do intervalo: {nota}")

def calcula_media(n1, n2, n3):
    """Calcula a media ponderada: a terceira nota vale 2x."""
    for n in (n1, n2, n3):
        _valida(n)
    return (n1 + n2 + 2 * n3) / 4