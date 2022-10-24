/* ===================================================================
    Author          : ModinaTheme
    Template Name   : Freebuild - Construction HTML Template
    Version         : 1.0
* ================================================================= */

(function($) {
    "use strict";

    $(document).on('ready', function() {

    /*==================================
     # SLide Item Carousel 
     ==================================*/
    $('.hero-slide-active').owlCarousel({
        items: 1,
        autoplay: true,
        loop: true,
        margin: 0,
        nav: false,
        dots: false,
    });

    /*==================================
     # home page one - slide Item Carousel 
     ==================================*/
    $('.hero-slides, .hero-slider').owlCarousel({
        items: 1,
        autoplay: true,
        loop: true,
        margin: 0,
        nav: false,
        dots: false,
    });

    /*==================================
     # Portfolio Item Carousel 
     ==================================*/
    $('.portfolio-carousel-items').owlCarousel({
        autoplay: true,
        loop: true,
        margin: 0,
        nav: false,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            500: {
                items: 1
            },
            700: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    });

    /*==================================
     # Blog Box Item Carousel 
     ==================================*/
    $('.blog-carousel-items').owlCarousel({
        autoplay: false,
        loop: true,
        margin: 30,
        nav: true,
        dots: false,
        navText: ['<i class="fal fa-long-arrow-left"></i>', '<i class="fal fa-long-arrow-right"></i>'],
        responsive: {
            0: {
                items: 1
            },
            500: {
                items: 1
            },
            700: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    });


    /* =============================================
        # Magnific popup init
     ===============================================*/
    $(".popup-link").magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        },
        // other options
    });

    $(".popup-gallery").magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        },
        // other options
    });

    $(".popup-video, .popup-vimeo, .popup-gmaps").magnificPopup({
        type: "iframe",
        mainClass: "mfp-fade",
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

    var wow = new WOW(
        {
            mobile: false,
        }
    )
    wow.init();



      /*==========================================
         Isotop & imagesloaded js initail
        ===========================================*/    
        $('#container').imagesLoaded( function() {
                
            $('.portfolio-filter-buttons').on( 'click', 'button', function() {
              var filterValue = $(this).attr('data-filter');
              $grid.isotope({ filter: filterValue });
            });

            var $grid = $('.portfolio-grid-items').isotope({
              itemSelector: '.grid-item',
              percentPosition: true,
              masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: '.grid-item'
              }
            })

        });

    /*==================================
     # meanmenu active - mobile menu 
     ==================================*/
    $('#responsive-menu').meanmenu({
        meanMenuContainer: '.responsive-menu',
        meanScreenWidth: "992"
    });

    /*==========================
       Count up init
    ============================*/
    $('.single-countup span').counterUp({
        delay: 20,
        time: 2000
    });

    /*==========================
       Scroll To Up init
    ============================*/
    $.scrollUp({
      scrollName: 'scrollUp', // Element ID
      topDistance: '1110', // Distance from top before showing element (px)
      topSpeed: 2000, // Speed back to top (ms)
      animation: 'slide', // Fade, slide, none
      animationInSpeed: 300, // Animation in speed (ms)
      animationOutSpeed: 300, // Animation out speed (ms)
      scrollText: '<i class="fal fa-angle-up"></i>', // Text for element
      activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
    });

    // Preloading
    $(window).on('load', function() {
        // Animate loader off screen
        $(".pre-loader").delay(500).fadeOut();
    });

    //# Smooth Scroll
    $('#responsive-menu a').on('click', function(event) {
        var $anchor = $(this);
        var headerH = '80';
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - headerH + "px"
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
    // sticky nav Scroll
    // sticky nav Scroll
    $("#sticky-nav").sticky({
        topSpacing: 0,
        zIndex: 99999999
    });


    }); // end document ready function
})(jQuery); // End jQuery

