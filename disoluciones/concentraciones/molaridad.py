from concentraciones import calcularPorcentaje, calcularSoluto, calcularSolucion

factores = {
    "ml": 1000,
    "l": 1,
}
listaFactores = factores.keys()


def validarUnidadVolumen(unidad: str):
    if (unidad in listaFactores):
        return
    else:
        raise ValueError("unidad de volumen desconocida")


def calcular(
    molesSoluto: float,
    volumenSolucion: float,
    unidadVolumenSn: str = 'ml'
) -> float:
    """ devuelve la Molaridad

    Parameters
    ----------
    molesSoluto: float
        la cantidad de soluto expresado en moles.

    volumenSolucion: float
        volumen final de la solución.
    """
    validarUnidadVolumen(unidadVolumenSn)
    return calcularPorcentaje(
        molesSoluto,
        volumenSolucion,
        factores[unidadVolumenSn]
    )


def calcularMolesSoluto(
    molaridad: float,
    volumenSolucion: float,
    unidadVolumenSn: str = 'ml'
) -> float:
    validarUnidadVolumen(unidadVolumenSn)
    return calcularSoluto(
        porcentaje=molaridad,
        solucion=volumenSolucion,
        factor=factores[unidadVolumenSn]
    )

def calcularVolumenSolucion(
    molaridad: float,
    molesSoluto: float,
    unidadVolumenSn: str = 'ml'
) -> float:
    validarUnidadVolumen(unidadVolumenSn)
    return calcularSolucion(
        porcentaje=molaridad,
        soluto=molesSoluto,
        factor=factores[unidadVolumenSn]
    )