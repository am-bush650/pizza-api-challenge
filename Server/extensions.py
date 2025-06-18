from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#initialize sqlalchemy and flask migrate
db = SQLAlchemy()
migrate = Migrate()
