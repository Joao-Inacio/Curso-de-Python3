"""
    Subprocess - Executando programas e comandos externos
"""
import subprocess

# Windows - ping 127.0.0.1

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

print(proc.stderr)
print(proc.stdout)
print(proc.returncode)
print(proc.args)
