Webcam.set({
    width: 320,
    height: 240,
    image_format: 'jpeg',
    jpeg_quality: 90
 });
 Webcam.attach( '#camera' );


 function take_snapshot(){
     Webcam.snap(function(data_uri){
         document.getElementById('result').innerHTML = '<img src="'+data_uri+'"/>';
     })
 }
 