$(document).ready(function(){

    $("#searchForm").submit(function(e){
        e.preventDefault();
        search_url = "/search/";
        params = {};
        // This list is defined in view_routes.py and search.html also
        keys = [
            "formula"
        ];
        for(x in keys)
        {
            k = keys[x];
            params[k] = $("#searchForm input[name='search-"+k+"-input']").val();
        }
        search_url += search_param(params);
        window.location = search_url;
    });

});


function search_param(param_d)
{
    s = "";
    for(x in param_d)
    {
        s = s + x + "=" + param_d[x] + ":";
    }
    return s.slice(0, -1);
}