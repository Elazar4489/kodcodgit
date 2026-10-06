dotnet add package Serilog.AspNetCore
dotnet add package Serilog.Sinks.Console
dotnet add package Serilog.Sinks.Elasticsearch


// Serilog in beginning the Program.cs

using Serilog;
using Serilog.Sinks.Elasticsearch;

Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Information()
    .WriteTo.Console()
    .WriteTo.Elasticsearch(new ElasticsearchSinkOptions(new Uri("http://localhost:9200"))
    {
        AutoRegisterTemplate = true,
        IndexFormat = "kol-aman-logs-{0:yyyy.MM}" // שם האינדקס שיווצר באלסטיק
    })
    .CreateLogger();

try
{
    Log.Information("Starting the background alert processing service...");
    
    var builder = Host.CreateDefaultBuilder(args);

    // חיבור Serilog ל-Generic Host (מה שמתאים ל-Background Service / Console App)
    builder.UseSerilog();

    builder.ConfigureServices((hostContext, services) =>
    {
        // הזרקת כל הסרביסים שלך לכאן...
        services.AddHostedService<AlertConsumerBackgroundService>();
    });

    var host = builder.Build();
    await host.RunAsync();
}
catch (Exception ex)
{
    Log.Fatal(ex, "Host terminated unexpectedly");
}
finally
{
    Log.CloseAndFlush();
}









הגעת התרעה חדשה מ-Kafka / FileSystem.
זיהוי כפילות ברדיס ונסיגה.
הצלחת ולידציה או נפילה שלה.
שליחה בפועל של התרעה לפיקוד ב-RabbitMQ (עם פירוט לאיזה פיקוד היא נשלחה, בדיוק לפי הדרישה במבחן!).
