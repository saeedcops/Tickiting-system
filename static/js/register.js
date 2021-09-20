const usernameField=document.querySelector('#usernameField');
const emailField=document.querySelector('#emailField');
const invalidFeedBack=document.querySelector(".invalid-feedback");
const emailFeedBack=document.querySelector(".email");
const successEmail=document.querySelector(".successEmail");
const successUsername=document.querySelector(".successUsername");
const passwordToggle=document.querySelector("#showpasswordtoggle");
const passwordField=document.querySelector("#passwordField");
const submitBtn=document.querySelector(".submit-btn");


const handleToggle=(e)=>{

    if(passwordToggle.textContent==="SHOW"){
        passwordToggle.textContent="HIDE";
        passwordField.type="text";
    }else{
        passwordToggle.textContent="SHOW";
         passwordField.type="password";
    }

};

passwordToggle.addEventListener('click',handleToggle)

usernameField.addEventListener('keyup',(e)=>{


        const usernameValue=e.target.value;

        if(usernameValue.length>0){

        fetch("/auth/validate/",{
            body:JSON.stringify({username:usernameValue}),
            method:"POST",
        }).then((res)=>res.json())
          .then((data) =>{
            console.log('Data',data);
            if(data.username_error){
                successUsername.style.display="none";
                usernameField.classList.add("is-invalid");
                invalidFeedBack.style.display="block";
                invalidFeedBack.innerHTML='<p>'+data.username_error+'</p>';
//                submitBtn.addAttribute("disabled");
                submitBtn.disabled=true;
            }else if(data.username_valid){

                usernameField.classList.remove("is-invalid");
                invalidFeedBack.style.display="none";
                successUsername.style.display="block";
                successUsername. innerHTML ="ok";
                submitBtn.disabled=false;

            }else{

                usernameField.classList.remove("is-invalid");
                invalidFeedBack.style.display="none";
                submitBtn.disabled=false;

            }

          });
        }
});

emailField.addEventListener('keyup',(e)=>{


        const emailValue=e.target.value;

        if(emailValue.length>0){

        fetch("/auth/validate-email/",{
            body:JSON.stringify({email:emailValue}),
            method:"POST",
        }).then((res)=>res.json())
          .then((data) =>{
            console.log('Data',data);
            if(data.email_error){
                successEmail.style.display="none";
                emailField.classList.add("is-invalid");
                emailFeedBack.style.display="block";
                emailFeedBack.innerHTML='<p>'+data.email_error+'</p>';
                submitBtn.disabled=true;

            }else if(data.email_valid){

                emailField.classList.remove("is-invalid");
                emailFeedBack.style.display="none";
                successEmail.style.display="block";
                successEmail. innerHTML ="ok";
                submitBtn.disabled=false;

            }else{

                emailField.classList.remove("is-invalid");
                emailFeedBack.style.display="none";
                submitBtn.disabled=false;

            }

          });
        }
});