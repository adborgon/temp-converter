# temp-converter

Pequeña utilidad en Python para convertir temperaturas entre Celsius y Fahrenheit

## Uso

### CLI

```bash
python -m app 100 c      # 100 °C -> 212 °F
python -m app 212 f      # 212 °F -> 100 °C
python -m app 21 f c     # 21 °F -> -6.11 °C
python -m app            # banner + ayuda
```

### API

```python
from app.converter import celsius_to_fahrenheit, fahrenheit_to_celsius

celsius_to_fahrenheit(100)    # 212.0
fahrenheit_to_celsius(32)     # 0.0
```

Las funciones validan la entrada y lanzan `TypeError` (no numérico) o
`ValueError` (NaN/infinito).

### Imagen Docker

La imagen publicada está en GHCR: `ghcr.io/adborgon/temp-converter`. El
`Dockerfile` usa `ENTRYPOINT ["python", "-m", "app"]`, así que los argumentos
de la CLI se pasan directamente a `docker run`.

```bash
# GHCR exige login aunque el paquete sea público:
#   Username: tu usuario GitHub
#   Password: token PAT clásico con scope read:packages
#   (los tokens fine-grained no sirven para pull de paquetes Docker)
docker login ghcr.io

docker pull ghcr.io/adborgon/temp-converter:0.1.0
docker run --rm ghcr.io/adborgon/temp-converter:0.1.0 100 c
#   -> 100 °C = 212 °F
docker run --rm ghcr.io/adborgon/temp-converter:0.1.0 212 f
#   -> 212 °F = 100 °C
```

Con Bionic Core (`C:\Bionic\Core`) no hace falta Docker CLI:

```python
import sys
sys.path.insert(0, r"C:\Bionic")
from Core.tools import ProjectDockerManager

with ProjectDockerManager(r"C:\Bionic\projects\temp-converter") as docker:
    docker.pull_and_run("ghcr.io/adborgon/temp-converter:0.1.0")
```

## Estructura del proyecto

- `src/app/`: Código fuente de la aplicación (`python -m app`).
  - `converter.py`: funciones puras de conversión.
- `tests/`: Suite de pruebas ejecutada en el sandbox de Bionic (`pytest`).
- `.bionic/project.json`: Metadatos generados automáticamente en el bootstrap.

## Tests

La suite se ejecuta en el sandbox Docker aislado de Bionic
(`DockerSandboxManager.run_pytest`), nunca en el shell del host.
