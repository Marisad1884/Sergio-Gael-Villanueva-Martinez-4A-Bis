import pytest
from app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError,
)


# 1. Aislamiento de estado: fixtures
@pytest.fixture
def perfil():
    return PerfilMovil("sergio", 100)


@pytest.fixture
def perfil_pro():
    return PerfilPro("gael", 100, 3)


# 2. Integridad estructural y aserciones
def test_atributos_iniciales(perfil):
    assert perfil.username == "sergio"
    assert perfil.gemas == 100
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_gemas_por_defecto():
    assert PerfilMovil("nuevo").gemas == 50


def test_ganar_gemas_suma_correctamente(perfil):
    assert perfil.ganar_gemas(30) == 130
    assert perfil.gemas == 130


def test_gastar_gemas_resta_correctamente(perfil):
    assert perfil.gastar_gemas(40) == 60
    assert perfil.gemas == 60


def test_gastar_todo_el_saldo(perfil):
    assert perfil.gastar_gemas(100) == 0


def test_transacciones_consistentes(perfil):
    perfil.ganar_gemas(50)
    perfil.gastar_gemas(20)
    assert perfil.gemas == 130


# 3. Validación de excepciones
def test_gemas_iniciales_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("x", -1)


def test_gastar_mas_de_lo_disponible(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(101)


def test_gastar_cantidad_invalida(perfil):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(0)


def test_saldo_no_cambia_tras_error(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(500)
    assert perfil.gemas == 100


def test_meses_suscripcion_invalidos():
    with pytest.raises(ValueError):
        PerfilPro("x", 10, 0)


def test_descarga_con_suscripcion_expirada(perfil_pro):
    perfil_pro.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False


# 4. Pruebas parametrizadas
@pytest.mark.parametrize("cantidad, esperado", [
    (1, 101),
    (10, 110),
    (50, 150),
    (999, 1099),
])
def test_ganar_gemas_validas(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -50, -1000])
def test_ganar_gemas_invalidas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


# 5. Tipo y jerarquía (isinstance)
def test_perfil_pro_es_perfil_movil(perfil_pro):
    assert isinstance(perfil_pro, PerfilPro)
    assert isinstance(perfil_pro, PerfilMovil)
    assert issubclass(PerfilPro, PerfilMovil)


def test_perfil_base_no_es_pro(perfil):
    assert not isinstance(perfil, PerfilPro)


def test_ciclo_de_vida_perfil_pro(perfil_pro):
    assert perfil_pro.es_pro is True
    assert perfil_pro.meses_suscripcion == 3
    assert perfil_pro.descargar_contenido_offline() == "Descarga offline completada con éxito."
    perfil_pro.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False


def test_perfil_pro_hereda_metodos(perfil_pro):
    assert perfil_pro.ganar_gemas(10) == 110


def test_excepciones_heredan_de_exception():
    assert issubclass(SuscripcionExpiradaError, Exception)
    assert issubclass(PuntosInsuficientesError, Exception)
