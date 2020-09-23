# files and directories
from pathlib import Path

# Relative path
# path = Path("ecommerce")
# print(path.exists())

# path = Path("emails")
# print(path.mkdir())

# path = Path("emails")
# print(path.rmdir())

path = Path()
for file in path.glob('*'):
    print(file)

path = Path()
for file in path.glob('*.py'):
    print(file)