const searchText=document.querySelector("#searchText");
const tableOutput=document.querySelector(".table-output");
const paginationContainer=document.querySelector(".pagination-container");
const appTable=document.querySelector(".app-table");
const tableBody=document.querySelector(".table-body");
const notFound=document.querySelector(".not-found");


searchText.addEventListener('keyup',(e)=>{

        const search=e.target.value;
        console.log("Value",search);

        if(search.trim().length > 0){
            paginationContainer.style.display="none";
            tableBody.innerHTML="";

            fetch("/search-expenses/",{
            body:JSON.stringify({ searchText:search }),
            method:"POST",
            }).then((res)=>res.json())
            .then((data) =>{
            console.log('Data',data);

            appTable.style.display="none";
            tableOutput.style.display="block";

            if(data.length === 0){

            console.log('length',0);
            notFound.style.display="block";
            tableOutput.style.display="none";

            }else{
                console.log('length',data.length);
                notFound.style.display="none";

                data.forEach(item=>{

tableBody.innerHTML+='<tr><td>'+item.amount+'</td><td>'+item.category+'</td><td>'+item.description+'</td><td>'+item.date+'</td></tr>';

                });

            }

          });

        }else{

            tableOutput.style.display="none";
            notFound.style.display="none";
            paginationContainer.style.display="block";
            appTable.style.display="block";
        }

 });