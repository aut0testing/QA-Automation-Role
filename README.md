QA Automation Project - The Internet

Автоматизация тестирования для веб-приложения [The Internet](https://the-internet.herokuapp.com) с использованием Python, Playwright и Pytest.  
Проект построен по паттерну Page Object и поддерживает CI через GitHub Actions.


# Стек технологий

- Python 3.11
- Pytest
- Playwright
- GitHub Actions CI
- Page Object Model


# Установка и запуск тестов 

1. Клонируем репозиторий:
   
   git clone git@github.com:aut0testing/QA-Automation-Role.git

2. Создаем виртуальное окружение:
   
   python -m venv venv

   source venv/bin/activate       # Linux / Mac

   venv\Scripts\activate          # Windows

3. Устанавливаем зависимости:
   pip install -r requirements.txt

4. Устанавливаем браузеры Playwright:
   playwright install

5. Запуск тестов:

6.1 Локально:
   
а) по url по умолчанию: pytest -v

б) для кастомного url: pytest --base-url=https://google.com -v

6.2 В Github CI - прогон тестов запускается автоматически при каждом push запроса в ветке в main

6.3 Github CI вручную:

  - Зайти в Actions
  - Выбрать Playwright Pytest Manual Run
  - Выбрать Run workflow
  - Нажать на зеленую кнопку Run workflow







