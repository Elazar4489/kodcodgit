using MondayExercise;
using System;
namespace MondayExercise
{
    class Program
    {
        static void Main()
        {
            List<Platform> platforms = new List<Platform>();
            Platform a = new AirPlatform(1, 500, 70, 1200);
            Platform b = new AirPlatform(2, 500, 160, 7000);
            Platform c = new SeaPlatform(3, 80, 230, 59);
            Platform d = new SeaPlatform(4, 90, 290, 34);
            Platform e = new GroundPlatform(5, 110, 20, "strit");
            Platform f = new GroundPlatform(6, 110, 20, "tunnel");
            platforms.Add(a); platforms.Add(b); platforms.Add(c); platforms.Add(d); platforms.Add(e); platforms.Add(f);
            foreach (Platform once in platforms)
            {
                Console.WriteLine($"{once.StatusLine()} and its state is {once.IsTrackable()}");
            }
        }
    }
    abstract class Platform
    {
        protected int _trackId { get; }
        private double _speedKnots;
        private double _heading;
        
        public double Heading
        {
            get => _heading;
            set
            {
                if (Heading < 0 || Heading > 359) _heading = 0.0;
                else _heading = value;
            }
        }
        public double SpeedKnots
        {
            get => _speedKnots;
            set
            {
                if (SpeedKnots < 0) _speedKnots = 0.0;
                else _speedKnots = value;
            }
        }
        protected Platform(int trackId, double speedKnots, double heading)
        {
            _trackId = trackId;
            SpeedKnots = speedKnots;
            Heading = heading;
        }
        public override string ToString()
        {
            return $"{_trackId}, {SpeedKnots}, {Heading}";
        }
        public abstract string StatusLine();
        public abstract bool IsTrackable();
    }

    class AirPlatform : Platform
    {
        private double _altitudeFeet;
        public double AltitudeFeet
        {
            get => _altitudeFeet;
            set
            {
                _altitudeFeet = value;
            }
        }
        public AirPlatform(int trackId, double speedKnots, double heading, double altitudeFeet)
            : base(trackId, speedKnots, heading) => AltitudeFeet = altitudeFeet;
        public override bool IsTrackable()
        {
            if (SpeedKnots > 0 && AltitudeFeet >= 100 && AltitudeFeet <= 6000)
            {
                return true;
            }
            return false;
        }
        public override string StatusLine()
        {
            return $"Track {_trackId} with a speed of {SpeedKnots} km/h is at a {Heading} degree heading and at an altitude of {AltitudeFeet} feet";
        }
    }
    class SeaPlatform : Platform
    {
        private double _depthMeters;
        public double DepthMeters
        {
            get => _depthMeters;
            set
            {
                _depthMeters = value;
            }
        }
        public SeaPlatform(int trackId, double speedKnots, double heading, double depthMeters)
            : base(trackId, speedKnots, heading) => DepthMeters = depthMeters;
        public override bool IsTrackable()
        {
            if (DepthMeters >= 0 && DepthMeters <= 300)
            {
                return true;
            }
            return false;
        }
        public override string StatusLine()
        {
            return $"Track {_trackId} with a speed of {SpeedKnots} km/h is at a {Heading} degree heading and at a depth of {DepthMeters} meters";
        }
    }
    class GroundPlatform : Platform
    {
        private string _terrainType;
        public string TerrainType
        {
            get => _terrainType;
            set
            {
                _terrainType = value;
            }
        }
        public GroundPlatform(int trackId, double speedKnots, double heading, string terrainType)
            : base(trackId, speedKnots, heading) => TerrainType = terrainType;
        public override bool IsTrackable()
        {
            if (TerrainType != "tunnel")
            {
                return true;
            }
            return false;
        }
        public override string StatusLine()
        {
            return $"Track {_trackId} with a speed of {SpeedKnots} km/h is at a {Heading} degree heading and on Terrain type {TerrainType}";
        }
    }
}
