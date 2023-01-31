
document.addEventListener("DOMContentLoaded", function(){
   
    const rating = document.querySelector('#rating');
    const release_year = document.querySelector('#release_year');
    const genre_select = document.querySelector('#genre');

    document.getElementById("genrebutton").onclick = function() {set_genre()};
    document.getElementById("release_year").onclick = function() {sort("release_year")};
    document.getElementById("rating").onclick = function() {sort("rating")};

    
    const previous_button = document.getElementById("previous");
    const next_button = document.getElementById("next");
    

    if(next_button){
        
        document.getElementById("next").onclick = function(){next_page()};
        console.log(next_button.dataset.page)
    }
    if (previous_button){
        document.getElementById("previous").onclick = function(){previous_page()};
    }
    

    function next_page(){   
            
            var url = new URL(window.location.href);
            var search_params = url.searchParams;        
            search_params.set('page', next_button.dataset.page);
            url.search = search_params.toString();        
            var new_url = url.toString();      
            window.location = new_url;          
    }

    
    function previous_page(){             
     
            
        var url = new URL(window.location.href);
        var search_params = url.searchParams;        
        search_params.set('page', previous_button.dataset.page);
        url.search = search_params.toString();        
        var new_url = url.toString();           
       
        window.location = new_url;  
    
    

}
    


    function set_genre(){        
        
            var url = new URL(window.location.href);
            var search_params = url.searchParams;        
            search_params.set('genre', genre_select.value);
            url.search = search_params.toString();        
            var new_url = url.toString();           
            window.location = new_url;                       
    }

    function sort(sort){
        
   
            if(sort == "rating" && rating.dataset.on == "enabled"){
                remove()
            }
            else if(sort == "release_year" && release_year.dataset.on == "enabled"){
               remove()
            }

            else{
                var url = new URL(window.location.href);
                var search_params = url.searchParams;        
                search_params.set('sort', sort);
                url.search = search_params.toString();        
                var new_url = url.toString();           
                window.location = new_url;    
            }
        
        }
    
    function search(search){

        var url = new URL(window.location.href);
        var search_params = url.searchParams;        
        search_params.set('q', search);
        url.search = search_params.toString();        
        var new_url = url.toString();           
        window.location = new_url; 

    }

})


function remove(){
    var url = new URL(window.location.href);
    var search_params = url.searchParams;        
    search_params.delete('sort');
    url.search = search_params.toString();        
    var new_url = url.toString();           
    window.location = new_url;  

}




