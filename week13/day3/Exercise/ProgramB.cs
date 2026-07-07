namespace ExerciseDay3.Phase2
{
    public interface ILendingStore
    {
        void RecordLending(Book book, string borrowerName);
        int GetTotalLendings();
    }

    public class MemoryLendingStore : ILendingStore
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

    public class FileLendingStore : ILendingStore
    {
        private string _filePath;
        // Constructor receives the file path
        public FileLendingStore(string filePath)
        {
            _filePath = filePath;
        }
        public void RecordLending(Book book, string borrowerName)
        {
            string record = $"{DateTime.Now:yyyy-MM-dd HH:mm} - ISBN: {book.ISBN} borrowed by{ borrowerName}";
        File.AppendAllText(_filePath, record + Environment.NewLine);
        }
        public int GetTotalLendings()
        {
            if (!File.Exists(_filePath))
                return 0;
            return File.ReadAllLines(_filePath).Length;
        }
    }

}