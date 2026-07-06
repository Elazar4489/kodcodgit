using Exercise.ImageMetadata;
using Exercise.Repositor;
namespace Exercise.Program
{
    class Program
    {
        static void Main()
        {
            Repository<ImageMetadataManager> repository = new Repository<ImageMetadataManager>();
            Formater formater = new Formater();
            
            repository.Add(new SARImage(1, 70));
            repository.Add(new EOImage(2, 44));
            repository.Add(new IRImage(3, 39.8));
            Console.WriteLine(repository.totalScore());
            foreach (ImageMetadataManager image in repository.GetAll())
            {
                Console.WriteLine($"{formater.Format(image)}");
            }
        }
    }
}