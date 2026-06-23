using System;
namespace ExerciseTuesday
{
    public enum Importances 
    { 
        Friendly, 
        Hostile, 
        Unidentified
    }
    class Transmissions
    {
        static void Main()
        {
            List<string> ids = new List<string>();
            List<string> levels = new List<string>();
            List<double> powers = new List<double>();
            bool flag = false; 
            while (flag)
            {
                Console.WriteLine("1. log a new transmission\n\r" +
                    "2. calibrate the strength of an existing source\n\r" +
                    "3. calibrate the strength of an existing source\n\r" +
                    "4. exit");
                Console.Write("Enter your choice: ");
                string choice = Console.ReadLine()!;
                if (choice == "1")
                {
                    Console.Write("Enter the level: ");
                    string level = Console.ReadLine()!;
                    Console.Write("Enter the power: ");
                    string powerStr = Console.ReadLine()!;
                    double power = double.Parse(powerStr);
                    if (CheckPower(power) && CheckLevel(level))
                    {
                        AddNew(level, power, ids, levels, powers);
                    }
                }
                if (choice == "2")
                {
                    Console.Write("Enter the id: ");
                    string id = Console.ReadLine()!;
                    Console.Write("Enter the power: ");
                    string powerStr = Console.ReadLine()!;
                    double power = double.Parse(powerStr);
                    if (CheckPower(power) && CheckID(id, ids))
                    {
                        int index = GetIndex(id, ids);
                        UpdateLevel(index, power, powers);
                    }
                }
            }
        }
        static bool CheckLevel(string importance)
        {
            if (Enum.TryParse(importance, true, out Importances selectedImportance))
            {
                if (selectedImportance == Importances.Friendly)
                {
                    return true;
                }
                else if (selectedImportance == Importances.Hostile)
                {
                    return true;
                }
                else if (selectedImportance == Importances.Unidentified)
                {
                    return true;
                }
            }

            
            return false;
        }
        static bool CheckPower(double power)
        {
            if (power > 0)
            {
                return false;
            }
            return true;
        }
        static bool CheckID(string id, List<string> ids)
        {
            foreach (string i in ids)
            {
                if (id == i)
                {
                    return true;
                }
            }
            return false;
        }
        static int GetIndex(string id, List<string> ids)
        {
            int index = new int();
            for (int i = 0; i < ids.Count; i++)
            {
                if (ids[i] == id)
                {
                    index = i;
                }
            }
            return index;
        }

        static string AddNew(string importance, double intensity, List<string> ids, List<string> levels, List<double> powers)
        {

            int lastid = new int();
            if (ids.Count > 0)
            {
                lastid = int.Parse(ids[^1]);
                lastid++;
            }
            else
            {
                lastid = 1;
            }
            string lastID = lastid.ToString();
            levels.Add(importance);
            powers.Add(intensity);
            ids.Add(lastID);
            return "Add succesfull";
        }
        static string UpdateLevel(int index, double power, List<double> powers)
        {
            powers[index] = power;
            return "done";
        }
    }
}