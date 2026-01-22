# QA Automation Project - The Internet

Автоматизация тестирования для веб-приложения [The Internet](https://the-internet.herokuapp.com) с использованием Python, Playwright и Pytest.  
Проект построен по паттерну Page Object и поддерживает CI через GitHub Actions.

## Стек технологий

- Python 3.13
- Pytest
- Playwright
- GitHub Actions CI
- Page Object Model

## Структура проекта

```
QA-Automation-Role/
├── pages/              # Page Object классы
│   ├── login_page.py
│   ├── main_page.py
│   └── secure_page.py
├── tests/              # Тестовые файлы
│   ├── conftest.py     # Pytest конфигурация и фикстуры
│   ├── test_login_page.py
│   ├── test_login_positive.py
│   └── test_main_page.py
├── requirements.txt    # Зависимости проекта
└── README.md
```

## Установка и запуск тестов

### 1. Клонируем репозиторий

```bash
git clone git@github.com:aut0testing/QA-Automation-Role.git
cd QA-Automation-Role
```

### 2. Создаем виртуальное окружение

```bash
python3.13 -m venv venv
```

Активируем виртуальное окружение:

- **Linux / Mac:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

### 4. Устанавливаем браузеры Playwright

```bash
playwright install
```

### 5. Запуск тестов

#### 5.1 Локально

**С URL по умолчанию:**
```bash
pytest -v
```

**С кастомным URL:**
```bash
pytest --base-url=https://google.com -v
```

#### 5.2 GitHub CI (автоматический)

Прогон тестов запускается автоматически при каждом push в ветку `main`.

#### 5.3 GitHub CI (ручной запуск)

1. Залогиниться в GitHub (логин и пароль отправены на почту)  
2. Зайти в **Actions**
3. Выбрать **Playwright Pytest Manual Run**
4. Выбрать **Run workflow**
5. Нажать на зеленую кнопку **Run workflow**







