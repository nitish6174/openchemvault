$(function() {
    let element = $('#molBox');
    let config = { backgroundColor: '#fcfcfc' };
    let viewer = $3Dmol.createViewer(element,config);

    // let data_file = 'http://files.rcsb.org/view/1mbs.pdb';
    // let data_file = 'http://3dmol.csb.pitt.edu/tests/test_structs/big.xyz';
    // let data_file = 'http://localhost:5000/data/BaHfO3.xyz';
    let data_file = 'http://localhost:5000/data/benzene.xyz';
    
    let file_type = data_file.substr(data_file.length-3);
    loadFile(viewer,data_file,file_type);
});

function loadFile(viewer,data_file,file_type)
{
    jQuery.ajax( data_file, { 
        success: function(data) {
            let v = viewer;
            v.addModel(data,file_type);
            viewer.setStyle({},{
                // cartoon : {},
                sphere  : {scale:0.3},
                stick   : {}
            });
            v.zoomTo();
            v.render();
            v.zoom(1.0, 1000);
        },
        error: function(hdr, status, err) {
            console.error( "Failed to load file " + data_file + ": " + err );
        },
    });
}
