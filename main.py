from rich.console import Console
from engine import Question, Match
import time

console = Console()

def get_players():
    player1 = input("نام بازیکن اول: ")
    player2 = input("نام بازیکن دوم: ")

    return player1, player2

def create_match():
    player1, player2 = get_players()

    match = Match(player1, player2, questions)

    return match


questions = [
    Question("پایتخت ژاپن کدام است؟", ["توکیو", "کیوتو", "اوساکا", "سئول"], "A"),
    Question("خروجی len('سلام') چیست؟", ["3", "4", "5", "خطا"], "B"),
    Question("بزرگ‌ترین سیاره‌ی منظومه‌ی شمسی؟", ["زمین", "زحل", "مشتری", "نپتون"], "C"),
    Question("نماد شیمیایی طلا چیست؟", ["Ag", "Au", "Fe", "Gd"], "B"),
    Question("شاهنامه اثر کیست؟", ["حافظ", "سعدی", "فردوسی", "مولوی"], "C"),
]


def start_game():
    match = create_match()

    console.print("مسابقه شروع شد!", style="bold green")
    for i in range(5):
        question = match.start_round()

        console.print(f"\nراند {match.round}", style="bold yellow")

        for player in match.players:
            ask_player(match, player, question)

        results = match.resolve_round()
        for player, result in results.items():
            console.print(
        f"{player}: {result.status} | امتیاز این راند: {result.points}"
    )
            console.print("\n[bold cyan]نتیجه نهایی مسابقه[/bold cyan]")

    for player in match.players:
        console.print(f"{player}: {match.score_of(player)} امتیاز")

    winner = match.winner()

    if winner is None:
        console.print("بازی مساوی شد!", style="bold yellow")
    else:
        console.print(f"برنده مسابقه: {winner} 🏆", style="bold green")
    return match

def ask_player(match, player, question):
    console.print(f"\nنوبت {player} است!")

    console.print(question.text)

    for letter, option in zip("ABCD", question.options):
        console.print(f"{letter}) {option}")

    start_time = time.perf_counter()

    answer = input("جواب شما (A-D): ")

    elapsed = time.perf_counter() - start_time

    match.submit(player, answer, elapsed)
    
def show_menu():
    console.print("\n[bold cyan]Quiz Battle[/bold cyan]")
    console.print("[bold green]۱)[/bold green] بازی جدید")
    console.print("[bold red]۲)[/bold red] خروج")


def play():
    total = len(questions)
    score = 0
    correct_count = 0

    for i, q in enumerate(questions, start=1):
        console.print(f"\n[bold cyan]سؤال {i} از {total}:[/bold cyan] {q.text}")
        for letter, opt in zip("ABCD", q.options):
            console.print(f"  [bold]{letter})[/bold] {opt}")

        answer = input("جواب تو (A-D): ")

        if q.is_correct(answer):
            console.print(" درست!", style="bold green")
            score += 10
            correct_count += 1
        else:
            console.print(f" غلط! جواب درست: {q.correct}", style="bold red")

    return score, correct_count, total

def show_results(score, correct_count, total):
    percent = correct_count / total * 100
    console.print("\n بازی تمام شد!", style="bold yellow")
    console.print(f"   امتیاز تو: [bold green]{score}[/bold green]")
    console.print(f"   درست: {correct_count} از {total}  ([bold]{percent:.0f}٪[/bold])")

while True:
    show_menu()
    choice = input("انتخاب تو (۱ یا ۲): ").strip()
    if choice in ("2", "۲"):
        console.print("خداحافظ!", style="bold cyan")
        break
    if choice not in ("1", "۱"):
        continue
    
start_game()

    