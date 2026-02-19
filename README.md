# Actividad A6.2 – Reservation System con Unit Tests

## Descripción

Este repositorio contiene la solución de la Actividad A6.2 de la materia Pruebas y Calidad de Software.  
Se desarrolló un sistema de reservaciones en Python con arquitectura modular (models y services), persistencia en archivos JSON y pruebas unitarias automatizadas.

El proyecto cumple con el estándar PEP-8 y fue validado con flake8 y pylint (10/10).

Fue realizado en tres PRs, favor de revisar la trazabilidad en: https://github.com/a01796900-arturoglezc/A01796900_A6.2/pulls?q=is%3Apr+is%3Aclosed

---

## Requisitos

- Python 3.10 o superior
- Terminal o consola (PowerShell, CMD o Terminal)
- Instalar herramientas de análisis estático descritas en el archivo requirements.txt (pytest, pytest-cov, pylint, flake8)

---

## Estructura

El proyecto está organizado en:

- `src/` → Código fuente (models, services y main)
- `tests/` → Pruebas unitarias
- `README.md` → Documentación

Se incluyen archivos `__init__.py` para el correcto reconocimiento de paquetes.

---

## Ejecutar el sistema con main.py manual

Desde la raíz del proyecto:

python -m src.main


---

## Ejecutar pruebas unitarias con Coverage (91%)

Desde la raíz del proyecto:

pytest --cov=src --cov-report=term-missing


---

## Análisis estático

Validación realizada con los comandos:

flake8 src
pylint src


---

## Autor

Arturo González Corona  
Matrícula: A01796900  
Actividad: A6.2 – Pruebas y Calidad de Software

