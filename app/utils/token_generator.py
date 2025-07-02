import jwt
from datetime import datetime, timedelta, timezone
from app.config import Config


def generate_access_token(id, name, roles):
    payload = {
        "id": id,
        "name": name,
        "roles": roles,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
    }
    return jwt.encode(payload=payload, key=Config.SECRET_KEY, algorithm="HS256")


def payload_proprocessing(payload, time_fields):
    # Преобразование каждого временного поля
    for field in time_fields:
        if field in payload:
            # Преобразуем Unix timestamp в datetime с UTC временной зоной
            payload[field] = datetime.fromtimestamp(payload[field], tz=timezone.utc)
    return payload
