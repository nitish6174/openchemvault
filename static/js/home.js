$("#logFileForm").submit(function(e){
    e.preventDefault();
});

$("#logFileSubmit").click(function(){
    var data = new FormData();
    data.append('logtype', document.getElementById("logFileType").value);
    file = document.getElementById('logFileInput').files[0];
    data.append('file', file);
    xhr = new XMLHttpRequest();
    xhr.open('POST', "http://localhost:5000/upload", true);
    xhr.send(data);
    xhr.onreadystatechange = function(ev){
        if (xhr.readyState == 4 && xhr.status == 200) {
            result_box = document.getElementById("resultBox");
            result_box.innerHTML = xhr.responseText;
        }
    };
});
