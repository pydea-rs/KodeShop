using System;
using KodeShop.DataLayer.Entities.Common;
using System.Linq;
using System.Threading.Tasks;

namespace KodeShop.DataLayer.Repositories
{
    public interface IGenericRepository<TEntity> : IDisposable where TEntity : BaseEntity
    {
        IQueryable<TEntity> EntitiesQuery { get; }

        Task<TEntity> GetById(long id);

        Task Add(TEntity item);

        Task Update(TEntity item);

        Task Remove(TEntity item);

        Task Remove(long id);

        Task Save();

    }
}
