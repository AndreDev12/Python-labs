def calcular_tiempo_maximo(calificacion, hora_generacion):
    # Definir los tiempos de respuesta, atención y penalidades según la calificación
    tiempos = {
        'Leve': {
            'TiempoRespuesta': 45,
            'TiempoAtencion': 4,
            'Penalidad': 50
        },
        'Urgente': {
            'TiempoRespuesta': 30,
            'TiempoAtencion': 2,
            'Penalidad': 80
        },
        'Muy urgente': {
            'TiempoRespuesta': 15,
            'TiempoAtencion': 1,
            'Penalidad': 140
        }
    }

    # Obtener los tiempos y penalidad correspondientes a la calificación
    tiempo_respuesta = tiempos[calificacion]['TiempoRespuesta']
    tiempo_atencion = tiempos[calificacion]['TiempoAtencion']
    penalidad = tiempos[calificacion]['Penalidad']

    # Calcular el tiempo máximo de atención sumando el tiempo de respuesta y atención
    tiempo_maximo = tiempo_respuesta + tiempo_atencion * 60  # Convertir tiempo de atención a minutos

    # Calcular el tiempo máximo de atención considerando la hora de generación del ticket
    hora_generacion = int(hora_generacion.replace(':', ''))  # Convertir la hora generación a un entero sin ":" (por ejemplo, de "10:48" a 1048)
    hora_atencion = hora_generacion + tiempo_maximo  # Calcular la hora de atención sumando el tiempo máximo al momento de generación del ticket

    # Obtener los minutos de retraso
    minutos_retraso = max(0, hora_atencion % 100 - 30)  # Calcular los minutos de retraso a partir de los minutos de la hora de atención (se considera retraso si supera los 30 minutos)

    # Calcular la penalidad total por retraso
    penalidad_total = minutos_retraso // 5 * penalidad  # Calcular la penalidad por cada 5 minutos de retraso o fracción

    # Mostrar el resultado
    print("El tiempo máximo de atención para una incidencia", calificacion, "es de", tiempo_maximo, "minutos.")
    print("La hora máxima de atención sería", str(hora_atencion // 100).zfill(2) + ":" + str(hora_atencion % 100).zfill(2), "horas.")
    print("Se aplicaría una penalidad de S/.", penalidad_total, "por retraso.")

# Ejemplo de uso
calificacion = 'Urgente'
hora_generacion = '10:48'
calcular_tiempo_maximo(calificacion, hora_generacion)

# Summary
# En este algoritmo, se define un diccionario tiempos que contiene los tiempos de respuesta, atención y penalidades para cada calificación. Luego, se obtienen los tiempos y penalidad correspondientes según la calificación proporcionada. El tiempo máximo de atención se calcula sumando el tiempo de respuesta y el tiempo de atención convertido a minutos. La hora de atención se calcula sumando el tiempo máximo al momento de generación del ticket. A partir de la hora de atención, se determina si hay retraso y se calcula la penalidad correspondiente. Finalmente, se muestra el resultado con el tiempo máximo de atención, la hora máxima de atención y la penalidad por retraso.

# Recuerda que puedes ajustar los valores de los tiempos, las penalidades y otros detalles según tus necesidades específicas.