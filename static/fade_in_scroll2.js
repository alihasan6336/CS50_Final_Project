$(document).ready(function(){

    var controller = new ScrollMagic.Controller();

    var ourScene = new ScrollMagic.Scene({
        triggerElement: '.fade-in',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in', 'show')
    .addTo(controller);

})