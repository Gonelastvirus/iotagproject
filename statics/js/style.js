if (window.location.pathname === '/dashboard/') {
  console.log("hello")
  const url = new URL('ws://127.0.0.1:8000/dashboard');
  const searchParams = new URLSearchParams(url.search);
  searchParams.append('token',token);
  url.search = searchParams.toString();
  let socket =new WebSocket(url);
  socket.onopen =function(e){
    alert('Connection open');
  };
  socket.onmessage = function(e){
    console.log(e.data);
    let threshold = ((800 / 1024) * 100).toFixed(2);
    document.getElementById("doggy").innerHTML =threshold;
    var recData=JSON.parse(e.data); //parse json data
    var x=Number(recData.node)
    if(x){
      document.getElementById("nodes"+recData.node).innerHTML ='<i class="fas fa-circle text-success"></i>';
    }
    var temp=Number(recData.temp)
      document.getElementById("sex").innerHTML =recData.value;
      document.getElementById("node"+recData.node+"time").innerHTML =recData.time;
      if (recData.value>threshold){
        document.getElementById("moisalt").innerHTML ='<i class="bi bi-arrow-down-circle-fill text-danger"></i>'; 
      }
      else{
        document.getElementById("moisalt").innerHTML ='<i class="bi bi-arrow-up-circle-fill text-success"></i>';
      }
      if (temp>50){
      document.getElementById("node"+recData.node).innerHTML ='<strong class="text-danger">'+temp+'</strong>';
      document.getElementById("tempalt").innerHTML ='<i class="bi bi-arrow-down-circle-fill text-danger"></i>'; 
      }
      else{
        document.getElementById("node"+recData.node).innerHTML ='<strong class="text-success">'+temp+'</strong>';
        document.getElementById("tempalt").innerHTML ='<i class="bi bi-arrow-up-circle-fill text-success"></i>';
      }
      dataObjNew=dataObj['data']['datasets'][x-1]['data'];//dataobjnew is created
      dataObjNew.shift(); // switch to the the new value
      dataObjNew.push(recData.value);//push receive value
      dataObj['data']['datasets'][x-1]['data']=dataObjNew;// update js code entry with rec data object
      window.myLine.update();//update graph without reloading
      let percentage = ((recData.value / 1024) * 100).toFixed(2);
      progresschart.updateSeries([percentage]); 
      tempchart.updateSeries([temp]);   
};

socket.onclose = function(e){
    alert('Connection CLosed');
};
var dataObj={
  type: 'line',
  data: {
      labels: [1,2,3,4,5,6],
      datasets: [{
          label: 'Node1',
          borderColor:'red',
          data: [0,50,45,65,80,100],
          fill: true,
      },
      {
          label: 'Node 2',
          borderColor:'blue',
          data: [0,80,65,90,60,80],
          fill: true,
      },
      {
          label: 'Node 3',
          borderColor:'green',
          data: [0,35,65,35,40,60],
          fill: true,
      },
      {
          label: 'Node 4',
          borderColor:'yellow',
          data: [0,40,65,70,10,100],
          fill: true,
      },
      {
          label: 'Node 5',
          borderColor:'black',
          data: [0,20,60,80,70,110],
          fill: true,
      }
      ]
      },
      options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: false
                  }
              }]
          }
      }
  }
  var ctx = document.getElementById('myChart').getContext('2d');
  window.myLine = new Chart(ctx,dataObj );



  const tabs = document.querySelectorAll('.nav-link');
  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      tabs.forEach(tab => tab.classList.remove('active'));
      this.classList.add('active');
    });
  });
  


  function closeNav() {
    document.getElementById("sidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }
  

  /* Progress Chart*/
var options1 = {
  chart: {
    height: 350,
    type: "radialBar",
  },

  series: [69],
  colors: ["#20E647"],
  plotOptions: {
    radialBar: {
      hollow: {
        margin: 0,
        size: "70%",
        background: "#293450"
      },
      track: {
        dropShadow: {
          enabled: true,
          top: 2,
          left: 0,
          blur: 4,
          opacity: 0.15
        }
      },
      dataLabels: {
        name: {
          offsetY: -10,
          color: "#fff",
          fontSize: "13px"
        },
        value: {
          color: "#fff",
          fontSize: "30px",
          show: true
        }
      }
    }
  },
  fill: {
    type: "gradient",
    gradient: {
      shade: "dark",
      type: "vertical",
      gradientToColors: ["#87D4F9"],
      stops: [0, 100]
    }
  },
  stroke: {
    lineCap: "round"
  },
  labels: ["Soil Moisture"]
};
var progresschart = new ApexCharts(document.querySelector("#progress_chart"), options1);
progresschart.render();
/* Progress Chart */

/* Temperature Details */
var options2 = {
  chart: {
    height: 330,
    type: "radialBar",
  },
  series: [70],
  colors: ["#20E647"],
  plotOptions: {
    radialBar: {
      startAngle: -135,
      endAngle: 135,
      track: {
        background: '#333',
        startAngle: -135,
        endAngle: 135,
      },
      dataLabels: {
        name: {
          show: true,
          fontSize: "50px",
          offsetY:100,
        },
        value: {
          fontSize: "35px",
          show: true,
          formatter: function(val) {
            return val + "°C";
          }
        }
      }
    }
  },
  fill: {
    type: "gradient",
    gradient: {
      shade: "dark",
      type: "horizontal",
      gradientToColors: ["#87D4F9"],
      stops: [0, 100]
    }
  },
  stroke: {
    lineCap: "butt"
  },
  labels: ["🌡"]
};

var tempchart =new ApexCharts(document.querySelector("#myDiv"), options2)
tempchart.render();

/* Temperature Details */
}

if (window.location.pathname === '/settings/') {
    document.getElementById("idusername").setAttribute("disabled","");
    document.getElementById("idemail").setAttribute("disabled","");
    document.getElementById("idtoken").setAttribute("disabled","");
  document.getElementById("editEmail").addEventListener("click", function() {
    document.getElementById("idemail").removeAttribute("disabled");
  });
  
  document.getElementById("editToken").addEventListener("click", function() {
    document.getElementById("idtoken").removeAttribute("disabled");
  });
  }
/* update form */
if (window.location.pathname === '/settings/') {
pass;
}
