
function get_val_from_get_tweet_by_name() {
    return $("#tweet_by_name_input").val()
}


function get_val_from_classify_tweet_input() {
    return $('#tweetToClassify').val()

}


function get_gen_text_info_with_rank() {

    let seed = $('#seed1').val()
    let charRange = $('#length').val()
    let method = $('#method').val()
    let output = $('#output1').val()
    let ranking = $('#rank-text').val()

    console.log('seed:',seed,' range: ',length,' method: ',method, ' output: ',output,' ranking:' ,ranking)
    return {'seed':seed,'length':charRange,'method':method,'output':output,'ranking':ranking}
}


function get_val_from_tweet_classification_user_feedback_radio_buttons() {
        return $('input[name=result_feedback]:checked').val()

}


function get_tweet_feedback_entire_data() {
    return {'tweet':'some tweet','classification':'some classification','feedbak':'some feedback'}
}

