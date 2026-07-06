using static System.Net.Mime.MediaTypeNames;

namespace Exercise.ImageMetadata
{
    //enum SensorEnum
    //{
    //    EO,
    //    SAR,
    //    IR
    //}
    public abstract class ImageMetadataManager
    {
        public int Id;
        public double CloudCover;
        Valibator valibator = new Valibator();
        public ImageMetadataManager(int id, double cloudCover)
        {
            Id = id;
            CloudCover = valibator.IsValid(cloudCover);
        }
        abstract public int Score();
    }
    class SARImage : ImageMetadataManager
    {
        public SARImage(int id, double cloudCover) : base(id, cloudCover) { }
        override public int Score()=> 100 - (int)CloudCover;
    }
    class EOImage : ImageMetadataManager
    {
        public EOImage(int id, double cloudCover) : base(id, cloudCover) { }
        override public int Score() => 60 - (int)CloudCover;
    }
    class IRImage : ImageMetadataManager
    {
        public IRImage(int id, double cloudCover) : base(id, cloudCover) { }
        override public int Score() => 40 - (int)CloudCover;
    }
    class Valibator
    {
        public double IsValid(double CloudCover)
        {
            if (CloudCover < 0 || CloudCover > 100)
            {
                throw new ArgumentException("jjj");
            }
            return CloudCover;
        }
    }
    class Formater
    {
        public string Format(ImageMetadataManager image)
        {
            return $"Image {image.Id}: {image.CloudCover}% cloud [{image.GetType().Name}]";
        }
    }
    class Saver
    {
        public void SaveToFile(string path, Formater formater, ImageMetadataManager image)
        {
            string txtt = File.ReadAllText(path);
            if (txtt.Length == 0)
            {
                File.WriteAllText(path, $"{formater.Format(image)}\n");
            }
            else
            {
                File.AppendAllText(path, $"{formater.Format(image)}\n");
            }

        }
    }
    //class Scorer
    //{
    //    public int Score(ImageMetadataManager image)
    //    {
    //        return image.Sensor switch
    //        {
    //            nameof(SensorEnum.SAR) => 100 - (int)image.CloudCover,
    //            nameof(SensorEnum.EO) => 60 - (int)image.CloudCover,
    //            nameof(SensorEnum.IR) => 40 - (int)image.CloudCover,
    //            _ => 0 - (int)image.CloudCover
    //        };
    //    }
    //}
    
 
}