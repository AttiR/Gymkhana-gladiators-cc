from app import create_app
import os

app = create_app('production' if os.environ.get('DYNO') else 'development')

if __name__ == '__main__':
    app.run(debug=True)