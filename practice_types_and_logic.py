# Словарь с настройками (как vars в Ansible)
settings = {
    "project_name": "testing",
    "target_branch": "vm_selOS",
    "web_port": 8080,
    "is_production": False   # <-- Меняй это значение на True/False и смотри, как меняется вывод
}

# Список файлов
files = ["README.md", "NOTES.md"]
files.append("requirements.txt")

# Формируем базовое сообщение коммита
commit_msg = f"deploy: prepare {settings['project_name']} on branch {settings['target_branch']}"

# --- УСЛОВНАЯ ЛОГИКА: проверка флага is_production ---
if settings["is_production"]:
    # Если production == True: добавляем предупреждение и меняем стиль сообщения
    print("⚠️ ВНИМАНИЕ: РЕЖИМ PRODUCTION! Все действия требуют подтверждения.")
    commit_msg = f"[PROD] {commit_msg} — ручная проверка обязательна"
else:
    # Если НЕ production: обычный режим
    print("✅ Режим: не production. Автоматизация разрешена.")

# Проверка: есть ли в списке нужный файл
if "requirements.txt" in files:
    print("📦 Файл requirements.txt найден — можно устанавливать зависимости.")
else:
    print("❌ Файл requirements.txt не найден — зависимости установить нельзя.")

# Вывод итогового отчёта
print("\n--- Итоговый отчёт ---")
print(f"Проект: {settings['project_name']}")
print(f"Целевая ветка: {settings['target_branch']}")
print(f"Порт: {settings['web_port']}")
print(f"Production режим: {settings['is_production']}")
print(f"Файлы для обработки: {files}")
print(f"Сообщение коммита: {commit_msg}")
print("-----------------------")

