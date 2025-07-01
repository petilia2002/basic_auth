# Flask User-Roles API

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-brightgreen.svg)

API для управления пользователями и ролями с отношениями многие-ко-многим

## 📌 Особенности

- Каскадное удаление связей при удалении ролей/пользователей
- Автоматическая обработка ассоциативной таблицы `user_roles`
- Защита от массового присвоения (mass assignment)
- Гибкая система ролей с возможностью расширения

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.8+
- PostgreSQL 13+
- Flask 2.0+

### Установка
```bash
git clone https://github.com/yourusername/flask-user-roles-api.git
cd flask-user-roles-api
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt