$(document).ready(function(){

    $("#searchForm").submit(function(e){
        e.preventDefault();

        // var result_msg = document.getElementById("resultMsg");
        // var result_box = document.getElementById("resultBox");
        // var progress_bar = document.getElementById("progressBar");
        // result_msg.innerHTML = "Loading . . .";
        // result_box.innerHTML = "";

        var query_type = $("#searchForm input[name='query-type']").val();
        var query_text = $("#searchForm input[name='query-text']").val();

        // $.post("/api/search", {
        //     query_type: query_type,
        //     query_text: query_text
        // }, function(data, status){
        //     if(data["success"]!=true)
        //     {
        //         var msg = "Oops! Something went wrong";
        //         result_msg.innerHTML = msg;
        //     }
        //     else
        //     {
        //         console.log(data["results"]);
        //         result_msg.innerHTML = "See result in console";
        //         // result_box.innerHTML = result_box_text;
        //     }
        //     progress_bar.classList.remove("success");
        //     void progress_bar.offsetWidth;
        //     progress_bar.classList.add("success");
        // });

        // window.location.url = "/search/type="+query_type+":query="+query_text;

    });

});
