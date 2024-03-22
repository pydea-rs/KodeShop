using System;
using System.Collections.Generic;
using System.Text;
using KodeShop.DataLayer.Entities.Common;
using KodeShop.DataLayer.Entities.Access;
using System.ComponentModel.DataAnnotations;

namespace KodeShop.DataLayer.Entities.Account
{
    public class User : BaseEntity
    {
        #region Properties

        [Display(Name = "نام کاربری")]
        [Required(ErrorMessage = "لطفا {0} خود را وارد کنید.")]
        [MaxLength(32, ErrorMessage = "طول '{0}' شما نباید بیشتر از {1} کاراکتر باشد.")]
        [MinLength(3, ErrorMessage = "طول '{0}' شما نباید کمتر از {1} کاراکتر باشد.")]
        public string Username { get; set; }
        [Display(Name = "رمزعبور")]
        [Required(ErrorMessage = "لطفا {0} خود را وارد کنید.")]
        [MaxLength(16, ErrorMessage = "طول '{0}' شما نباید بیشتر از {1} کاراکتر باشد.")]
        [MinLength(6, ErrorMessage = "طول '{0}' شما نباید کمتر از {1} کاراکتر باشد.")]
        public string Password { get; set; }

        // these four fields must be wrapped around Profile entity later
        [Display(Name = "نام")]
        [Required(ErrorMessage = "لطفا {0} خود را وارد کنید.")]
        [MaxLength(16, ErrorMessage = "طول '{0}' شما نباید بیشتر از {1} کاراکتر باشد.")]
        [MinLength(6, ErrorMessage = "طول '{0}'شما نباید کمتر از {1} کاراکتر باشد.")]
        public string Fullname { get; set; }
        [Display(Name = "استان")]
        [Required(ErrorMessage = "لطفا نام {0} خود را وارد کنید.")]
        [MaxLength(32, ErrorMessage = "طول '{0}' شما نباید بیشتر از {1} کاراکتر باشد.")]
        [MinLength(2, ErrorMessage = "طول '{0}'شما نباید کمتر از {1} کاراکتر باشد.")]
        public string Province { get; set; }

        [Display(Name = "شهر")]
        [Required(ErrorMessage = "لطفا نام {0} خود را وارد کنید.")]
        [MaxLength(32, ErrorMessage = "طول '{0}' شما نباید بیشتر از {1} کاراکتر باشد.")]
        [MinLength(2, ErrorMessage = "طول '{0}'شما نباید کمتر از {1} کاراکتر باشد.")]
        public string City { get; set; }

        [Display(Name = "آدرس محل سکونت")]
        [Required(ErrorMessage = "لطفا {0} خود را وارد کنید.")]
        [MaxLength(64, ErrorMessage = "طول '{0}' شما نباید بیشتر از {1} کاراکتر باشد.")]
        [MinLength(5, ErrorMessage = "طول '{0}'شما نباید کمتر از {1} کاراکتر باشد.")]
        public string Address { get; set; }

        [Display(Name = "شماره موبایل")]
        [Required(ErrorMessage = "لطفا {0} خود را وارد کنید.")]
        [MaxLength(14, ErrorMessage = "لطفا یک {0} معتبر وارد نمایید.")]
        [MinLength(11, ErrorMessage = "طول '{0}'شما نباید کمتر از {1} کاراکتر باشد.")]
        public string Phonenumber { get; set; }

        [Display(Name = "کد 6 رقمی")]
        [Required(ErrorMessage = "لطفا {0} خود را وارد کنید.")]
        [StringLength(6, ErrorMessage = "لطفا یک {0} معتبر وارد نمایید.")]

        public string VerificationCode { get; set; }

        public bool IsActivated { get; set; }
        #endregion


        #region Relations
        public ICollection<UserRole> UserRoles { get; set; }
        #endregion
    }
}
