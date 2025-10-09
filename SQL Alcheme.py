from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Создаём базовый класс для моделей
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # Имя таблицы

    id = Column(Integer, primary_key=True)  # Первичный ключ
    name = Column(String)                   # Имя пользователя
    age = Column(Integer)                   # Возраст
    gender = Column(String)                 # Пол пользователя

# Подключение к базе данных SQLite в памяти
engine = create_engine('sqlite:///:memory:', echo=True)

# Создание таблицы
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создаём объект пользователя
new_user = User(name="Alice", age=30, gender="women")

# Добавляем объект в сессию
session.add(new_user)

# Фиксируем транзакцию в базе данных
session.commit()

# Запрашиваем всех пользователей
# Находим пользователя с именем Alice
user = session.query(User).filter_by(name="Alice").first()

# Обновляем возраст пользователя
if user:
    user.age = 31
    session.commit()  # Фиксируем измененияame: {user.name}, Age: {user.age}")

# Закрытие сессии
# session.close()
