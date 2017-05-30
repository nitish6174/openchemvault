$(document).ready(function(){

    $("#searchForm").submit(function(e){
        e.preventDefault();

        var query_type = $("#searchForm input[name='query-type']").val();
        var query_text = $("#searchForm input[name='query-text']").val();

        search_url = "/search/type="+query_type+":query="+query_text;
        window.location = search_url;
    });

});
