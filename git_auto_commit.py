import subprocess  # Модуль для запуска системных команд (git, ls, etc.)
import sys         # Модуль для работы с аргументами командной строки


def run_git_command(command):
    """Выполняет git-команду и возвращает результат."""
    result = subprocess.run(
        command,
        capture_output=True,   # Захватываем вывод команды
        text=True,              # Возвращаем строку, а не байты
        shell=True              # Выполняем через shell (для простоты)
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def main():
    # 1. Проверяем статус репозитория
    status_out, status_err, status_code = run_git_command("git status --porcelain")

    # Если вывод пустой — изменений нет
    if not status_out:
        print("✅ Репозиторий чист. Нет изменений для коммита.")
        sys.exit(0)

    # 2. Показываем, какие файлы изменены
    print("📝 Обнаружены изменения:")
    print(status_out)

    # 3. Спрашиваем сообщение для коммита
    commit_message = input("\nВведите сообщение для коммита (или 'q' для отмены): ")

    if commit_message.lower() == 'q':
        print("❌ Отмена. Коммит не создан.")
        sys.exit(0)

    if not commit_message:
        print("❌ Сообщение не может быть пустым.")
        sys.exit(1)

    # 4. Добавляем все изменения
    print("\n⏳ Добавляю файлы...")
    add_out, add_err, add_code = run_git_command("git add -A")
    if add_code != 0:
        print(f"❌ Ошибка при git add: {add_err}")
        sys.exit(1)

    # 5. Делаем коммит
    print("⏳ Создаю коммит...")
    commit_out, commit_err, commit_code = run_git_command(
        f'git commit -m "{commit_message}"'
    )
    if commit_code != 0:
        print(f"❌ Ошибка при коммите: {commit_err}")
        sys.exit(1)

    # 6. Пушим на сервер
    print("⏳ Отправляю на сервер...")
    push_out, push_err, push_code = run_git_command("git push origin main")
    if push_code != 0:
        print(f"❌ Ошибка при пуше: {push_err}")
        sys.exit(1)

    print("✅ Готово! Изменения успешно отправлены на сервер.")


# Точка входа в программу
if __name__ == "__main__":
    main()

