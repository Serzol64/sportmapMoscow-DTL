using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;

namespace frontend.Pages
{
    public class AnalyticModel : PageModel
    {
        private readonly ILogger<AnalyticModel> _logger;


        public AnalyticModel(ILogger<AnalyticModel> logger)
        {
            _logger = logger;


        }

        public void OnGet()
        {

        }

    }
}
