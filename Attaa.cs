using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace WeatherKafkaService;

public class WeatherBackgroundService : BackgroundService
{
    private readonly ILogger<WeatherBackgroundService> _logger;

    private readonly WeatherFileWatcher _fileWatcher;
    private readonly AlertProcessor _alertProcessor;
    private readonly KafkaProducer _kafkaProducer;

    public WeatherBackgroundService(
        ILogger<WeatherBackgroundService> logger)
    {
        _logger = logger;

        // יצירת כל השירותים שהמערכת צריכה
        _kafkaProducer = new KafkaProducer();
        _alertProcessor = new AlertProcessor(_kafkaProducer);
        _fileWatcher = new WeatherFileWatcher(_alertProcessor);
    }

    protected override async Task ExecuteAsync(
        CancellationToken stoppingToken)
    {
        _logger.LogInformation(
            "Weather Background Service started.");

        try
        {
            // מתחילים להאזין לתיקיות
            _fileWatcher.Start();
            _fileWatcher.Start();

            var alert = await _alertProcessor.ProcessAsync(path);

            await _kafkaProducer.SendAsync(alert);
            _logger.LogInformation(
                "Weather File Watcher started.");

            // משאירים את השירות רץ
            await Task.Delay(
                Timeout.Infinite,
                stoppingToken);
        }
        catch (OperationCanceledException)
        {
            _logger.LogInformation(
                "Weather Background Service is stopping.");
        }
        catch (Exception ex)
        {
            _logger.LogError(
                ex,
                "Fatal error in Weather Background Service.");
        }
        finally
        {
            // עצירת ה-Watcher
            _fileWatcher.Stop();

            // סגירת Kafka
            await _kafkaProducer.DisposeAsync();

            _logger.LogInformation(
                "Weather Background Service stopped.");
        }
    }
}
:::

ואז `Program.cs` נהיה פשוט מאוד:

:::writing{variant="document" id="31857" title="Program.cs"}
```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = Host.CreateApplicationBuilder(args);

builder.Services.AddHostedService<WeatherBackgroundService>();

var app = builder.Build();

app.Run();
