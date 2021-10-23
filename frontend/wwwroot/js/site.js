// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

$(document).ready(function(){
	$('.container > main').attr('data-page',document.title);

	// Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Возрастная группа');
        data.addColumn('number', 'Доля');
        data.addRows([
			["7-14", 10.0],
            ["15-30", 45.0],
            ["31-62", 40.0],
            ["63 и более", 31.66]
        ]);

        // Set chart options
        var options = {'width':600,
                       'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('gystodata-age'));
        chart.draw(data, options);
      }
});
