$(document).ready(function(){

    var controller = new ScrollMagic.Controller();

    var ourScene = new ScrollMagic.Scene({
        triggerElement: '.aaaa',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in', 'show')
    .addTo(controller);

})