var ctx = document.getElementById('myChart').getContext('2d');

const renderChar=(label,data)=>{

var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: label,
        datasets: [{
            label: '# of Votes',
            data: data,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
            display:true,
            text:"Expenses Summary",
        }
    }
});

};

const getChartData=()=>{

    fetch("/summary_status-expenses/",{
            method:"GET",
            }).then((res)=>res.json())
            .then((result) =>{
            console.log('Data',result);

            const [label,data]=[Object.keys(result),Object.values(result),];

            renderChar(label,data);
          });

};

document.onload = getChartData();
