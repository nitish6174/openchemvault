$(document).ready(function(){

    $("#logFileForm").submit(function(e){
        e.preventDefault();
    });

    $("#logFileSubmit").click(function(){
        var result_msg = document.getElementById("resultMsg");
        var result_box = document.getElementById("resultBox");
        var progress_bar = document.getElementById("progressBar");
        result_msg.innerHTML = "Loading . . .";

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
                    result_msg.innerHTML = "Oops! Parsing error or unsupported format";
                }
                else
                {
                    var result_box_text = "";
                    for(var key in d["data"])
                    {
                        var result_line_val = d["data"][key];
                        var valstring = "";
                        if(key=="formula")
                        {
                            for(var element in result_line_val)
                            {
                                atom_count = result_line_val[element];
                                if(atom_count>1)
                                    valstring += element +  "<sub>"+atom_count.toString()+"</sub>";
                                else
                                    valstring += element
                            }
                        }
                        else
                        {
                            valstring = JSON.stringify(d["data"][key]);
                        }
                        result_box_text += "<div class='accordion-item'>";
                        result_box_text += "<div class='accordion-title' onclick='$(this).next().next().toggle();'>";
                        result_box_text += "<h4><i class='text-muted glyphicon glyphicon-menu-down'></i> "+key+"</h4></div>";
                        result_box_text += "<hr class='hr-no-gap'>";
                        result_box_text += "<div class='accordion-text'>"+valstring+"</div>";
                        result_box_text += "</div>";
                    }
                    result_msg.innerHTML = "Result";
                    result_box.innerHTML = result_box_text;
                }
                progress_bar.classList.remove("success");
                void progress_bar.offsetWidth;
                progress_bar.classList.add("success");
            }
        };
    });

});
