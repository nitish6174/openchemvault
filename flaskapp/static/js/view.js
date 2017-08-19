$(document).ready(function(){

    var jsonified_parsed_data = parsed_data.replace(/&#39;/g, '"').replace(/nan/g, "null");
    var parsed_data_dl = "text/json;charset=utf-8," + jsonified_parsed_data;
    $('#dlParsed a').attr("href", "data:" + parsed_data_dl);
    $('#dlParsed a').removeClass("disabled");

    if(xyz_data != "")
    {
        load3Dmodel($("#molBox"), xyz_data);
        var xyz_data_dl = "text;charset=utf-8," + encodeURIComponent(xyz_data);
        $('#dlXYZ a').attr("href", "data:" + xyz_data_dl);
        $('#dlXYZ a').removeClass("disabled");
    }

});

function load3Dmodel(container,data)
{
    let config = { backgroundColor: '#444' };
    let viewer = $3Dmol.createViewer(container,config);
    viewer.addModel(data,'xyz');
    viewer.setStyle({},{
        // cartoon : {},
        sphere  : {scale:0.3},
        stick   : {}
    });
    viewer.zoomTo();
    viewer.render();
    viewer.zoom(1.0, 1000);
}
