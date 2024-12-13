import tkinter as tk
import random

class Donate:
    def __init__(self, donor, amount):
        self.donor = donor
        self.amount = amount

class Leaderboard:
    def __init__(self):
        self.leaderboard = {}

    def add_donation(self, donor, amount):
        if donor in self.leaderboard:
            self.leaderboard[donor] += amount
        else:
            self.leaderboard[donor] = amount

    def get_leaderboard(self):
        return sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)

def generate_fake_donations(names, n):
    for _ in range(n):
        donor = random.choice(names)
        amount = random.randint(10, 500)
        yield Donate(donor, amount)

class DonationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Donation App")
        self.leaderboard = Leaderboard()
        self.fake_names = [
            "John", "Emma", "Sophia", "James", "Olivia",
            "Michael", "Liam", "isabella", "ethan", "Mia",

            "Charlotte", "benjamin", "Amelia", "Alexander", "elijah",
            "Harper", "Lucas", "Ava", "Daniel", "Scarlett"
        ]
        for donation in generate_fake_donations(self.fake_names, 20):
            self.leaderboard.add_donation(donation.donor, donation.amount)
        self.create_donation_window()

    def create_donation_window(self):
        self.donation_window = tk.Toplevel(self.root)
        self.donation_window.title("Thank you! Anything helps :)")

        tk.Label(self.donation_window, text="Please put you name here >").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.donation_window, text="Please put your donation here >").grid(row=1, column=0, padx=10, pady=5)

        self.name_entry = tk.Entry(self.donation_window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.amount_entry = tk.Entry(self.donation_window)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.donation_window, text="Submit (Thank you again <3)", command=self.submit_donation).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.donation_window, text="Exit", command=self.root.quit).grid(row=3, column=0, columnspan=2, pady=5)

    def submit_donation(self):
        name = self.name_entry.get()
        try:
            amount = int(self.amount_entry.get())
        except ValueError:
            return
        self.leaderboard.add_donation(name, amount)
        self.donation_window.destroy()
        self.show_leaderboard_window()

    def show_leaderboard_window(self):
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("Thankful for all of you...")

        tk.Label(leaderboard_window, text="Donors as generous as you", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(leaderboard_window, text="Amount Donated", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

        for i, (donor, amount) in enumerate(self.leaderboard.get_leaderboard(), start=1):
            tk.Label(leaderboard_window, text=donor).grid(row=i, column=0, padx=10, pady=5)
            tk.Label(leaderboard_window, text=f"${amount}").grid(row=i, column=1, padx=10, pady=5)

        tk.Button(leaderboard_window, text="Exit", command=self.root.quit).grid(row=i + 1, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = DonationApp(root)
    root.mainloop()
