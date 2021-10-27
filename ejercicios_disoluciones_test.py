import unittest
from disoluciones import calculadoraMasa, calculadoraMoles, calculadoraVolumen
import concentraciones


"""
Esta clase de unitesting tendrá los ejercicios de la guía
de actividades que han preparado los profesores de química
de sexto año del nacional de san isidro.
"""


class DisolucionesEjerciciosIntroductorios(unittest.TestCase):
    # 1.a
    def test_1_a(self):
        masa = 120  # g
        densidad = 0.4  # g/ml
        volumenEsperado = 300  # ml
        res = calculadoraVolumen.masa_densidad(masa, densidad)
        self.assertEqual(res, volumenEsperado,
                         f'debería ser {volumenEsperado}')

    # 1.b
    def test_1_b(self):
        volumen = 800  # ml
        densidad = 0.75  # g/ml
        masaEsperada = 600  # g
        res = calculadoraMasa.volumen_densindad(volumen, densidad)
        self.assertEqual(res, masaEsperada,
                         f'la respuesta debería ser {masaEsperada}')

    # 1.c
    def test_1_c(self):
        masa = 600  # g
        # trioxido de azufre
        masaMolar = 32 + 16*3  # g/mol
        molesEsperados = 7.5
        res = calculadoraMoles.masa_masaMolar(masa, masaMolar)
        self.assertEqual(res, molesEsperados,
                         f'la respuesta debería ser {molesEsperados}')

    # 1.d
    def test_1_d(self):
        # kg -> g
        masa = 2.835 * 1000
        masaMolar = 1+14+16*3  # g/mol
        molesEsperados = 45
        res = calculadoraMoles.masa_masaMolar(masa, masaMolar)
        self.assertEqual(res, molesEsperados,
                         f'la respuesta debería ser {molesEsperados}')

    # 1.e
    def test_1_e(self):
        volumen = 2875  # ml
        masaMolar = 2*12+5+16+1  # g/mol
        densidad = 0.8  # g/ml

        masaEsperada = 2300  # g
        masa = calculadoraMasa.volumen_densindad(volumen, densidad)
        self.assertEqual(masa, masaEsperada, f'se esperaban {masaEsperada}g')

        molesEsperados = 50  # mol
        moles = calculadoraMoles.masa_masaMolar(masa, masaMolar)
        self.assertEqual(moles, molesEsperados,
                         f'se esperaban {molesEsperados}mol')

    # 1.f
    def test_1_f(self):
        moles = 12  # mol
        masaMolar = 12*3+16+6  # g/mol
        densidad = 0.8  # g/ml

        masaEsperada = 696  # g
        masa = calculadoraMasa.masaMolar_moles(masaMolar, moles)
        self.assertEqual(masa, masaEsperada,
                         f'la masa debe ser {masaEsperada}')

        volumenEsperado = 870  # ml
        volumen = calculadoraVolumen.masa_densidad(masa, densidad)
        self.assertEqual(volumen, volumenEsperado,
                         f'el volumen debe ser {volumenEsperado}')

    # 2.a
    def test_2_a(self):
        masaSol = 30  # g azúcar
        masaDis = 400  # g H20
        masaSn = masaDis + masaSol  # g

        porcentajeEsperad = (30/(400+30))*100
        porcentaje = concentraciones.calcularPorcentaje(masaSol, masaSn)
        self.assertEqual(porcentaje, porcentajeEsperad,
                         f'se esperaba {porcentajeEsperad}')

    # 2.b
    def test_2_b(self):
        masaSol = 30  # g nitrato de plata
        volumenSn = 60  # ml solucion

        porcentajeEsperado = (30/60)*100
        porcentaje = concentraciones.calcularPorcentaje(masaSol, volumenSn)
        self.assertEqual(porcentaje, porcentajeEsperado,
                         f'se esperaba {porcentajeEsperado}')

    # 2.c
    def test_2_c(self):
        masaSol = 26  # g sacarosa
        masaSn = 70  # g solucion (almíbar)

        porcentajeEsperado = (26/70)*100
        porcentaje = concentraciones.calcularPorcentaje(masaSol, masaSn)
        self.assertEqual(porcentaje, porcentajeEsperado,
                         f'se esperaba {porcentajeEsperado}')

    # 2.f / 2.g
    def test_2_f(self):
        # * alcohol absoluto
        volumenDis = 200  # ml
        densidadDis = 0.8  # g/ml
        masaDisEsperada = 200 * 0.8  # g
        masaDis = calculadoraMasa.volumen_densindad(volumenDis, densidadDis)
        self.assertEqual(masaDis, masaDisEsperada,
                         f'masa del disolvente esperada {masaDisEsperada}')

        # * H2O
        volumenSol = 100  # ml
        densidadSol = 1  # g/ml
        masaSolEsperada = 100  # g
        masaSol = calculadoraMasa.volumen_densindad(volumenSol, densidadSol)
        self.assertEqual(masaSol, masaSolEsperada,
                         f'masa del soluto esperada {masaSolEsperada}')

        # * masa final de la solución (2.g).
        resultadoEsperado = masaSolEsperada + masaDisEsperada
        resultado = masaSol + masaDis
        self.assertEqual(resultado, resultadoEsperado,
                         f'se esparaba cómo resultado {resultadoEsperado}')

        # * volumen final de la solución (2.f).
        # no sé cómo obtener la densidad final de la solución.
        # Sé cómo sumar las masas, pero en este caso los volúmenes
        # no son aditivos. Entonces, sin la densidad de la
        # solución, no puedo obtener ningún resultado :/

    # 2.h
    def test_2_g(self):
        concentracion = 3  # %m/m
        solucion = 200  # g

        solutoEsperado = (3/100)*solucion
        soluto = concentraciones.calcularSoluto(concentracion, solucion)

        self.assertEqual(soluto, solutoEsperado,
                         f'se esperaba como resultado {solutoEsperado}')

    def test_3(self):
        # * datos soluto
        masaSt = 88.3  # g de HNO3
        densidadSt = 1.513  # g/ml
        volumenSt = calculadoraVolumen.masa_densidad(masaSt, densidadSt)  # ml
        volumenStEsperado = 88.3/1.513  # ml
        self.assertEqual(volumenSt, volumenStEsperado,
                         f'se esperaba {volumenStEsperado} cómo volumen del soluto')

        # * datos solvente
        masaSv = 206.22  # g de H2O
        volumenSv = masaSv  # el volumen del agua es igual a su peso

        # * datos solucion
        masaSn = masaSt + masaSv
        densidadSn = 1.178
        volumenSn = calculadoraVolumen.masa_densidad(masaSn, densidadSn)
        volumenSnEsperado = masaSn / densidadSn
        self.assertEqual(volumenSn, volumenSnEsperado,
                         f'se esperaba {volumenSnEsperado} cómo volumen de la solucion')

    def test_4(self):
        # solvente H2O densidad = 1
        volumenSv = 132.16  # ml
        masaSv = volumenSv  # g

        # solucion
        volumenSn = 200  # ml
        densidadSn = 0.947  # g/ml
        masaEsperadaSn = volumenSn * densidadSn
        masaSn = calculadoraMasa.volumen_densindad(volumenSn, densidadSn)
        self.assertEqual(masaSn, masaEsperadaSn,
                         f'se esperaba una masa de {masaEsperadaSn} para la solución')

        # soluto
        masaSt = masaSn - masaSv
        denisdadSt = 0.789
        volumenEsperadoSt = masaSt / denisdadSt
        volumenSt = calculadoraVolumen.masa_densidad(masaSt, denisdadSt)
        self.assertEqual(volumenSt, volumenEsperadoSt,
                         f'se esperaba un volumen de {volumenEsperadoSt} para el soluto')

    def test_5(self):
        # ! falta terminar
        # solvente H2O
        masaSv = 1.2 * 1000  # g
        volumenSv = masaSv

        # soluto sal
        masaSt = 250  # g
        densidadSt = 1.5
        volumenSt = calculadoraVolumen.masa_densidad(masaSt, densidadSt)

        # solución
        masaSn = masaSt + masaSv  # g
        densidadSn = 1.2  # g/ml
        volumenEsperadoSn = masaSn / densidadSn  # ml
        volumenSn = calculadoraVolumen.masa_densidad(masaSn, densidadSn)
        self.assertEqual(volumenSn, volumenEsperadoSn,
                         f'el volumen esperado es {volumenEsperadoSn} de solucion')

        # concentraciones
        porcentajeMM = concentraciones.calcularPorcentaje(masaSt, masaSn)
        porcentajeMMEsperado = (masaSt/masaSn)*100
        self.assertEqual(porcentajeMM, porcentajeMMEsperado,
                         f'se esperaba una concentración de {porcentajeMMEsperado} %m/m')

        porcentajeMV = concentraciones.calcularPorcentaje(masaSt, volumenSn)
        porcentajeMVEsperado = (masaSt/volumenSn)*100
        self.assertEqual(porcentajeMV, porcentajeMVEsperado,
                         f'se esperaba {porcentajeMVEsperado} %m/v')

        porcentajeVV = concentraciones.calcularPorcentaje(volumenSt, volumenSn)
        porcentajeVVEsperado = (volumenSt/volumenSn)*100

        # gramos de soluto en 5kg de solucion
        respuesta = concentraciones.calcularSoluto(porcentajeMM, 5000)
        respuestaEsperada = (porcentajeMMEsperado/5000)*100
        self.assertEqual(respuesta, respuestaEsperada,
                         f'se esperaba cómo respuesta {respuestaEsperada} gramos')


if __name__ == '__main__':
    unittest.main()
