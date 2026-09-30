import os

def process_files(files_list):
    """
    Проверяет файлы и возвращает список строк для отчёта.
    Ничего не печатает — только готовит данные.
    """
    report_lines = []
    report_lines.append("📁 ОТЧЁТ ПО ФАЙЛАМ")
    report_lines.append("-" * 40)
    
    for file_name in files_list:
        exists = os.path.exists(file_name)
        
        if exists:
            status_icon = "✅"
            status_text = "найден"
        else:
            status_icon = "❌"
            status_text = "НЕ найден (но есть в плане)"
        
        line = f"{status_icon} {file_name} — {status_text}"
        report_lines.append(line)
        
        # Классификация (только если файл есть)
        if exists:
            if file_name.endswith(".md"):
                report_lines.append(f"   📄 Это документ — можно собрать оглавление.")
            elif file_name == "requirements.txt":
                report_lines.append(f"   📦 Это список зависимостей — нужно установить пакеты.")
            else:
                report_lines.append(f"   ℹ️ Тип не определён — пропускаю автоматическую обработку.")
    
    return report_lines

# --- Основная часть ---

settings = {
    "project_name": "testing",
    "target_branch": "vm_selOS"
}

files = ["README.md", "NOTES.md", "requirements.txt", "CHANGELOG.md", "Dockerfile", "Make_file"]

# 1. Готовим отчёт
report = process_files(files)

# 2. ЗАПИСЬ в файл (сохраняем отчёт)
output_filename = "file_report.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    for line in report:
        f.write(line + "\n")
print(f"💾 Отчёт сохранён в файл: {output_filename}")

# 3. ЧТЕНИЕ из файла (проверяем, что сохранили)
print("\n👁 Читаем отчёт обратно из файла:")
with open(output_filename, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Дополнительно: покажем сообщение коммита
file_list_str = ", ".join(files)
commit_msg = f"deploy: prepare {settings['project_name']} with files: {file_list_str}"
print(f"📝 Готовое сообщение коммита: {commit_msg}")

