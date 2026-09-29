import os
# Словарь с настройками
settings = {
    "project_name": "testing",
    "target_branch": "vm_selOS",
    "web_port": 8080,
    "is_production": False
}

# Список файлов — теперь он может быть любым по длине
files = ["README.md", "NOTES.md", "requirements.txt", "CHANGELOG.md", "Dockerfile","Make_file"]

# --- ЦИКЛ: перебираем каждый файл в списке ---
print("🔁 Обработка файлов (цикл for):")
for file_name in files:
    # Проверка: существует файл или нет в текущей папке
    if os.path.exists(file_name):
        print(f" → ✅ Файл {file_name} найден на диске.")
    # file_name — это переменная, которая на каждой итерации равна одному элементу списка
        print(f"  → Обрабатываю файл: {file_name}")

    # Внутри цикла можно делать проверки для каждого файла отдельно
        if file_name.endswith(".md"):
            print(f"     • Это документ (.md) — можно собрать оглавление.")
        elif file_name == "requirements.txt":
            print(f"     • Это список зависимостей — нужно установить пакеты.")
        else:
            print(f"     • Тип файла не определён — пропускаю автоматическую обработку.")
    else:
        # Если файла нет на диске, но он есть в нашем списке
        print(f"  → ❌ Файл {file_name} НЕ найден на диске (но есть в плане работ).")

# --- Ещё один цикл: перебор ключей и значений словаря ---
print("\n📋 Настройки проекта (перебор словаря):")
for key, value in settings.items():
    # key — имя настройки (например, "web_port")
    # value — её значение (например, 8080)
    print(f"   {key}: {value}")

# Пример: формируем сообщение коммита, перечисляя все файлы
file_list_str = ", ".join(files)
commit_msg = f"deploy: prepare {settings['project_name']} with files: {file_list_str}"
print(f"\n📝 Готовое сообщение коммита: {commit_msg}")

