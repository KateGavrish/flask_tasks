// Activate Carousel
$("#arouselExampleIndicators").carousel();

// Enable Carousel Indicators
$(".item").click(function(){
$("#carouselExampleIndicators").carousel(1);
});

// Enable Carousel Controls
$(".left").click(function(){
$("#carouselExampleIndicators").carousel("prev");
});