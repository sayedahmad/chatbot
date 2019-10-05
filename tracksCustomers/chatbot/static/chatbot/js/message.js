


let counter=0;
let questionLength=0;


function loadQuestion(count){
  var token = '{{csrf_token}}';
  $.ajax({
    type:'POST',
    headers: { "X-CSRFToken": token },
    url: "/chatbot/question/",
    data:{
      count: count
      },
    success: function(result){
        
        incoming_message(result['question'])
        questionLength=result['counter']
    
  }});

};



// $(document).ready(loadQuestion(counter))


// Display incoming and outgoing message

function incoming_message(data){
  $(".msg_history").append(`  <div class="incoming_msg">
        <div class="incoming_msg_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="bot"> </div>
        <div class="received_msg">
          <div class="received_withd_msg">
            <p>`+data+`</p>
            <span class="time_date"></span></div>
        </div>
      </div>

          `)
}


function outgoing_message(data){
  $(".msg_history").append(`

  <div class="outgoing_msg">
    <div class="sent_msg">
      <p>`+data+`</p>
      <span class="time_date">  </div>
  </div>
  
  `)


  $("#write_msg").val('');
  $(".msg_history").animate({
      scrollTop:$(".msg_history")[0].scrollHeight
  },"slow")
}



// 1. get input for the first question via click or enter

function get_input(){
  var message =  $("#write_msg").val();
  if(counter<questionLength){
  send_input_to_server(message,counter)
  outgoing_message(message)
}
if(counter==questionLength){
    
    send_input_to_server(message,counter)
    counter++
    
}
   
 

 
}



// 2.validate function send the input to python gets python reply if the reply is valid proceed to the next step else loop on the same feild

function validate(is_valid,feedback){

  // if valide load next question
  if(is_valid){
    counter++
    loadQuestion(counter)
      
  }

  // else loop untill we get the right answer

  else{

    incoming_message(feedback);
  }
}


function send_input_to_server(input_data,count){
  
  var token = '{{csrf_token}}';
   $.ajax({
    type:'POST',
    headers: { "X-CSRFToken": token },
    url: "/chatbot/store/",
    data:{
      count: count,
      message:input_data,
      },
    success: function(result){
      if (result){
        validate(false,result)
      
      }
      else{
         validate(true);
         if (count==1){
          window.brand=input_data;
        }
      }
  }});
  
}



$('#write_msg').keypress(function(){
if(event.which==13){
  
    get_input();
    

 
}
});



$('#msg_send_btn').click(get_input, loadQuestion(counter));

