import requests
import mimetypes

def check_url_details(url):
    try:
        # Verificar si la URL utiliza HTTPS
        if not url.startswith("https://"):
            print(f"❌ La URL no utiliza HTTPS: {url}")
        else:
            print(f"✅ La URL utiliza HTTPS: {url}")

        # Hacer una solicitud HEAD para obtener información sin descargar todo el archivo
        response = requests.head(url, allow_redirects=True)

        # Verificar si la URL es accesible (código de estado 200)
        if response.status_code == 200:
            print(f"✅ La URL es accesible (Código de estado 200): {url}")
        else:
            print(f"❌ La URL no es accesible. Código de estado: {response.status_code}")
            return  # Salir si no es accesible

        # Verificar el tipo de archivo (Debe ser APK)
        content_type = response.headers.get('content-type')
        if content_type == "application/vnd.android.package-archive":
            print(f"✅ El archivo es un APK: {content_type}")
        else:
            mime_type, _ = mimetypes.guess_type(url)
            if mime_type == "application/vnd.android.package-archive":
                print(f"✅ El archivo es un APK basado en la URL: {mime_type}")
            else:
                print(f"❌ El archivo no es un APK. Tipo detectado: {content_type}")

        # Verificar el tamaño del archivo (debería estar entre 5 MB y 50 MB)
        file_size = int(response.headers.get('content-length', 0)) / (1024 * 1024)  # Convertir a MB
        if 5 <= file_size <= 50:
            print(f"✅ El tamaño del archivo es razonable: {file_size:.2f} MB")
        else:
            print(f"❌ El tamaño del archivo no es razonable: {file_size:.2f} MB")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al intentar acceder a la URL: {e}")

# Pedir la URL por consola
url = input("Por favor ingresa la URL del APK: ")
check_url_details(url)
