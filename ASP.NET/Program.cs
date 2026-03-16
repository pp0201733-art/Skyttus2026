var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

builder.Services.AddSingleton<EmailService>();
builder.Services.AddSingleton<SmsService>();

builder.Services.AddHostedService<BackgroundNotificationService>();

var app = builder.Build();

app.MapControllers();

app.Run();