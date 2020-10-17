
urlstring='https://alternate-energy.herokuapp.com/readData'

Plotly.d3.json(urlstring, function(err, rows){
  //console.log(rows)
  function unpack(rows, key) {
    
  return rows.map(function(row) { return row[key]; });
}

var source = unpack(rows, 'source')
console.log(source)
var parents = unpack(rows, 'continent')
console.log(parents)
var country1 = unpack(rows, 'country')
console.log(country1)
var values = unpack(rows, 'TWh_Unit')
console.log(values)

//var data = [
//  {
//    type: "sunburst",
//    maxdepth: 5,
//    ids: country1,
//    labels: parents,
//    parents: ["Biofuel",'Wind'],
//    values: values 
//  }
//];

//var layout = {
//  margin: {l: 0, r: 0, b: 0, t: 0},
//  width: 500,
//  height: 500
//};
var trace = {
  x: source,
  y: values,
  type: "bar"
};

// Create the data array for the plot
var data = [trace];

// Define the plot layout
var layout = {
  title: "Source vs TerraWattHour",
  xaxis: { title: "Alternative Source" },
  yaxis: { title: "Terra Watt" }
};

// Plot the chart to a div tag with id "bar-plot"
var trace1 = {
  x: country1,
  y: values,
  type: "bar"
};

// Create the data array for the plot
var data1 = [trace1];

// Define the plot layout
var layout1 = {
  title: "Country vs TerraWattHour",
  xaxis: { title: "Country" },
  yaxis: { title: "Terra Watt" }
};

Plotly.newPlot('plot', data, layout);

Plotly.newPlot('plot2', data1, layout1)

})
