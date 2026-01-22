QA Automation Project - The Internet

Автоматизация тестирования для веб-приложения [The Internet](https://the-internet.herokuapp.com) с использованием Python, Playwright и Pytest.  
Проект построен по паттерну Page Object и поддерживает CI через GitHub Actions.


# Стек технологий

- Python 3.13
- Pytest >= 8.3.0
- Playwright >= 1.48.0
- GitHub Actions CI
- Page Object Model


# Установка и запуск тестов 

1. Клонируем репозиторий:
   
   git clone git@github.com:aut0testing/QA-Automation-Role.git

   cd QA-Automation-Role

3. Создаем виртуальное окружение:
   
   python -m venv venv

   source venv/bin/activate       # Linux / Mac

   venv\Scripts\activate          # Windows

4. Устанавливаем зависимости:
   
   Для Python 3.13 используйте один из способов:
   
   а) Используйте скрипт установки (рекомендуется):
      bash install.sh
   
   б) Или установите вручную с предпочтением wheel файлов:
      pip install --prefer-binary -r requirements.txt
   
   в) Если возникли проблемы с компиляцией, попробуйте:
      pip install --prefer-binary --no-build-isolation -r requirements.txt

5. Устанавливаем браузеры Playwright:
   
   playwright install

6. Запуск тестов:

5.1 Локально:
   
   а) по url по умолчанию: pytest -v

   б) для кастомного - укажите url в параметре(--base-url), например: pytest --base-url=https://google.com -v

5.2 В Github CI - прогон тестов запускается автоматически при каждом push запроса в ветке в main

5.3 Github CI вручную:

  - Зайти в Actions
  - Выбрать Playwright Pytest Manual Run
  - Выбрать Run workflow
  - Нажать на зеленую кнопку Run workflow







