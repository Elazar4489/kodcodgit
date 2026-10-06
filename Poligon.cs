using System.Text.Json;

public interface IGeographicClassificationService
{
    string ClassifyRegion(double lat, double lon);
}

public class GeographicClassificationService : IGeographicClassificationService
{
    // משתנה ששומר את הפוליגונים בזיכרון לאחר טעינה חד-פעמית
    private readonly Dictionary<string, List<(double Lon, double Lat)>> _polygons = new();

    public GeographicClassificationService(string geoJsonFilePath)
    {
        LoadGeoJson(geoJsonFilePath);
    }

    private void LoadGeoJson(string filePath)
    {
        if (!File.Exists(filePath))
            throw new FileNotFoundException($"GeoJSON file not found at: {filePath}");

        string jsonContent = File.ReadAllText(filePath);
        var geoJson = JsonSerializer.Deserialize<GeoJsonFeatureCollection>(jsonContent);

        if (geoJson?.Features == null) return;

        foreach (var feature in geoJson.Features)
        {
            string regionName = feature.Properties.Region; // NORTH, CENTER, SOUTH[span_0](start_span)[span_0](end_span)
            
            // לוקחים את טבעת הפוליגון הראשונה
            if (feature.Geometry.Coordinates.Count > 0)
            {
                var ring = feature.Geometry.Coordinates[0];
                var points = ring.Select(coord => (Lon: coord[0], Lat: coord[1])).ToList();
                _polygons[regionName] = points;
            }
        }
    }

    public string ClassifyRegion(double lat, double lon)
    {
        // עוברים על כל אזור (צפון, מרכז, דרום)
        foreach (var polygon in _polygons)
        {
            if (IsPointInPolygon(lon, lat, polygon.Value))
            {
                return polygon.Key; // מחזיר NORTH, CENTER או SOUTH[span_1](start_span)[span_1](end_span)
            }
        }

        // אם לא נמצא באף פוליגון – מוגדר כפיקוד העומק (OVERSEAS)[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span)
        return "DEPTH"; 
    }

    /// <summary>
    /// אלגוריתם Ray Casting לבדיקה האם הנקודה נמצאת בתוך הפוליגון
    /// </summary>
    private bool IsPointInPolygon(double testLon, double testLat, List<(double Lon, double Lat)> polygon)
    {
        bool inside = false;
        int j = polygon.Count - 1;

        for (int i = 0; i < polygon.Count; j = i++)
        {
            double xi = polygon[i].Lon, yi = polygon[i].Lat;
            double xj = polygon[j].Lon, yj = polygon[j].Lat;

            bool intersect = ((yi > testLat) != (yj > testLat)) &&
                             (testLon < (xj - xi) * (testLat - yi) / (yj - yi) + xi);
            if (intersect)
                inside = !inside;
        }

        return inside;
    }
}
using System.Text.Json.Serialization;

public class GeoJsonFeatureCollection
{
    [JsonPropertyName("features")]
    public List<Feature> Features { get; set; } = new();
}

public class Feature
{
    [JsonPropertyName("properties")]
    public Properties Properties { get; set; } = new();

    [JsonPropertyName("geometry")]
    public Geometry Geometry { get; set; } = new();
}

public class Properties
{
    [JsonPropertyName("region")]
    public string Region { get; set; } = string.Empty;
}

public class Geometry
{
    [JsonPropertyName("coordinates")]
    public List<List<List<double>>> Coordinates { get; set; } = new();
}
