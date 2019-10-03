


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
      $(".msg_history").append(`  <div class="incoming_msg">
        <div class="incoming_msg_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
        <div class="received_msg">
          <div class="received_withd_msg">
            <p>${result['question']}</p>
            <span class="time_date"> 11:01 AM    |    Today</span></div>
        </div>
      </div>

          `)
       
        questionLength=result['counter']
    
  }});

};


function storeMessage(inputMessage,count){
  
  var token = '{{csrf_token}}';
  let callbackdata= $.ajax({
    type:'POST',
    headers: { "X-CSRFToken": token },
    url: "/chatbot/store/",
    data:{
      count: count,
      message:inputMessage
      },
    success: function(result){
      if (result){
        validate(true)
      }
      else validate(false)
  }});
  
}


// $(document).ready(loadQuestion(counter))

function validate(boolean){
  if (boolean){
    console.log(true)
  }
  else console.log(false)
}

var sendStoreData=function(){
    var message =  $("#write_msg").val();
    let store=storeMessage(message,counter)
    if(store){
      console.log("wrong input")
    }
    else console
    
    $(".msg_history").append(`

    <div class="outgoing_msg">
      <div class="sent_msg">
        <p>${message}</p>
        <span class="time_date"> 11:01 AM    |    Today</span> </div>
    </div>
    
    `)


    $("#write_msg").val('');
    $(".msg_history").animate({
        scrollTop:$(".msg_history")[0].scrollHeight
    },"slow")

    counter=counter+1;
}



// 1. get input for the first question via click or enter


// 2.validate function send the input to python gets python reply if the reply is valid proceed to the next step else loop on the same feild




// 3. load the next question












$('#write_msg').keypress(function(){
if(event.which==13){
  if(counter<questionLength){
  sendStoreData();
  loadQuestion(counter);
  }
 
  else if( counter==questionLength){
     sendStoreData();

     $(".msg_history").append(`  <div class="incoming_msg">
     <div class="incoming_msg_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
     <div class="received_msg">
       <div class="received_withd_msg time_date">
          
         <span class="time_date">Thank you for the participation</span></div>
     </div>
   </div>
 
       `)
   }
 
}
});

$('#msg_send_btn').click(sendStoreData, loadQuestion(counter));

