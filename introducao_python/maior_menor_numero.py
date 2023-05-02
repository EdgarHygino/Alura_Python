pri = int(input('Digite o primeiro número: '))
seg = int(input('digite o segundo número: '))
ter = int(input('Digite o terceiro número: '))

def maior (pri, seg, ter):
    upper = [pri, seg, ter]
    upper.sort()
    _maior = upper[2]
    return _maior

def menor (pri, seg, ter):
    lower = [pri, seg, ter]
    lower.sort()
    _menor = lower[0]
    return _menor

_maior = maior(pri, seg, ter)
_menor = menor(pri, seg, ter)

print(f'O maior numero é {_maior}')
print(f'O menor numero é {_menor}')
