//var imported = document.createElement('script');
//imported.src = '/static/';
//document.head.appendChild(imported);
//
//var loc = window.location.pathname;
//var dir = loc.substring(0, loc.lastIndexOf('/'));

 console.log ( $(location).attr('href'));
 console.log(  $(location).attr('pathname'))

$.getScript('../static/events_parser.js', function()
{
    $.getScript('../static/client_requests.js', function()
    {

    });
});
      // script is now loaded and executed.
        // put your dependent JS here.

        function clicked_get_tweet_button() {
                //get text
                let text = get_val_from_get_tweet_by_name();
                console.log('text',text)
                if (text == undefined) {
                    return
                }
                get_tweet_by_username(text)
                    .then(value =>{
                        console.log(value)
                        $("#result_text").val(value)
                    })
                    .catch(err => {
                        console.log('err in clicked_get_tweet_button',err)
                                        alert(err['responseText'])


                    })

        }
        //TODO
        function clicked_classify_tweet_button() {
                //get text
                let text = get_val_from_classify_tweet_input();
                console.log('text',text)
                if (text == undefined) {
                    return
                }
                get_tweet_classification(text)
                    .then(value =>{
                        console.log('value',value)
                        $('input[value='+value+'][name=classification_result]').prop('checked',true)
                    })
                    .catch(err => {
                        console.log('err in clicked_classify_tweet_button',err)
                        alert(err['responseText'])
                    })

        }

        //TODO
        //TODO get_val_from_tweet_classification_user_feedback_radio_buttons get_val_from_classify_tweet_input
        function give_feedback_on_tweet_classification() {
                //get text
                let tweet_data = get_tweet_feedback_entire_data();
                console.log('get_val_from_tweet_classification_user_feedback_radio_buttons',tweet_data)
                if (tweet_data == undefined) {
                    alert("Cannot send a request of Empty Text")
                    return
                }
                set_feedback_on_tweet_classification(tweet_data)
                    .then(value =>{
                        console.log(value)
                        $("#result_text").val(value)
                    })
                    .catch(err => {
                        console.log('err in give_feedback_on_tweet_classification',err)
                        alert(err['responseText'])

                    })

        }

        function give_feedback_on_gen_text() {
            let data = get_gen_text_info_with_rank();
            console.log(data);
            send_feedback_request(data)
                .then(data => {
                alert(data)


                })
                .catch(err => {
                alert(err)
                })
        }

        //TODO
        function send_feedback_event(select_id,type) {
            //GET PARAMS
            return {'data':true}
        //    let seed = '';
        //    let output_size = 1;
        //    let method = 'a';
        //    let result = 'b';
        //    feedback = $('#'+select_id).val();
        //    console.log('feedback val:',feedback);
        //    if (type=='text_gen') {
        //     set_feedback_text_generator()
        //        .then(data => {
        //
        //            alert('thank you for you feedback!')
        //        })
        //        .catch(err => {})
        //    }
        //    else {
        //     set_feedback_text_generator()
        //        .then(data => {
        //
        //            alert('thank you for you feedback!')
        //        })
        //        .catch(err => {})
        //    }



        }

        function delete_history() {
            delete_history_request()
                 .then(value =>{
                    console.log(value)
                    alert(value)
                })
                .catch(err => {
                    console.log('err in delete_history',err)
                    alert(err['responseText'])


                })
        }

 console.log ( 'aaaaa');
