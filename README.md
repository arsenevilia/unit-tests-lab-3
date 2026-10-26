# unit-tests-lab-3

Практична робота №4 (тема 3, «Автоматизація тестування»).

- Студент: Арсеньєв Ілля, група 3-41
- Номер журналу: 3, **варіант 3**
- Мова: Python 3 + PyTest (+ pytest-cov)
- Функція: `score_to_ects(score)` у `ects.py`

## Що робить функція
Бал 0..100 перетворюється на літеру ECTS: 90–100 A, 82–89 B, 74–81 C, 64–73 D, 60–63 E, 0–59 F. Межа входить у вищий діапазон. Бал поза 0..100 (або не число) — `ValueError`.

## Запуск
```
pip install -r requirements.txt
pytest -v
pytest --cov=ects --cov-report=term-missing
```
Фактичне покриття рядків модуля `ects`: **100 %** (див. `coverage-report.txt`, `screenshots/`).
