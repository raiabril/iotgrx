/*    CUSTOM DROPDOWNS    */

$(function() {
    $(".custom-dropdown-toggler").each(function() {
        $(this).attr("aria-expanded", "false");
    });

    $(".custom-dropdown-menu").each(function() {
        var totalHeight = 0;
        var dropdownMenu =  $(this);
        var dropdownItems = dropdownMenu.children(".dropdown-item");

        for (var i = 0; i < dropdownItems.length; i++) {
            totalHeight += dropdownItems.eq(i).outerHeight();
        }
        dropdownMenu.attr("data-height", totalHeight + 2);
    });
});

$( ".custom-dropdown-toggler" ).click(function() {
    var dropdownMenu = $($(this).attr("data-toggle"));

    if(dropdownMenu.children().length === 0) return;

    if($(this).attr("aria-expanded") === "true") {
        $(this).attr("aria-expanded", "false");
        dropdownMenu.css("height", "0");
    } else {
        $(this).attr("aria-expanded", "true");
        dropdownMenu.css("height", dropdownMenu.attr("data-height"));
    }
});


/*    TIME FILTER    */
var visibleOverflowTimeout;

$("#time-filter").mouseenter(function() {
    visibleOverflowTimeout = setTimeout(function(){
        $("#time-filter").css("overflow", "visible");
    }, 900);
});

$("#time-filter").mouseleave(function() {
    $("#time-filter").css("overflow", "hidden");
    clearTimeout(visibleOverflowTimeout);
});


/*    GENERAL FILTERS    */
$("#general-filters .custom-dropdown").mouseleave(function() {
    var toggler = $(this).children(".custom-dropdown-toggler");
    toggler.attr("aria-expanded", "false");
    $(toggler.attr("data-toggle")).css("height", "0");
});
