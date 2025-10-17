import logging
import time

def configurar_logging():
    """Configura el sistema de logging para la aplicación."""
    # Crear logger
    logger = logging.getLogger('procesador_datos')
    logger.setLevel(logging.DEBUG)

    # Evitar duplicación de handlers si la función se llama múltiples veces
    if not logger.handlers:
        # Handler para consola
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console_format = logging.Formatter('%(levelname)s: %(message)s')
        console.setFormatter(console_format)

        # Handler para archivo
        file_handler = logging.FileHandler('procesamiento.log')
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)

        # Añadir handlers al logger
        logger.addHandler(console)
        logger.addHandler(file_handler)

    return logger

def procesar_datos(datos):
    """Procesa una lista de datos y devuelve los resultados."""
    logger = logging.getLogger('procesador_datos')

    logger.info(f"Iniciando procesamiento de {len(datos)} elementos")
    resultados = []

    for i, item in enumerate(datos):
        try:
            logger.debug(f"Procesando item {i}: {item}")

            # Simular procesamiento
            time.sleep(0.1)

            if item < 0:
                logger.warning(f"Valor negativo encontrado: {item}")

            resultado = item * 2
            resultados.append(resultado)

        except Exception as e:
            logger.error(f"Error procesando item {i}: {e}", exc_info=True)

    logger.info("Procesamiento completado")
    return resultados

# Uso de la aplicación
if __name__ == "__main__":
    logger = configurar_logging()
    logger.info("Aplicación iniciada")

    try:
        datos = [1, 2, -3, 4, "5"]
        resultados = procesar_datos(datos)
        logger.info(f"Resultados: {resultados}")
    except Exception as e:
        logger.critical(f"Error fatal en la aplicación: {e}", exc_info=True)

    logger.info("Aplicación finalizada")
