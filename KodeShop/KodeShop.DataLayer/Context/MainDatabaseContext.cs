using System.Linq;
using Microsoft.EntityFrameworkCore;
using KodeShop.DataLayer.Entities.Account;
using KodeShop.DataLayer.Entities.Access;


namespace KodeShop.DataLayer.Context
{
    public class MainDatabaseContext : DbContext
    {
        #region init
        public MainDatabaseContext(DbContextOptions<MainDatabaseContext> options) : base(options)
        {

        }
        #endregion

        #region Database DbSets [for migration]
        public DbSet<User> Users { get; set; }
        public DbSet<UserRole> UserRoles { get; set; }

        public DbSet<Role> Roles { get; set; }


        #endregion
        #region Disable Cascade delete in database
        // This piece will prevent database from performing on_delete=CASCADE
        // it finds all the items with on_delete=cascade, and changes their on_delete behaviour

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            var cascades = modelBuilder.Model.GetEntityTypes()
                .SelectMany(table => table.GetForeignKeys())
                .Where(foreignKey => foreignKey.IsOwnership && foreignKey.DeleteBehavior == DeleteBehavior.Cascade);

            foreach (var item in cascades)
                item.DeleteBehavior = DeleteBehavior.Restrict;

            base.OnModelCreating(modelBuilder); // do the super method by modified model builder 
        }
        #endregion
    }
}
