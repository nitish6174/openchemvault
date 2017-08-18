$(document).ready(function(){

    $("#logFileForm").submit(function(e){
        e.preventDefault();
    });

    $("#logFileSubmit").click(function(){
        var result_msg = document.getElementById("resultMsg");
        var result_box = document.getElementById("resultBox");
        var progress_bar = document.getElementById("progressBar");
        result_msg.innerHTML = "Loading . . .";
        result_box.innerHTML = "";

        var data = new FormData();
        file = document.getElementById('logFileInput').files[0];
        data.append('file', file);

        xhr = new XMLHttpRequest();
        xhr.open('POST', "/api/addfile", true);
        xhr.send(data);
        xhr.onreadystatechange = function(ev){
            if (xhr.readyState==4) {
                if (xhr.status==200) {
                    try {
                        d = JSON.parse(xhr.responseText);
                        if(d["success"]==false)
                        {
                            var msg = "Oops! <br>" + d["message"];
                            result_msg.innerHTML = msg;
                        }
                        else
                        {
                            var msg = "The uploaded file was successfully added to the data repository! <br><br>";
                            msg += "Document Id : " + d["inserted_id"] + " <br>";
                            msg += "Please note the above Id for reference <br><br>";
                            msg += "The added document can be viewed at <a href='/view/" +  d["inserted_id"] + "'>this link</a>";
                            result_msg.innerHTML = msg;
                        }
                    }
                    catch (e)
                    {
                        var msg = "Oops! There was some issue displaying the data from this file";
                        result_msg.innerHTML = msg;
                        console.log(e.message);
                    }
                    progress_bar.classList.remove("success");
                    void progress_bar.offsetWidth;
                    progress_bar.classList.add("success");
                }
                else
                {
                    var msg = "Sorry! Your query could not be completed due to some error";
                    result_msg.innerHTML = msg;
                }
            }
        };
    });

});
