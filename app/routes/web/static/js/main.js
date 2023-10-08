(function($) {
  'use strict';

  /*-------------------------------------------------------------------------------
  Preloader
	-------------------------------------------------------------------------------*/
  $(window).on('load', function() {
    $('.acr-preloader').addClass('hidden');
  });

  /*-------------------------------------------------------------------------------
  Aside Menu
	-------------------------------------------------------------------------------*/
  $(".aside-trigger").on('click', function() {
    $(".main-aside").toggleClass('open');
    $("body").toggleClass('aside-open');
  });
  $(".main-aside .menu-item-has-children > a").on('click', function(e) {

    e.preventDefault();

    var submenu = $(this).next(".submenu");

    if($(this).parent().hasClass('active')){
      submenu.slideUp(200);
      $(this).parent().siblings().find('.submenu').slideUp(200);
      $(this).parent().removeClass('active');
    }else{
      $(this).closest('ul').find(".menu-item-has-children").find('.submenu').slideUp(200);
      $(this).closest('ul').find(".menu-item-has-children").removeClass('active');
      $(this).parent().addClass('active');
      submenu.slideDown(200);
    }

  });

  /*-------------------------------------------------------------------------------
  Sticky Header
	-------------------------------------------------------------------------------*/
  var header = $(".can-sticky");
  var headerHeight = header.innerHeight();

  function doSticky() {
    if (window.pageYOffset > headerHeight) {
      header.addClass("sticky");
    } else {
      header.removeClass("sticky");
    }
  }
  doSticky();

  /*-------------------------------------------------------------------------------
  Header (Style 2)
  -------------------------------------------------------------------------------*/

  // Search Category
  $(".cat-selc").on("click", ".init", function () {
    $(this).closest(".cat-selc").children('.cat-selc li:not(.init)').toggleClass("animatedcat");
    $(this).closest(".cat-selc").children('.cat-selc li.init').toggleClass("arrowh3");
  });
  var allOptions = $(".cat-selc").children('li:not(.init)');
  $(".cat-selc").on("click", "li:not(.init)", function () {
    allOptions.removeClass('selected');
    $(this).addClass('selected');
    $(".cat-selc").children('.init').html($(this).html());
    allOptions.toggleClass("animatedcat");
    $(this).closest(".cat-selc").children('.cat-selc li.init').removeClass("arrowh3");
  });
  $(document).on("click", function (event) {
    var $trigger = $(".cat-selc");
    if ($trigger !== event.target && !$trigger.has(event.target).length) {
      $(".animatedcat").removeClass("animatedcat");
      $(".cat-selc li.init").removeClass("arrowh3");
    }
  });

  // Desktop Nav
  $("#open-nav").click(function () {
    $("#mySidenav").css("width", "500px");
  });
  $("#close-nav").click(function () {
    $("#mySidenav").css("width", "0%");
  });
  // Mobile Nav
  $("#mobile-open-nav").click(function () {
    $("#mobile-mySidenav").css("width", "100%");
  });
  $("#mobile-close-nav").click(function () {
    $("#mobile-mySidenav").css("width", "0%");
  });
  $('.dropdown-menu li>a').append('<span></span>');
  $('.megamenu .menu-style>ul>li a').append('<span></span>');

  $('.nav-tabs-menu>li').mouseover( function(){
      $(this).find('a').click();
    });
    $('.nav-tabs-menu>li').mouseout( function(){
      $(this).find('a').click();
    });

    // side nav 
  $(document).ready(function () {
    $('.mobile-nav .sidenav li.custom-dropdown-nav>a').on('click', function () {
      $(this).removeAttr('href');
      var element = $(this).parent('li');
      if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('li').removeClass('open');
        element.find('ul').slideUp();
      } else {
        element.addClass('open');
        element.children('ul').slideDown();
        element.siblings('li').children('ul').slideUp();
        element.siblings('li').removeClass('open');
        element.siblings('li').find('li').removeClass('open');
        element.siblings('li').find('ul').slideUp();
      }
    });
    $('.mobile-nav .sidenav li.custom-dropdown-nav>a').append('<span class="arrow"></span>');
  });

  // Search bar
  $("#search-btn").click(function () {
    $("#main-sec").hide();
    $("#show-search").show();
  });
  $("#close").click(function () {
    $("#show-search").hide();
    $("#main-sec").show();
  });


  /*-------------------------------------------------------------------------------
  Filters Scroll
  -------------------------------------------------------------------------------*/
  $('.listing-main-wrapper').niceScroll({
    cursorcolor:"#dcdcdc",
    cursorwidth:"5px"
  });

  /*-------------------------------------------------------------------------------
  Banner Slider (Home v1)
  -------------------------------------------------------------------------------*/
  $(".banner-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    dots: false,
    fade: true,
    prevArrow: $('.banner .slider-prev'),
    nextArrow: $('.banner .slider-next'),
  });

  /*-------------------------------------------------------------------------------
  Banner Slider (Home v1)
  -------------------------------------------------------------------------------*/
  $(".listing-banner-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    dots: false,
    prevArrow: $('.listing-banner-inner .slider-prev'),
    nextArrow: $('.listing-banner-inner .slider-next'),
  });

  /*-------------------------------------------------------------------------------
  Banner featured slider (Home v2)
  -------------------------------------------------------------------------------*/
  $(".banner-featured-slider").slick({
    slidesToShow: 2,
    slidesToScroll: 2,
    arrows: false,
    dots: true,
    autoplay: true,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });

  /*-------------------------------------------------------------------------------
  Listing Slider
  -------------------------------------------------------------------------------*/
  $(".listings-slider").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    prevArrow: $('.listings .slider-prev'),
    nextArrow: $('.listings .slider-next'),
    dots: false,
    responsive: [
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
        }
      }
    ]
  });

  /*-------------------------------------------------------------------------------
  Top Jobs Slider (Home v1)
  -------------------------------------------------------------------------------*/
  $(".top-listings-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    dots: false,
    autoplay: true,
    prevArrow: $('.top-listings .slider-prev'),
    nextArrow: $('.top-listings .slider-next'),
    responsive: [
      {
        breakpoint: 991,
        settings: {
          arrows: false,
        }
      },
    ]
  });

  /*-------------------------------------------------------------------------------
  Clients Slider
  -------------------------------------------------------------------------------*/
  $(".clients-slider").slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    arrows: false,
    dots: false,
    autoplay: true,
    responsive: [
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 4,
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 3,
        }
      },
      {
        breakpoint: 575,
        settings: {
          slidesToShow: 2,
        }
      },
    ]
  });

  /*-------------------------------------------------------------------------------
  Agents Slider
  -------------------------------------------------------------------------------*/
  $(".agents-slider").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    prevArrow: $('.agents .slider-prev'),
    nextArrow: $('.agents .slider-next'),
    dots: false,
    responsive: [
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
        }
      }
    ]
  });


  /*-------------------------------------------------------------------------------
  Coming Soon & Login Sliders
  -------------------------------------------------------------------------------*/
  $(".acr-cs-bg-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    autoplay: true,
    dots: true,
  });

  /*-------------------------------------------------------------------------------
  Listing Gallery Sliders (Listing details v2)
  -------------------------------------------------------------------------------*/
  $('.listing-thumbnail-slider-main').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.listing-thumbnail-slider-nav'
  });
  $('.listing-thumbnail-slider-nav').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    asNavFor: '.listing-thumbnail-slider-main',
    dots: false,
    centerMode: false,
    focusOnSelect: true,
    autoplay: true,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
        }
      },
    ]
  });

  /*-------------------------------------------------------------------------------
  Sidebar filter collapse (Listing grid and list)
  -------------------------------------------------------------------------------*/
  $(".acr-collapse-trigger").on('click', function(){
    $(this).next().slideToggle(200);
  });

  /*-------------------------------------------------------------------------------
  Trigger advanced Search
  -------------------------------------------------------------------------------*/
  $(".advanced-search-trigger").on('click', function(){
    $(".advanced-search").slideToggle(200);
    $(this).toggleClass('active');
  });

  /*-------------------------------------------------------------------------------
  Trigger listing filter
  -------------------------------------------------------------------------------*/
  $(".filter-trigger").on('click', function(){
    $(".acr-filter-form").slideToggle(300);
  });

  /*-------------------------------------------------------------------------------
  Select2
  -------------------------------------------------------------------------------*/
  $('.acr-select2').select2({
    allowClear: false
  });

  /*-------------------------------------------------------------------------------
  Tooltips
  -------------------------------------------------------------------------------*/
  $('[data-toggle="tooltip"]').tooltip();

  /*-------------------------------------------------------------------------------
  Load More Features (Listing Details)
  -------------------------------------------------------------------------------*/
  $(".load-more-features").on('click', function(){
    $(this).hide(0);
    $(".hidden-listing-features").slideDown();
  });

  /*-------------------------------------------------------------------------------
  Magnific Popup
  -------------------------------------------------------------------------------*/
  $('.popup-youtube').magnificPopup({
    type: 'iframe'
  });
  $('.popup-vimeo').magnificPopup({
    type: 'iframe'
  });
  $('.popup-video').magnificPopup({
    type: 'iframe'
  });
  $('.gallery-thumb').magnificPopup({
    type: 'image',
    gallery: {
      enabled: true
    },
  });
  $('.magnific-gallery').magnificPopup({
    delegate: 'a', 
    type: 'image',
    removalDelay: 300,
    easing: 'ease-in-out',
    mainClass: 'mfp-fade',
    gallery:{
        enabled: true
    }
    
    });

  /*-------------------------------------------------------------------------------
  Masonry
  -------------------------------------------------------------------------------*/
  $('.masonry').imagesLoaded(function() {
    var isotopeContainer = $('.masonry');
    isotopeContainer.isotope({
      itemSelector: '.masonry-item',
    });
  });

  /*-------------------------------------------------------------------------------
  Submit listing Gallery Upload
  -------------------------------------------------------------------------------*/
  if($("#acrListingGallery").length){
    // This prevents using the class 'dropzone' which will conflict with new instances of DropZone created programatically
    // Set this to true, or delete if you want to create an instance of Dropzone without having to write any code:
    // More info here: https://www.dropzonejs.com/#configuration
    Dropzone.autoDiscover = false;
    $("#acrListingGallery").dropzone({

      paramName: "file",
      maxFiles: 5,
      maxFilesize: 5,
      addRemoveLinks: true,
      acceptedFiles: "image/*,application/pdf,.psd",
    });
  }

  //On scroll events
  $(window).on('scroll', function() {

    doSticky();

  });

})(jQuery);
