$(document).ready(function(){

    var controller = new ScrollMagic.Controller();

    var ourScene1 = new ScrollMagic.Scene({
        triggerElement: '.fade-in1',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in1', 'show1')
    .addTo(controller);

    var ourScene2 = new ScrollMagic.Scene({
        triggerElement: '.fade-in2',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in2', 'show2')
    .addTo(controller);

    var ourScene3 = new ScrollMagic.Scene({
        triggerElement: '.fade-in3',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in3', 'show3')
    .addTo(controller);

    var ourScene3 = new ScrollMagic.Scene({
        triggerElement: '.fade-int1',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-int1', 'showt1')
    .addTo(controller);

    var ourScene3 = new ScrollMagic.Scene({
        triggerElement: '.fade-int2',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-int2', 'showt2')
    .addTo(controller);



    var ourScene3 = new ScrollMagic.Scene({
        triggerElement: '.fade-in1t',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in1t', 'show1t')
    .addTo(controller);

    var ourScene3 = new ScrollMagic.Scene({
        triggerElement: '.fade-in2t',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in2t', 'show2t')
    .addTo(controller);

    var ourScene3 = new ScrollMagic.Scene({
        triggerElement: '.fade-in3t',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in3t', 'show3t')
    .addTo(controller);

    var ourScene3 = new ScrollMagic.Scene({
        triggerElement: '.fade-in-block',
        triggerHook: 0.9,
    })
    .setClassToggle('.fade-in-block', 'show-block')
    .addTo(controller);

})