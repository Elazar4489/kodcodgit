using System;

namespace Examples
{
    class Exam
    {
        static void Main()
        {
            AddTrack("01", 250);
            AddTrack("02", 300);
            AddTrack("03", 390);
            Console.WriteLine(AverageSpeed());
            Report();
            Report("03");
            List<string> fast = FastTracks(300);
            Console.WriteLine($"{fast.Count} fast tracks");
        }
        static List<string> tracks = new List<string>();
        static List<double> speeds = new List<double>();
        static void AddTrack(string id, double speed)
        {
            tracks.Add(id);
            speeds.Add(speed);
        }
        static double AverageSpeed()
        {
            if (speeds.Count == 0) return 0.0;
            double sum = 0;
            foreach (double s in speeds) sum += s;
            return sum / speeds.Count;
        }
        static void Report() // version 1: no parameters
            => Console.WriteLine($"{tracks.Count} tracks");
        static void Report(string id)
        {
            int i = tracks.IndexOf(id);
            if (i >= 0) Console.WriteLine($"{id}: {speeds[i]} kn");
            else Console.WriteLine($"{id} not found");
        }
        static List<string> FastTracks(double threshold)
        {
            List<string> result = new List<string>();
            for (int i = 0; i < tracks.Count; i++)
            {
                if (speeds[i] > threshold)
                    result.Add(tracks[i]);
            }
            return result;
        }
       
    }
}

