import pytest
import allure

@allure.suite("Pruebas de ejemplo")
@allure.title("Test con resultados variados")
def test_1():
    assert True

@allure.suite("Pruebas de ejemplo")
@allure.title("Test con resultados variados")
def test_2():
    assert True
