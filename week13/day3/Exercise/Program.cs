namespace ExerciseDay3
{
    public class Book
    {
        public string Title { get; set; }
        public string Author { get; set; }
        public string ISBN { get; set; }
    }
    public class MemoryLendingStore
    {
        private List<string> _records = new List<string>();
        public void RecordLending(Book book, string borrowerName)
        {
            string record = $"ISBN: {book.ISBN} borrowed by {borrowerName}";
            _records.Add(record);
        }
        public int GetTotalLendings()
        {
            return _records.Count;
        }
    }
    public class LibraryService
    {
        // ❌ BAD: Creating the dependency INSIDE the class with 'new'
        private MemoryLendingStore _store = new MemoryLendingStore();
        public void LendBook(Book book, string borrowerName)
        {
            Console.WriteLine($"Lending '{book.Title}' to {borrowerName}");
            _store.RecordLending(book, borrowerName);
        }
        public int GetTotalLendings()
        {
            return _store.GetTotalLendings();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            // Create some books
            Book book1 = new Book
            {
                Title = "1984",
                Author = "George Orwell",
                ISBN =
            "978-0451524935"
            };
            Book book2 = new Book
            {
                Title = "The Hobbit",
                Author = "J.R.R. Tolkien",
                ISBN =
            "978-0547928227"
            };
            Book book3 = new Book
            {
                Title = "Clean Code",
                Author = "Robert Martin",
                ISBN =
            "978-0132350884"
            };
            // Create the library service (notice: NO parameters needed - that's the problem!)
            LibraryService library = new LibraryService();
            // Lend the books
            library.LendBook(book1, "Alice");
            library.LendBook(book2, "Bob");
            library.LendBook(book3, "Charlie");
            // Print total
            Console.WriteLine($"\nTotal lendings: {library.GetTotalLendings()}");
        }
    }

}