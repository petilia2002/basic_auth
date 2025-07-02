import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone

time_fields = ["iat", "exp"]


def datetime_proprocessing(payload):
    # Преобразование каждого временного поля
    for field in time_fields:
        if field in payload:
            # Преобразуем Unix timestamp в datetime с UTC временной зоной
            payload[field] = datetime.fromtimestamp(payload[field], tz=timezone.utc)
    return payload


SECRET_KEY = "your_very_secret_key_here"

user_id = "1"
username = "John"

# Создаем токен с timezone-aware временем:
payload = {
    "sub": user_id,
    "username": username,
    "iat": datetime.now(timezone.utc),  # Правильный способ в Python 3.12+
    "exp": datetime.now(timezone.utc) + timedelta(hours=1),
}

print(payload)

token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm="HS256")
print(f"Сгенерированный токен: {token}")

try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    payload = datetime_proprocessing(payload)
    print(f"Данные из токена: {payload}")
except ExpiredSignatureError:
    print("Ошибка: Срок действия токена истек")
except InvalidTokenError as e:
    print(f"Ошибка: Невалидный токен - {e}")
except Exception as e:
    print(f"Ошибка при проверке токена - {e}")
