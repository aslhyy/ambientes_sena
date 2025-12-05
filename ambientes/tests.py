import sys

try:
    import pymysql
    print(f"PyMySQL instalado: {pymysql.__version__}")
    print(f"Ubicación: {pymysql.__file__}")
except ImportError:
    print(" PyMySQL NO instalado")

try:
    import MySQLdb
    print(f"MySQLdb encontrado: {MySQLdb.__version__}")
    print(f"Ubicación: {MySQLdb.__file__}")
except ImportError:
    print("MySQLdb NO encontrado (esto es bueno)")

print(f"\nPython ejecutable: {sys.executable}")
print(f"Python path: {sys.path}")