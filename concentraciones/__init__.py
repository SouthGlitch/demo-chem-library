def calcularPorcentaje(soluto: float, solucion: float, factor = 100)-> float:
    """ devuelve el porcentaje de concentración entre soluto y solución

    Para utilizar estas PRIMERO deben lograr que las unidades tengan sentido.
    Por ejemplo, para obtener porcentaje masa en masa, el soluto y la solucion
    deben estar expresados en gramos; para obtener masa en volumen el soluto
    debe estar expresado en gramos y la solución en mililitros; así con cualquier
    unidad de medida.

    Parameters
    ----------
    soluto: float
        cantidad de soluto en la solución
    solucion: float
        cantidad de solucion

    Returns
    -------
    float
    """
    return (soluto/solucion)*factor

def calcularSoluto(porcentaje: float, solucion: float, factor = 100)-> float:
    """ devuelve el soluto de una concentración.

    Dependiendo de las unidadeds de concentración, se obtendrá una
    determinada respuesta. Por ejemplo en el caso de %m/m la solución
    se expresa en gramos y el resultado será en gramos; en el caso %m/v
    la solución será en mililitros y el resultado será en gramos; en 
    el caso %v/v la solución será en mililitros y el resultado de la función
    también en mililitros; etc

    Parameters
    ----------
    porcentaje: float
        porcentaje de concentración
    solucion: float
        cantidad de solucion

    Returns
    -------
    float
    """
    return (porcentaje/factor)*solucion

def calcularSolucion(porcentaje: float, soluto: float, factor = 100) -> float:
    """ devuelve el soluto de una concentración.

    Dependiendo de las unidadeds de concentración, se obtendrá una
    determinada respuesta. Por ejemplo en el caso de %m/m el soluto 
    se expresa en gramos y el resultado será en gramos; en el caso 
    %m/v el soluto será en gramos y el resultado en mililitros; en 
    el caso %v/v la solución será en mililitros y el resultado de 
    la función también en mililitros; etc

    Parameters
    ----------
    porcentaje: float
        porcentaje de concentración
    soluto: float
        cantidad de soluto

    Returns
    -------
    float
    """
    return (soluto/porcentaje)*factor
