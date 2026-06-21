namespace SingleTrackConsoleReadout;

class ConsoleReadout
{
    static void Main()
    {
        int TrackID = 0;
        int Heading = 0;
        int Speed = 0;
        string status = "";

        bool flag = true;
        while (flag)
        {
            Console.Write("Enter the Track ID: ");
            string trackId = Console.ReadLine();
            if (int.TryParse(trackId, out TrackID))
            {
                flag = false;
            }
        }

        flag = true;
        while (flag)
        {
            Console.Write("Enter the Speed: ");
            string speed = Console.ReadLine();
            if (int.TryParse(speed, out Speed))
            {
                flag = false;
            }
        }

        flag = true;
        while (flag)
        {
            Console.Write("Enter the Heading: ");
            string heading = Console.ReadLine();
            if (int.TryParse(heading, out Heading))
            {
                flag = false;
            }
        }

        flag = true;
        while (flag)
        {
            Console.Write("Enter the Status: ");
            status = Console.ReadLine();
            string[] StatusTypes = { "cruising", "turning", "stopped", "accelerating" };
            bool statusValid = StatusTypes.Contains(status);
            if (statusValid)
            {
                flag = false;
            }
        }

        string category;
        if (Speed <= 100) category = "slow";
        else if (Speed <= 300) category = "cruise";
        else category = "fast";

        int divDemo1 = Heading / 30;
        int divDemo2 = Speed / 60;
        double demo1 = (double)Heading / 30;
        double demo2 = (double)Speed / 60;
        Console.WriteLine(
            $"=== Track Report ===\r\n" +
            $"Track ID: {TrackID}\r\n" +
            $"Speed: {Speed} km/h {category}\r\n" +
            $"Heading: {Heading} degrees\r\n" +
            $"Status: {status}\r\n" +
            $"Division Demo 1: {Heading}/30 = {divDemo1} (int) | {demo1} (double)" +
            $"\r\nDivision Demo 2: {Speed}/60 = {divDemo2} (int) | {demo2} (double)"
            );
    }
}
