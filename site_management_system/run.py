from app import create_app, db
from app.models import User, Employee, Material

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)