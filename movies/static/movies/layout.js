document.addEventListener("DOMContentLoaded", function (){



    const search = document.querySelector('#search');


    //Set's the value of the input field
    var url = new URL(window.location.href);
    var search_params = url.searchParams; 
    search_value = search_params.get('q');
    search.value = search_value

    console.log(search_value)

    

    search.addEventListener("keypress", function(event) {
        
        if (event.key === "Enter") {
         
          event.preventDefault();

        search_value = search.value
          var url = new URL(window.location.href);
          var search_params = url.searchParams;        
          search_params.set('q', search_value);
          url.search = search_params.toString();        
          var new_url = url.toString();           
          window.location = new_url; 
          
        }
      });

})