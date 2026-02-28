import calculadora
def test_add():
    calc = calculadora.Calculadora()
    assert calc.add(2, 3) == 5
