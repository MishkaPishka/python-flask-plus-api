 function hello() {
    return "Hello";
}

function get_val_from_get_tweet_by_name() {
    return $("#tweet_by_name_input").val()
}


function get_val_from_classify_tweet_input() {
    return $('#tweetToClassify').val()

}





function get_val_from_tweet_classification_user_feedback_radio_buttons() {
        return $('input[name=result_feedback]:checked').val()

}


function get_tweet_feedback_entire_data() {
    return {'tweet':'some tweet','classification':'some classification','feedbak':'some feedback'}
}

