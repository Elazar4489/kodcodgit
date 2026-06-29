using System;
using System.Transactions;

namespace ExerciseSunday
{
    enum AType
    {
        Saving,
        Chacking,
        Business
    }
    class Program
    {
        static void Main()
        {
            List<BankAccount> accounts = new List<BankAccount>();
            BankAccount a = new BankAccount(1, "avi", 300, "Saving");
            BankAccount b = new BankAccount(2, "elazar", 200, "Business");
            BankAccount c = new BankAccount(3, "meair", 299);
            BankAccount d = new BankAccount(4, "eliau");
            BankAccount e = new BankAccount(5, "shalom", 600, "Saving");
            BankAccount f = new BankAccount(6, "muchamad");
            BankAccount g = new BankAccount(7, "", -49, "demo");
            accounts.Add(a); accounts.Add(b); accounts.Add(c); accounts.Add(d); accounts.Add(e); accounts.Add(f); accounts.Add(g);
            foreach (BankAccount ones in accounts)
            {
                Console.WriteLine($"at first: {ones.Balance}");
            }
            a.Deposit(100);
            b.Deposit(900);
            c.Withdraw(50);
            e.Withdraw(300);
            c.Withdraw(700);
            f.Deactivate();
            f.Deposit(70);
            f.Activate();
            foreach (BankAccount ones in accounts)
            {
                Console.WriteLine($"befor: {ones.Balance}");
                ones.ApplyInterest();
                Console.WriteLine($"after: {ones.Balance}");
            }
            Console.WriteLine($"from {a.OwnerName} balance befor {a.Balance} to {b.OwnerName} balance befor {b.Balance}");
            BankAccount.Transfer(a, b, 200);
            Console.WriteLine($"from {a.OwnerName} balance after {a.Balance} to {b.OwnerName} balance after {b.Balance}");
            a.PrintTransactionHistory();
            b.PrintTransactionHistory();
            foreach (BankAccount ones in accounts)
            {
                Console.WriteLine(ones);
            }
            }
    }
    class BankAccount
    {
        private int _accountNumber { get; }
        private string _ownerName;
        private double _balance;
        private string _accountType;
        private bool _isActive;
        private List<string> _transactionHistory;
        
        public string OwnerName
        {
            get => _ownerName;
            set 
            {
                if (string.IsNullOrWhiteSpace(value))
                    _ownerName = "Unknown";
                else _ownerName = value;
            }
        }
        public double Balance
        {
            get => _balance;
            set
            {
                if (value < 0)
                    _balance = 0.0;
                else _balance = value;
            }
        }
        public string AccountType
        {
            get => _accountType;
            set
            {
                if (Enum.TryParse(value, true, out AType thisType))
                {
                    _accountType = value;
                    
                }
                else 
                {
                    _accountType = "Chacking";
                }
            }
        }
        private bool IsActive
        {
            get => _isActive;
            set
            {
               _isActive = value;
            }
        }
        public BankAccount(int accountNumber, string ownerName, double balance, string accountType)
        {
            _accountNumber = accountNumber;
            OwnerName = ownerName;
            Balance = balance;
            AccountType = accountType;
            IsActive = true;
            _transactionHistory = new List<string>();

        }
        public BankAccount(int accountNumber, string ownerName) : this(accountNumber, ownerName, 0.0, "Checking") { }
        public BankAccount(int accountNumber, string ownerName, double initialDeposit) : this(accountNumber, ownerName, initialDeposit, "Checking") { }
        public override string ToString()
            => $"Account #[{_accountNumber}] | Owner: [{_ownerName}] | Balance: $[{ _balance.ToString("F2")}] | Type: [{_accountType}]";
        public void Deposit(double amount)
        {
            if (amount > 0)
            {
                Balance += amount;
                _transactionHistory.Add($"Deposited ${amount}");
            }
            else
            {
                Console.WriteLine("amount is negative");
            }
        }
        public bool Withdraw(double amount)
        {
            if (amount > 0 && Balance >= amount)
            {
                Balance -= amount;
                _transactionHistory.Add($"Withdrawed ${amount}");
                return true;
            }
            Console.WriteLine("amount is negative");
            return false;
        }
        public void ApplyInterest()
        {
            if (Enum.Parse<AType>(AccountType, true) == AType.Saving)
            {
                Balance = Balance * 1.02;
            }
        }
        public void PrintTransactionHistory()
        {
            foreach (string Transaction in _transactionHistory)
            {
                Console.WriteLine(Transaction);
            }
        }
        public void Activate()
        {
            IsActive = true;
        }
        public void Deactivate()
        {
            IsActive = false;
        }
        public static bool Transfer(BankAccount from, BankAccount to, double amount)
        {
            if (from.IsActive && to.IsActive && amount > 0 && from.Balance >= amount)
            {
                from.Balance -= amount;
                to.Balance += amount;
                from._transactionHistory.Add($"{amount} transfer to {to._accountNumber}");
                to._transactionHistory.Add($"{amount} transfer from {from._accountNumber}");
                return true;
            }
            else Console.WriteLine("canno't transfer");
            return false;
            
        }
    }
}