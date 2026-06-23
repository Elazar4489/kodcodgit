using System;

namespace ExerciseMonday
{
    class Tracks
    {
        
        static void Main()
        {
            List<Dictionary<string, string>> data = new List<Dictionary<string, string>>();
            //AddTrack(250, "travle", data);
            //AddTrack(320, "stopped", data);
            //Console.WriteLine(GetTrackByID("2", data));
            //DeleteTrack("2", data);
            //Console.WriteLine(GetTrackByID("2", data));
        }
        static bool AddTrack(int speed, string heading, List<Dictionary<string, string>> data)
        {
            int lastid = new int();
            if (data.Count > 0)
            {
                lastid = int.Parse(data[^1]["id"]);
                lastid++;
            }
            else
            {
                lastid = 1;
            }
            string lastID = lastid.ToString();
            string Speed = speed.ToString();
            Dictionary<string, string> track = new Dictionary<string, string>()
            {
                {"id", lastID },
                {"speed", Speed },
                {"heading", heading }
            };
            data.Add(track);
            return true;
        }
        static bool DeleteTrack(string id, List<Dictionary<string, string>> data)
        {
            for (int i = 0; i < data.Count; i++)
            {
                if (data[i]["id"] == id)
                {
                    data.Remove(data[i]);
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
                    string TrackByID = $"TrackID: {id}, Heading: {data[i]["heading"]}, speed: {data[i]["speed"]}";
                    return TrackByID;
                }
            }
            return "not found";
        }
        static List<string> GetAllTracks(List<Dictionary<string, string>> data)
        {
            List<string> AllTracks = new List<string>();
            foreach (Dictionary<string, string> i in data)
            {
                AllTracks.Add(GetTrackByID(i["id"], data));
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