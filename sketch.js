
//TO ADD
//images are being squished - cropped rather than squish them
//make photogrid responsive
//add the lightbox

//for all the images in the folder
$(document).ready(function(){

    for (i = 1; i <= 100; i++) {

        var img = new Image(); //create a new image
        $(img)
            .attr('src', 'images/' + i + '.jpg')
            .attr('class', 'mirror') //give each image a class ofmirror
            .load(function(){
                $('#container').append( $(this) );
                // Your other custom code
        
                $(this).css( {
                    "height": "250px",
                    "width": "250px",
                    // "padding": "1px",
                    // "padding-bottom":"0px",
                    "margin": "2px 2px 0px 2px",
                    // "margin-bottom":"0px"
                    // "border": "1px solid #333"
                });    
           
            });        
    }

});