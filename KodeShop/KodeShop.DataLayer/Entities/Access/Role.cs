using System;
using System.Collections.Generic;
using System.Text;
using KodeShop.DataLayer.Entities.Common;
using System.ComponentModel.DataAnnotations;

namespace KodeShop.DataLayer.Entities.Access
{
    public class Role : BaseEntity
    {
        #region Properties
        [Display(Name = "مشخصه نقش")]
        [Required(ErrorMessage = "لطفا {0} را و.ارد کنید.")]
        [MinLength(4, ErrorMessage = "حداقل طول {0} باید {1} کاراکتر باشد.")]
        [MaxLength(16, ErrorMessage = "حداکثر طول {0} باید {1} کاراکتر باشد.")]
        public string Name { get; set; }

        [Display(Name = "عنوان نقش")]
        [Required(ErrorMessage = "لطفا {0} را و.ارد کنید.")]
        [MinLength(4, ErrorMessage = "حداقل طول {0} باید {1} کاراکتر باشد.")]
        [MaxLength(32, ErrorMessage = "حداکثر طول {0} باید {1} کاراکتر باشد.")]
        public string Title { get; set; }

        #endregion

        #region Properties
        public ICollection<UserRole> UserRoles { get; set; }
        #endregion
    }
}
