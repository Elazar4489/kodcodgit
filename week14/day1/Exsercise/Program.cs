using System.Text.Json;

namespace ExserciseDay1
{
    public class PriorityNegativeException : Exception { public PriorityNegativeException(string Message) : base(Message) { } }
    class Program
    {
        static void Main()
        {
            ReadFile readFile = new ReadFile();
            readFile.SaveToJson(readFile.CheckLinesAndCreateObject("w4d1_field_reports_input.txt"), "new_json.json");
            readFile.LoadFromJson("w4d1_reports.json");
            readFile.LoadFromJson("w4d1_reports_corrupted.json");
            readFile.LoadFromJson("new_json.json");
        }
    }
    class Report
    {
        public int Id { get; set; }
        public string Category { get; set; }
        public int Priority { get; set; }
        public Report(int id, string category, int priority) { Id = id; Category = category; Priority = priority; }
    }
    class ReadFile
    {
        public ReadFile() { }
        public List<Report> CheckLinesAndCreateObject( string path)
        {
            int accepted = 0;
            int rejected = 0;
            List<Report> reports = new List<Report>();
            try              
            {
                using (StreamReader reader = new StreamReader(path))
                {
                    string? line;
                    while ((line = reader.ReadLine()) != null)
                    {
                        try      
                        {
                            string[] parts = line.Split(" ");
                            int id = int.Parse(parts[0]);
                            string category = parts[1];
                            int priority = int.Parse(parts[2]);
                            if (priority >= 0)
                            {
                                reports.Add(new Report(id, category, priority));
                                accepted++;
                            }
                            else
                            {
                                throw new PriorityNegativeException("Priority cannot be negative.");
                            }
                        }
                        catch (FormatException ex)
                        {
                            Console.WriteLine(ex.Message);
                            rejected++;
                        }
                        catch (PriorityNegativeException ex)
                        {
                            Console.WriteLine(ex.Message);
                            rejected++;
                        }
                    }
                }
            }
            catch (FileNotFoundException ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                Console.WriteLine($"accepted: {accepted}. rejected: {rejected}.");
            }
            return reports;
        }
        public void SaveToJson(List<Report> reports, string path)
        {
            string jsonStr = JsonSerializer.Serialize(reports, new JsonSerializerOptions{WriteIndented = true});
            using (StreamWriter writer = new StreamWriter(path))
            {
                writer.Write(jsonStr);
            }
        }
        public void LoadFromJson(string path)
        {
            try
            {
                using (StreamReader reader = new StreamReader(path))
                {
                    string jsonStr = reader.ReadToEnd();
                    List<Report> reports = JsonSerializer.Deserialize<List<Report>>(jsonStr);
                    if (reports is not null)
                    {
                        foreach (Report report in reports)
                        {
                            Console.WriteLine($"{report.Id}, {report.Category}, {report.Priority}.");
                        }
                    }
                }
            }
            catch (FileNotFoundException ex)
            {
                Console.WriteLine(ex.Message);
            }
            catch (JsonException ex)
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine(ex.StackTrace);
            }
        }
    }
}