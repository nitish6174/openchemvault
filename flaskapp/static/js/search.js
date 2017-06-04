$(document).ready(function(){

    $("#searchForm input.span2").each(function(){
        $(this).slider({});
    });

    $("#searchForm").submit(function(e){
        e.preventDefault();
        search_url = "/search/";
        params = {};
        $("#searchForm input[name^='search-']").each(function(){
            input_name = $(this).attr('name');
            k = input_name.substring(7, input_name.length-6);
            val = $(this).val();
            default_val = "";
            if($(this).hasClass('span2'))
                default_val = $(this).attr("data-slider-min")+","+$(this).attr("data-slider-max");
            if(val!=default_val)
                params[k] = val;
        });
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