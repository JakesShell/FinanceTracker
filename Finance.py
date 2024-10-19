import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
def load_data():
    try:
        return pd.read_csv('data.csv')
    except FileNotFoundError:
        # Return an empty DataFrame with specified columns if the file doesn't exist
        return pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Type'])

# Save data to CSV file
def save_data(df):
    df.to_csv('data.csv', index=False)

# Add a transaction to the tracker
def add_transaction(date, description, amount, t_type):
    df = load_data()
    df = df.append({'Date': date, 'Description': description, 'Amount': amount, 'Type': t_type}, ignore_index=True)
    save_data(df)

# Show summary of finances
def show_summary():
    df = load_data()
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Net Savings: ${income - expenses:.2f}")

# Visualize income and expenses using a bar chart
def visualize_data():
    df = load_data()
    df.groupby('Type')['Amount'].sum().plot(kind='bar', color=['green', 'red'])
    plt.title('Income vs Expenses')
    plt.xlabel('Type')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Main program loop
if __name__ == "__main__":
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. Show Summary")
        print("3. Visualize Data")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            t_type = input("Enter type (Income/Expense): ")
            add_transaction(date, description, amount, t_type)
            print("Transaction added successfully.")
        elif choice == '2':
            show_summary()
        elif choice == '3':
            visualize_data()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
