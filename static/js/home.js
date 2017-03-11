$("#logFileForm").submit(function(e){
    e.preventDefault();
});

$("#logFileSubmit").click(function(){
    result_box = document.getElementById("resultBox");
    result_box.innerHTML = "Loading . . .";
    var data = new FormData();
    data.append('logtype', document.getElementById("logFileType").value);
    file = document.getElementById('logFileInput').files[0];
    data.append('file', file);
    xhr = new XMLHttpRequest();
    xhr.open('POST', "http://localhost:5000/upload", true);
    xhr.send(data);
    xhr.onreadystatechange = function(ev){
        if (xhr.readyState == 4 && xhr.status == 200) {
            d = JSON.parse(xhr.responseText);
            if(d["success"]==false)
            {
                result_box.innerHTML = "Oops! Parsing error or unsupported format";
            }
            else
            {
                s = "";
                for(var key in d["data"])
                {
                    s += "<strong>" + key + " : " + "</strong>" + d["data"][key].toString() + "<br>";
                }
                result_box.innerHTML = s;
            }
            $("#resultBox").addClass('success');
        }
    };
});
