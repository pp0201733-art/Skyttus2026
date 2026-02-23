using DemoConfigApp.Services;
using DemoConfigApp.Middleware;

var builder = WebApplication.CreateBuilder(args);

// Controllers
builder.Services.AddControllers();

// ✅ Register Custom Service (DI)
builder.Services.AddScoped<IMyService, MyService>();

var app = builder.Build();

// ✅ Use Custom Middleware
app.UseMiddleware<RequestLoggingMiddleware>();

app.MapControllers();

app.Run();
