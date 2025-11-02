from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.translation import get_language

def seleccionar_storage():
    if settings.DEBUG:
        return FileSystemStorage()
    else:
        # Solo importar Cloudinary en producción
        from cloudinary_storage.storage import MediaCloudinaryStorage
        return MediaCloudinaryStorage()

def get_translated_field(obj, field_name):
    """
    Obtiene el valor de un campo traducido según el idioma activo.
    Si no existe traducción, devuelve el valor en español (fallback).
    
    Args:
        obj: Objeto del modelo
        field_name: Nombre del campo base (ej: 'titulo', 'descripcion')
    
    Returns:
        Valor del campo en el idioma activo o español como fallback
    """
    current_language = get_language()
    
    # Si el idioma es inglés, intentar obtener el campo traducido
    if current_language == 'en':
        translated_field = f"{field_name}_en"
        translated_value = getattr(obj, translated_field, None)
        
        # Si existe traducción y no está vacía, devolverla
        if translated_value:
            return translated_value
    
    # Fallback: devolver el campo en español
    return getattr(obj, field_name, '')
