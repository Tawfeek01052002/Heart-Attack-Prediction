

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var age = document.getElementById("uiage");
  var sex = document.getElementById("uisex");
  var cp = document.getElementById("uicp");
  var trestbps = document.getElementById("uitrest");
  var chol = document.getElementById("uichol");
  var fbs = document.getElementById("uifbs");
  var restecg = document.getElementById("uirest");
  var thalach = document.getElementById("uithalach");
  var exang = document.getElementById("uiexang");
  var oldpeak = document.getElementById("uioldpeak");
  var slope = document.getElementById("uislope");
  var ca = document.getElementById("uica");
  var thal = document.getElementById("uithal");
  var estPrice = document.getElementById("uiEstimatedPrice");


  // var url = "http://127.0.0.1:5000/predict_home_price"; Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/predict_value"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      age: parseInt(age.value),
      sex: parseInt(sex.value),
      cp: parseInt(cp.value),
      trestbps: parseInt(trestbps.value),
      chol :parseInt(chol.value)
      fbs:parseInt(fbs.value),
      restecg:parseInt(restecg.value),
      thalach :parseInt(thalach.value),
      exang :parseInt(exang.value),
      oldpeak :parseFloat(oldpeak.value),
      slope :parseInt(slope.value),
      ca : parseInt(ca.value),
      thal : parseInt(thal.value)
// 63,0,0,124,197,0 ,1 ,136 ,1  ,0.0 ,1 ,0 ,2
  },function(data, status) {
      console.log(data.estimated_value);
      estPrice.innerHTML = "<h2>" + 10 + " Lakh</h2>";
      console.log(status);
  });
}


