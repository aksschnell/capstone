

document.addEventListener("DOMContentLoaded", function(){        


    document.querySelectorAll(".remove").forEach(button =>{        

        button.onclick = function(){

            //ID of the review
            id = (button.dataset.id).slice(0, -1)

            fetch("/api/reaction",{

                method : "DELETE",
                body : JSON.stringify({
                    review_id : id,
                })


            })
            .then(response => response.json())   
            
            
            const likebutton = document.querySelector('[data-id="' + id + 'l"' + '] '); 
            const dislikebutton = document.querySelector('[data-id="' + id + 'd"' + '] '); 
            const removebutton = document.querySelector('[data-id="' + id + 'r"' + '] ');             

            likebutton.style.display = "block";
            dislikebutton.style.display = "block";
            removebutton.style.display = "none";

            const likes_amount = document.querySelector('[data-id="' + id + 'la"' + '] '); 
            const dislikes_amount = document.querySelector('[data-id="' + id + 'da"' + '] ');  

             if(removebutton.dataset.latest == "l"){
                
                likes_amount.dataset.likes--;
                likes_amount.innerHTML = likes_amount.dataset.likes + " likes";
            }
            else if (removebutton.dataset.latest == "d"){
                dislikes_amount.dataset.dislikes--;
                dislikes_amount.innerHTML = dislikes_amount.dataset.dislikes + " dislikes";
            }

            else if (removebutton.innerHTML = "Remove dislike"){
                dislikes_amount.dataset.dislikes--;
                dislikes_amount.innerHTML = dislikes_amount.dataset.dislikes + " dislikes";
            }

        }


    })

    //DISLIKE BUTTON
    document.querySelectorAll(".dislike").forEach(button =>{

        button.onclick = function(){

            //ID of the review
            id = (button.dataset.id).slice(0, -1)

            fetch("/api/reaction",{
                method : "POST",
                body: JSON.stringify({
                    review_id : id,
                    reaction : 2
                })

            })
            .then(response => response.json())
            

            const dislikes_amount = document.querySelector('[data-id="' + id + 'da"' + '] ');  
            dislikes_amount.dataset.dislikes++;
            dislikes_amount.innerHTML = dislikes_amount.dataset.dislikes + " dislikes"
            const removebutton = document.querySelector('[data-id="' + id + 'r"' + '] ');
            removebutton.dataset.latest = "d";
            update_display(2);

        }

    })


    //LIKE BUTTON
    document.querySelectorAll(".like").forEach(button =>{  
        
        button.onclick = function(){

            //ID of the review
            id = (button.dataset.id).slice(0, -1)              
            
            fetch("/api/reaction", {
                method : "POST",
                body: JSON.stringify({
                    review_id : id,
                    reaction : 1,
                })
        
            })
            .then(response => response.json())    

            //Changes the frontend without reloading
            const likes_amount = document.querySelector('[data-id="' + id + 'la"' + '] ');  
            likes_amount.dataset.likes++;
            likes_amount.innerHTML = likes_amount.dataset.likes + " likes"

            const removebutton = document.querySelector('[data-id="' + id + 'r"' + '] ');
            removebutton.dataset.latest = "l";
            console.log("hej")
            update_display(1);          

        }
    })

    
})


function update_display(reaction_type){

    const likebutton = document.querySelector('[data-id="' + id + 'l"' + '] '); 
    const dislikebutton = document.querySelector('[data-id="' + id + 'd"' + '] '); 
    const removebutton = document.querySelector('[data-id="' + id + 'r"' + '] '); 

    likebutton.style.display = "none";
    dislikebutton.style.display = "none";

    if (reaction_type == 1){
        removebutton.innerHTML = "Remove like";
    }
    else if (reaction_type == 2){
        removebutton.innerHTML = "Remove dislike";
    }

    removebutton.style.display = "block";

}


