$(function() {
const ctx = $("#macro-chart");

var data = {
    datasets: [{
        data: [
            30, 45, 25
        ],
        backgroundColor: [
            "#FF6384",
            "#4BC0C0",
            "#FFCE56"
        ],
        label: 'Macros' // for legend
    }],
    labels: [
        "Protein",
        "Carbs",
        "Fat"
    ]
};

    var macroChart = new Chart(ctx, {
        type: "doughnut", 
        data: data
    });

});