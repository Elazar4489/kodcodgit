using ExerciseDay3.Phase2;

namespace ExerciseDay3
{
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
            Console.WriteLine("=== Test 1: Using MemoryLendingStore ===");
            // Create the library service (notice: NO parameters needed - that's the problem!)
            ILendingStore memoryStore = new MemoryLendingStore();
            LibraryService library1 = new LibraryService(memoryStore);

            // Lend the books
            library1.LendBook(book1, "Alice");
            library1.LendBook(book2, "Bob");
            library1.LendBook(book3, "Charlie");
            // Print total
            Console.WriteLine($"\nTotal lendings: {library1.GetTotalLendings()}");
            Console.WriteLine("=== Test 2: Using FileLendingStore ===");
            ILendingStore fileStore = new FileLendingStore("lendings.txt");
            LibraryService library2 = new LibraryService(fileStore);
            library2.LendBook(book3, "Charlie");
            library2.LendBook(book1, "Diana");
            Console.WriteLine($"Total lendings: {library2.GetTotalLendings()}");
            Console.WriteLine("Check the 'lendings.txt' file to see the records!");
        }
    }
    public class Book
    {
        public string Title { get; set; }
        public string Author { get; set; }
        public string ISBN { get; set; }
    }
   
    public class LibraryService
    {
        // ❌ BAD: Creating the dependency INSIDE the class with 'new'
        private readonly ILendingStore _store;
        public LibraryService(ILendingStore store)
        {
            _store = store ?? throw new ArgumentNullException(nameof(store));
        }
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
   

}