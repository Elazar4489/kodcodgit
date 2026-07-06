using Exercise.ImageMetadata;
using System;
using System.Collections.Generic;
using System.Text;

namespace Exercise.Repositor
{
    public class Repository<T> where T : ImageMetadataManager
    {
        private readonly List<T> values = new List<T>();
        public void Add(T image)
        {
            values.Add(image);
        }
        public int totalScore()
        {
            return values.Sum(image => image.Score());
        }
        public List<T> GetAll()
        {
            return values;
        }
    }
}
