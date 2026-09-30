import os

def process_files(files_list):
    """
    Принимает список имён файлов и выводит структурированный отчёт.
    Ничего не делает с файлами — только проверяет наличие и классифицирует.
    """
    print("🔁 Обработка файлов:")
    
    for file_name in files_list:
        exists = os.path.exists(file_name)
        
        if exists:
            status_icon = "✅"
            status_text = "найден"
        else:
            status_icon = "❌"
            status_text = "НЕ найден (но есть в плане)"
        
        # Формируем строку отчёта — теперь она одна на файл, без дублей
        print(f"  {status_icon} {file_name} — {status_text}")
        
        # Классификация (только если файл реально есть)
        if exists:
            if file_name.endswith(".md"):
                print(f"     📄 Это документ — можно собрать оглавление.")
            elif file_name == "requirements.txt":
                print(f"     📦 Это список зависимостей — нужно установить пакеты.")
            else:
                print(f"     ℹ️ Тип не определён — пропускаю автоматическую обработку.")
    
    return exists  # Возвращаем статус последнего файла (для примера)

# --- Основная часть скрипта ---

settings = {
    "project_name": "testing",
    "target_branch": "vm_selOS",
    "web_port": 8080,
    "is_production": False
}

files = ["README.md", "NOTES.md", "requirements.txt", "CHANGELOG.md", "Dockerfile", "Make_file"]

# Вызываем функцию одной строкой — вся логика внутри
process_files(files)

print("\n📋 Настройки проекта:")
for key, value in settings.items():
    print(f"   {key}: {value}")

file_list_str = ", ".join(files)
commit_msg = f"deploy: prepare {settings['project_name']} with files: {file_list_str}"
print(f"\n📝 Готовое сообщение коммита: {commit_msg}")

