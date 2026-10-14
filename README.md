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

## Estructura del proyecto

- `src/app/`: Código fuente de la aplicación (`python -m app`).
  - `converter.py`: funciones puras de conversión.
- `tests/`: Suite de pruebas ejecutada en el sandbox de Bionic (`pytest`).
- `.bionic/project.json`: Metadatos generados automáticamente en el bootstrap.

## Tests

La suite se ejecuta en el sandbox Docker aislado de Bionic
(`DockerSandboxManager.run_pytest`), nunca en el shell del host.
