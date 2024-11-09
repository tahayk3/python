import jwt
from datetime import datetime, timedelta

# Token JWT proporcionado
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMDQ1Mzg4LCJqdGkiOiIwOGYyNTQ1YTIzOTY0YTExYmM4ZDEzMjExOTMzYmUyZCIsInVzZXJfaWQiOjF9.Rf9n97EYaJg10hBngQrdiT4CxN4LdIZc-1lCgTF0CdQ"

# Decodificación del token sin verificar la firma
payload = jwt.decode(token, options={"verify_signature": False})

# Extraer expiracion del token del payload
tiempoExpiracion = payload.get('exp')

# Vida útil del token en segundos (24 horas)
lifetime_in_seconds = 6 * 60 * 60

# Calcular iat_timestamp (fecha de creación)
iat_timestamp = tiempoExpiracion - lifetime_in_seconds

# Convertir iat_timestamp a una fecha legible
iat_datetime = datetime.utcfromtimestamp(iat_timestamp)

print("Fecha de creación (iat):", iat_datetime)























class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Obtener el token de las cookies
        token = request.COOKIES.get('access_token')
        print(f"Token recibido: {token}")

        payload = jwt.decode(token, options={"verify_signature": False})

        # Extraer expiracion del token del payload
        tiempoExpiracion = payload.get('exp')

        # Vida útil del token en segundos (6 horas)
        lifetime_in_seconds = 6 * 60 * 60

        # Calcular iat_timestamp (fecha de creación)
        iat_timestamp = tiempoExpiracion - lifetime_in_seconds

        # Convertir iat_timestamp a una fecha legible
        iat_datetime = datetime.utcfromtimestamp(iat_timestamp)


        print("Fecha de expiracion:", tiempoExpiracion)
        print("Fecha de creación (iat):", iat_datetime)