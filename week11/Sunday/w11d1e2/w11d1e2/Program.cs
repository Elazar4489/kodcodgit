using System;

namespace E3;

class ExampleThree
{
    static void Main()
    {
        Console.Write("Enter speed: ");
        string raw = Console.ReadLine();
        if (double.TryParse(raw, out double speed)) // true if it parsed, value goes into speed
        {
            string band;
            if (speed < 200) band = "slow";
            else if (speed < 600) band = "cruise";
            else band = "fast";
            Console.WriteLine($"Speed {speed} -> {band}");
        }
        else
        {
            Console.WriteLine("That was not a number.");
        }
    }
}