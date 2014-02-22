/*
 * Example of how to apply the infinite scroll plugin
 */
 
(function ($) {
    $(function () {
        $('#searchListing').infiniteScroll({
            calculateBottom: function () {
                return ($('.searchListing').position().top + $('.searchListing').height()) - $(window).height() + 50;
            },
            processResults: function (results) {
                $('#number-of-results').text(results.Key);
 
                for (var i = 0; i < results.Value.length; i++) {
                    $('#search-results').append($('<div class="divider"></div>'));
 
                    var result = results.Value[i];
 
                    var el = $('#result-template').find('.item').clone();
                    el.find('#result-url').attr('href', result.Url).html(result.Title);
                    el.find('#result-description').html(result.Description);
                    el.find('.section').html(result.Category);
 
                    $('#search-results').append(el);
                }
            },
            url: $('#searchListing').data('url') + '/GetSearchResults',
            getData: function () {
                return { "query": $('#hidQuery').val() };
            }
        });
    });
} (jQuery));