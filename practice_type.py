# Словарь с настройками (как vars в Ansible)
settings = {
    "project_name": "testing",
    "target_branch": "vm_selOS",
    "web_port": 8080,
    "is_production": False
}

# Список файлов, которые мы планируем обработать
files = ["README.md", "NOTES.md"]

# Добавляем ещё один файл динамически
files.append("requirements.txt")

# Формируем сообщение коммита на основе данных
commit_msg = f"deploy: prepare {settings['project_name']} on branch {settings['target_branch']}"

# Вывод отчёта
print("--- Отчёт по проекту ---")
print(f"Проект: {settings['project_name']}")
print(f"Целевая ветка: {settings['target_branch']}")
print(f"Порт: {settings['web_port']}")
print(f"Production режим: {settings['is_production']}")
print(f"Файлы для обработки: {files}")
print(f"Сообщение коммита: {commit_msg}")
print("-----------------------")

