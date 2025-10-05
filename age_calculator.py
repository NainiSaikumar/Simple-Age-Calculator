"""Simple Age Calculator
Calculates your exact age in years, months, and days using your date of birth.
"""

from datetime import datetime


def calculate_age(birth_date: datetime) -> tuple[int, int, int]:
    """Calculate age in years, months, and days."""
    today = datetime.today()

    # Check for invalid (future) date
    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust negative values
    if days < 0:
        months -= 1
        prev_month = (today.month - 1) or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def main():
    print("=== Simple Age Calculator ===")
    while True:
        dob_str = input("Enter your Date of Birth (DD-MM-YYYY): ").strip()
        try:
            birth_date = datetime.strptime(dob_str, "%d-%m-%Y")
            years, months, days = calculate_age(birth_date)

            print(f"\n🧾 You are {years} years, {months} months, and {days} days old.")

            today = datetime.today()
            if birth_date.day == today.day and birth_date.month == today.month:
                print("🎉 Happy Birthday! 🎂")

        except ValueError as e:
            print(f"⚠️ Error: {e}. Please enter a valid date (DD-MM-YYYY).")

        again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye! Stay young at heart ❤️")
            break


if __name__ == "__main__":
    main()
