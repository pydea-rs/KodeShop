using System;
using System.Collections.Generic;
using System.Text;
using System.ComponentModel.DataAnnotations;

namespace KodeShop.DataLayer.Entities.Common
{
    // Parent of all entities, containing all common fields such as id, etc.
    public class BaseEntity
    {
        [Key]
        public long Id { get; set; }
        public bool IsTrash { get; set; }
        public DateTime CreatedAt { get; set; }
        public DateTime ModifiedAt { get; set; }
    }
}
