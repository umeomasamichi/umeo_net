
var $slider_container = $('.slider-container'),
    $slider = $('.slider'),
    $slider_nav_container = $('.slider-nav-container'),
    $slider_nav = $('.slider-nav');

// ナビゲーション用に複製
$slider_nav.append($slider.contents().clone());

$slider.on('init', function(){
  $slider_container.addClass('initialized');
});

$slider_nav.on('init', function(){
  $slider_nav_container.addClass('initialized');
});

$slider.slick({
  centerMode: false,
  arrows: false,
  //dots: true,
  pauseOnFocus: false,
  pauseOnHover: true,
  pauseOnDotsHover: true,
  asNavFor: $slider_nav,
  waitForAnimate: false,
  fade:true,
});

$slider_nav.slick({
  arrows: true,
  appendArrows: $slider_nav_container,
  //Arrowを付けるとクリックしても動かない．．．．．．
  prevArrow: '<button type="button" class="slick-prev slider-arrow">次</button>',
  nextArrow: '<i class="slider-arrow slider-next fa fa-angle-right"></i>',
  slidesToShow: 3,
  asNavFor: $slider,
  focusOnSelect: true,
  centerMode: true,
  centerPadding: '40px',
  autoplay: true,
  autoplaySpeed: 5000,
});


/*
$slider_nav.on('setPosition', function(){
  var slider_width = $slider_nav.width(),
      slide_gutter = $slider_nav.find('.slick-slide').eq(0).css('margin-right').split('px')[0],
      slides_num = $slider_nav.slick('slickGetOption', 'slidesToShow'),
      slides_center_padding = $slider_nav.slick('slickGetOption', 'centerPadding').split('px')[0],
      slide_width = (slider_width - slide_gutter * (slides_num - 1) - (slides_center_padding * 2)) / slides_num;
  $slider_nav.find('.slick-slide').css('width', slide_width + 'px');
});
*/

$(function() {
	$("#typed").typed({
		strings: ["テキストが入ります。", "<strong>テキスト</strong>が入ります。<br>テキストが入ります。"],
		typeSpeed: 30,
		startDelay: 0,
		backSpeed: 30,
		backDelay: 500,
		loop: false,
		cursorChar: "|",
		contentType: 'html'
	});
});