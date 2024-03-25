using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.EntityFrameworkCore;
using KodeShop.DataLayer.Contexts;

namespace KodeShop.Infrustructure.Utilities.Extensions.Connection
{
    public static class ConnectionExtension
    {

        // Adds and configs database cotext to project.
        public static IServiceCollection RegisterDbContext(this IServiceCollection service, IConfiguration configuration)
        {
            service.AddDbContext<MainDatabaseContext>(options =>
            {
                var connectonString = "ConnectionStrings:KodeShopConnection:" + "Development"; //for now
                options.UseSqlServer(configuration[connectonString]);
            });
            return service;
        }
    }
}
