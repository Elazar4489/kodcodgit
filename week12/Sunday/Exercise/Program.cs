using System;

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
            BankAccount a = new BankAccount(1234, "Elazar", 200.0, "Saving");
            a.Deposit(130.9);
            a.Deposit(590.0);
            a.Withdraw(300.8);
            a.PrintTransactionHistory();
            Console.WriteLine(a);
        }
    }
    class BankAccount
    {
        private int _accountNumber { get; }
        private string _ownerName { get; set; }
        private double _balance { get; set; }
        private string _accountType { get; set; }
        private bool _isActive { get; set; }
        private List<string> _transactionHistory { get; set; }
        public List<string> TransactionHistory
        {
            get => _transactionHistory;
            set
            {
                new List<string>();
            }
        }
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
                if (!value)
                    _isActive = true;
                else _isActive = value;
            }
        }
        public BankAccount(int accountNumber, string ownerName, double balance, string accountType)
        {
            _accountNumber = accountNumber;
            OwnerName = ownerName;
            Balance = balance;
            AccountType = accountType;
            IsActive = _isActive;
            _transactionHistory = TransactionHistory;

        }
        public BankAccount(int accountNumber, string ownerName) : this(accountNumber, ownerName, 0.0, "Checking") { }
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
            foreach (string Transaction in TransactionHistory)
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
    }
}