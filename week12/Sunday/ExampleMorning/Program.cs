using System;

namespace Mornung
{
    class MainSun
    {
        static void Main()
        {
            Track full = new Track(17, 412.5, 270);
            Track quick = new Track(8);
            Track anotherTrack = new Track(3, 4.5);
            Console.WriteLine($"{full.Id},{full.Speed}, {full.Heading}");
            Console.WriteLine($"{quick.Id},{quick.Speed}, {quick.Heading}");
        }
    } 
    class Track
    {
        public int Id;
        public double Speed;
        public double Heading;
        // full constructor — the one real setup lives here
        public Track(int id, double speed, double heading)
        {
            Id = id;
            Speed = speed;
            Heading = heading;
            Console.WriteLine("1 con");
        }
        // overloaded + chained: forwards to the full one, no duplicated setup
        public Track(int id) : this(id, 0.0, 0.0) { Console.WriteLine("2 con"); }
        public Track(int id, double heading) 
        {
            Id = id;
            Speed = 5.0;
            Heading = heading;
            Console.WriteLine("3 con");
        }
    }
}
