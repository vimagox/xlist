import os
from xlist.app import app


def main():
    app.run(port=8080, debug=os.environ.get('DEBUG', False))

if __name__ == '__main__':
    main()