using SecureAPI.Middleware;

var builder = WebApplication.CreateBuilder(args);

// Add services
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();


// 🔐 Read Environment Variable
string password = Environment.GetEnvironmentVariable("DB_PASSWORD");
Console.WriteLine("Database Password: " + password);


var app = builder.Build();


// Production error hide
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/error");
}


// Global Exception Middleware
app.UseMiddleware<ExceptionMiddleware>();


// HTTPS Redirection
app.UseHttpsRedirection();


// Authorization
app.UseAuthorization();


// Map Controllers
app.MapControllers();


// Run Application
app.Run();