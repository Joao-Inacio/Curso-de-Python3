try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise
from Aula057.pacote1.modulo1 import v1
v2 = 'variavel 2'
print(v1)
