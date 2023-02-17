from funcion import sumar, primo

def test_sumar():
    assert sumar(2,4) == 6
    assert sumar(-2,2) == 0
    assert sumar(2,2) == 4
    
def test_primo():
    assert primo(5) == True
    assert primo(1) == True
    assert primo(10) == False
    
    