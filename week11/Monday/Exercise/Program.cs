using System;

namespace ExerciseMonday
{
    class Tracks
    {
        
        static void Main()
        {
            List<int> ids = new List<int>();
            List<string> headings = new List<string>();
            List<int> speeds = new List<int>();
            AddTrack(300, "hfj", ids, speeds, headings);
            AddTrack(250, "chaaa", ids, speeds, headings);
            AddTrack(180, "miau", ids, speeds, headings);
            Console.WriteLine(GetTrackByID(1, ids, speeds, headings));
            Console.WriteLine(GetTrackByID(2, ids, speeds, headings));
            Console.WriteLine(GetTrackByID(3, ids, speeds, headings));
            Console.WriteLine(DeleteTrack(3, ids, speeds, headings));
            Console.WriteLine(GetTrackByID(3, ids, speeds, headings));
            Console.WriteLine(GetAllTracks(ids, speeds, headings));
        }
        static bool AddTrack(int speed, string heading, List<int> ids, List<int> speeds, List<string> headings)
        {
            speeds.Add(speed);
            headings.Add(heading);
            int lastID = ids.Count == 0 ? 1 : ids[^1] + 1;
            ids.Add(lastID);
            return true;
        }
        static bool DeleteTrack(int id, List<int> ids, List<int> speeds, List<string> headings)
        {
            for (int i = 0; i < ids.Count; i++)
            {
                if (ids[i] == id)
                {
                    speeds.Remove(speeds[i]);
                    headings.Remove(headings[i]);
                    ids.Remove(ids[i]);
                    return true;
                }
            }
            return false;
        }
        static string GetTrackByID(int id, List<int> ids, List<int> speeds, List<string> headings)
        {
            for (int i = 0; i < ids.Count; i++)
            {
                if (ids[i] == id)
                {
                    string TrackByID = $"TrackID: {id}, Heading: {headings[i]}, speed: {speeds[i]}";
                    return TrackByID;
                }
            }
            return "not found";
        }
        static List<string> GetAllTracks(List<int> ids, List<int> speeds, List<string> headings)
        {
            List<string> AllTracks = new List<string>();
            foreach (int i in ids)
            {
                AllTracks.Add(GetTrackByID(i, ids, speeds, headings));
            }
            return AllTracks;
        }
        //static List<Array> FilterTracks()
        //{

        //}
        //static string FleetSummary()
        //{

        //}
    }
}