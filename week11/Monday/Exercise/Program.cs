using System;

namespace ExerciseMonday
{
    class Tracks
    {
        
        static void Main()
        {
            List<Dictionary<string, string>> data = new List<Dictionary<string, string>>();
            List<int> ids = new List<int>();
            List<string> headings = new List<string>();
            List<int> speeds = new List<int>();
            //AddTrack(300, "hfj", ids, speeds, headings);
            //AddTrack(250, "chaaa", ids, speeds, headings);
            //AddTrack(180, "miau", ids, speeds, headings);
            //Console.WriteLine(GetTrackByID(1, ids, speeds, headings));
            //Console.WriteLine(GetTrackByID(2, ids, speeds, headings));
            //Console.WriteLine(GetTrackByID(3, ids, speeds, headings));
            //Console.WriteLine(DeleteTrack(3, ids, speeds, headings));
            //Console.WriteLine(GetTrackByID(3, ids, speeds, headings));
            //Console.WriteLine(GetAllTracks(ids, speeds, headings));
        }
        static bool AddTrack(int speed, string heading, List<Dictionary<string, string>> data)
        {
            int lastid = data.Count == 0 ? 1 : (int)data[^1]["id"] + 1;
            string lastID = (string)lastid;
            Dictionary<string, string> track = new Dictionary<string, string>()
            {
                {"id", lastID },
                {"speed", speed },
                {"heading", heading }
            }
            data.Add(track);
            //speeds.Add(speed);
            //headings.Add(heading);
            
            //ids.Add(lastID);
            return true;
        }
        static bool DeleteTrack(string id, List<Dictionary<string, string>> data)
        {
            for (int i = 0; i < data.Count; i++)
            {
                if (data[i]["id"] == id)
                {
                    data.Remove(data[i])
                    //speeds.Remove(speeds[i]);
                    //headings.Remove(headings[i]);
                    //ids.Remove(ids[i]);
                    return true;
                }
            }
            return false;
        }
        static string GetTrackByID(string id, List<Dictionary<string, string>> data)
        {
            for (int i = 0; i < data.Count; i++)
            {
                if (data[i]["id"] == id)
                {
                    string TrackByID = $"TrackID: {id}, Heading: {data[i]["headings"]}, speed: {data[i]["speeds"]}";
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