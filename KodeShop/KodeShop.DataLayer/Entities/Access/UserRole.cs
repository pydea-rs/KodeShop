using KodeShop.DataLayer.Entities.Common;
using KodeShop.DataLayer.Entities.Account;

namespace KodeShop.DataLayer.Entities.Access
{
    public class UserRole : BaseEntity
    {
        #region Properties
        public long UserId { get; set; }

        public long RoleId { get; set; }
        #endregion

        #region Relations
        public User User { get; set; }

        public Role Role { get; set; }
        #endregion
    }
}
