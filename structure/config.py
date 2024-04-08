class Config:
    SECRET_KEY = '479cdcf08d2b4a16b9c3ea2eba2853a7'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:1234@localhost:3306/todo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MESSAGE_FLASHING_OPTIONS = { 'duration': 3000 }
