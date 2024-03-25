using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using KodeShop.DataLayer.Entities.Common;
using KodeShop.DataLayer.Contexts;
using Microsoft.EntityFrameworkCore;


namespace KodeShop.DataLayer.Repositories
{
    public class GenericRepository<TEntity> : IGenericRepository<TEntity> where TEntity : BaseEntity
    {
        #region Initialize
        private MainDatabaseContext context;
        private DbSet<TEntity> database;

        public GenericRepository(MainDatabaseContext ctx)
        {
            this.context = ctx;
            this.database = this.context.Set<TEntity>();
        }
        #endregion

        public IQueryable<TEntity> EntitiesQuery => this.database.AsQueryable();

        public async Task Add(TEntity item){
            item.ModifiedAt = item.CreatedAt = DateTime.Now;

            await this.database.AddAsync(item);
        }

        public async Task<TEntity> GetById(long id)
        {
            return await this.database.SingleOrDefaultAsync(existingItem => existingItem.Id == id);
        }

        public Task Remove(TEntity item)
        {
            throw new NotImplementedException();
        }

        public Task Remove(long id)
        {
            throw new NotImplementedException();
        }

        public Task Save()
        {
            throw new NotImplementedException();
        }

        public void Dispose()
        {
            throw new NotImplementedException();
        }
    }
}
