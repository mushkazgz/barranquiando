# web/scripts/populate_db.py

import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mongoengine import connect
from models.barranco import Barranco

# Conéctate a la base de datos MongoDB
connect(db='barranquiando_db', host='localhost', port=27017)

# Crear instancias de Barranco
barranco1 = Barranco(
    nombre="Gorgas de Fuentes Callejas",
    descripcion="Barranco Gorgas de Fuentes Callejas, ubicado en los Pirineos.",
    periodo_descenso="Todo el año",
    dificultad="Moderado",
    poblacion="Pirineos",
    wikiloc="https://www.wikiloc.com",
    longitud=1500.0,
    altitud_max=1200.0,
    altitud_min=800.0,
    diferencia=400.0,
    rapeles="2 rápeles de 20m",
    equipamiento="Anclajes modernos",
    longitud_max=20.0,
    cartografia="Mapa XYZ",
    tiempo_recorrido="2 horas con un coche",
    aproximacion="Aproximación sencilla",
    recorrido="Recorrido interesante con saltos y toboganes",
    retorno="Retorno rápido",
    topografia_imagen="http://example.com/topografia.jpg",
    descenso_info="Rápeles con agua, algunos toboganes.",
    meteorologia="Zona con lluvias frecuentes",
    caudal="Moderado",
    rio="Rio XYZ",
    hilo_foro="https://foro.example.com",
    punto_control_caudal="Punto X en el río",
    informacion_adicional="Se recomienda llevar traje de neopreno.",
    video_youtube="http://youtube.com/video",
    acceso_mapa_real="http://maps.google.com",
    informacion_acceso="Acceso fácil desde el pueblo",
    imagen_mapa_acceso="http://example.com/mapa_acceso.jpg",
    aproximacion_imagen_mapa="http://example.com/aproximacion_mapa.jpg",
    descenso_imagen_mapa="http://example.com/descenso_mapa.jpg",
    retorno_imagen_mapa="http://example.com/retorno_mapa.jpg",
    escapes="Escapes fáciles a mitad del recorrido",
    combinacion_barrancos="Puede combinarse con Barranco X",
    geomorfologia_hidrologia="Roca calcárea, caudal constante",
    observaciones="Llevar casco y cuerda de 60m.",
    historia="Descubierto en 1980 por el grupo XYZ."
)

# Guarda el barranco en la base de datos
barranco1.save()

print("Barranco guardado exitosamente en la base de datos.")
