import random

def get_difficulty():
    """سطح دشواری رو از کاربر میگیره"""
    print("\n🎮 به بازی حدس عدد خوش اومدی!")
    print("-" * 35)
    print("سطح دشواری رو انتخاب کن:")
    print("  1 - آسون   (1 تا 50  |  10 شانس)")
    print("  2 - متوسط  (1 تا 100 |  7 شانس)")
    print("  3 - سخت    (1 تا 200 |  5 شانس)")
    print("-" * 35)

    while True:
        choice = input("انتخابت (1/2/3): ").strip()
        if choice == "1":
            return 50, 10, "آسون"
        elif choice == "2":
            return 100, 7, "متوسط"
        elif choice == "3":
            return 200, 5, "سخت"
        else:
            print("❌ فقط 1، 2 یا 3 وارد کن!")


def get_hint(guess, secret, max_num):
    """راهنمایی هوشمند به کاربر میده"""
    diff = abs(guess - secret)
    percent = diff / max_num

    if guess < secret:
        direction = "⬆️  بزرگتره!"
    else:
        direction = "⬇️  کوچیکتره!"

    if percent > 0.4:
        warmth = "🧊 خیلی سرد"
    elif percent > 0.2:
        warmth = "😐 سرد"
    elif percent > 0.1:
        warmth = "🌡️  گرم میشه"
    elif percent > 0.05:
        warmth = "🔥 داغه!"
    else:
        warmth = "🌋 خیلی داغ!!!"

    return f"{direction}  ({warmth})"


def calculate_score(attempts, max_attempts, max_num):
    """امتیاز بازیکن رو حساب میکنه"""
    if attempts == 1:
        return 1000
    efficiency = (max_attempts - attempts + 1) / max_attempts
    base_score = int(efficiency * 500)
    bonus = max(0, 100 - attempts * 10)
    return base_score + bonus


def play_game():
    """منطق اصلی بازی"""
    max_num, max_attempts, level_name = get_difficulty()
    secret = random.randint(1, max_num)
    attempts = 0
    history = []

    print(f"\n✅ سطح {level_name} انتخاب شد!")
    print(f"یه عدد بین 1 تا {max_num} فکر کردم...")
    print(f"تا {max_attempts} تلاش داری. بریم!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"[تلاش {attempts + 1}/{max_attempts}]  ({remaining} شانس مونده)")

        # گرفتن ورودی از کاربر
        while True:
            try:
                guess = int(input(f"عددت بین 1 تا {max_num}: "))
                if 1 <= guess <= max_num:
                    break
                print(f"❌ عدد باید بین 1 تا {max_num} باشه!")
            except ValueError:
                print("❌ فقط عدد وارد کن!")

        attempts += 1
        history.append(guess)

        if guess == secret:
            score = calculate_score(attempts, max_attempts, max_num)
            print(f"\n{'🎉' * 5}")
            print(f"آفرین! عدد {secret} بود!")
            print(f"در {attempts} تلاش بردی!")
            print(f"امتیازت: {score} ⭐")
            if attempts == 1:
                print("🏆 واو! اولین تلاش! یه معجزه‌ست!")
            elif attempts <= max_attempts // 2:
                print("💪 عالی بود!")
            return True, attempts, score

        else:
            hint = get_hint(guess, secret, max_num)
            print(f"   {hint}")
            print(f"   حدس‌های قبلی: {history}\n")

    # بازی تموم شد و نبرد
    print(f"\n😔 تلاش‌هات تموم شد!")
    print(f"عدد مخفی {secret} بود.")
    print(f"حدس‌هات: {history}")
    return False, max_attempts, 0


def main():
    """حلقه اصلی برنامه"""
    total_wins = 0
    total_games = 0
    best_score = 0

    print("=" * 40)
    print("   🎯 NUMBER GUESSING GAME 🎯")
    print("        نوشته شده با Python")
    print("=" * 40)

    while True:
        won, attempts, score = play_game()
        total_games += 1

        if won:
            total_wins += 1
            if score > best_score:
                best_score = score
                print(f"🥇 رکورد جدید! بهترین امتیاز: {best_score}")

        print(f"\n📊 آمار کلی:")
        print(f"   بازی‌ها: {total_games}  |  بردها: {total_wins}  |  بهترین: {best_score}")

        again = input("\n🔄 دوباره بازی کنی؟ (y/n): ").strip().lower()
        if again != 'y':
            print(f"\n👋 ممنون که بازی کردی!")
            print(f"🏅 نتیجه نهایی: {total_wins} برد از {total_games} بازی")
            break


if __name__ == "__main__":
    main()
