$(document).ready(function(){

    if(xyz_data != "")
        load3Dmodel($("#molBox"), xyz_data);

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
