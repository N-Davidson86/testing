import subprocess
import sys

def run_git_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def get_current_branch():
    """Получает имя текущей ветки."""
    out, err, code = run_git_command("git rev-parse --abbrev-ref HEAD")
    if code != 0:
        print(f"❌ Не удалось получить ветку: {err}")
        sys.exit(1)
    return out

def main():
    branch = get_current_branch()
    print(f"📂 Текущая ветка: {branch}")

    # Защита: не пушим в main без подтверждения
    if branch == "main":
        confirm = input("⚠️ Вы находитесь в ветке main. Пушить напрямую в main опасно. Подтвердить? (y/n): ")
        if confirm.lower() != 'y':
            print("❌ Отмена пуша в main.")
            sys.exit(0)

    status_out, _, status_code = run_git_command("git status --porcelain")
    if not status_out:
        print("✅ Репозиторий чист. Нет изменений для коммита.")
        sys.exit(0)

    print("📝 Обнаружены изменения:")
    print(status_out)

    commit_message = input("\nВведите сообщение для коммита (или 'q' для отмены): ")
    if commit_message.lower() == 'q':
        print("❌ Отмена.")
        sys.exit(0)
    if not commit_message:
        print("❌ Сообщение не может быть пустым.")
        sys.exit(1)

    print("\n⏳ Добавляю файлы...")
    add_out, add_err, add_code = run_git_command("git add -A")
    if add_code != 0:
        print(f"❌ Ошибка git add: {add_err}")
        sys.exit(1)

    print("⏳ Создаю коммит...")
    commit_out, commit_err, commit_code = run_git_command(f'git commit -m "{commit_message}"')
    if commit_code != 0:
        # Если нет изменений для коммита (например, все файлы игнорируются), это не ошибка
        if "nothing to commit" in commit_err.lower():
            print("⚠️ Нет новых изменений для коммита после git add.")
            # Но мы всё равно не делаем push, если коммит не создан
            sys.exit(0)
        print(f"❌ Ошибка при коммите: {commit_err}")
        sys.exit(1)

    print("⏳ Отправляю на сервер...")
    # Пушим в текущую ветку: origin/<branch>
    push_out, push_err, push_code = run_git_command(f"git push origin {branch}")
    if push_code != 0:
        print(f"❌ Ошибка при пуше: {push_err}")
        sys.exit(1)

    print(f"✅ Готово! Изменения отправлены в ветку {branch}.")

if __name__ == "__main__":
    main()

