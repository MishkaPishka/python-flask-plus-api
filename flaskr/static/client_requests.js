function get_tweet_by_username(username) {
    return new Promise((resolve,reject)=> {
        $.ajax("/twitter-classification/get-tweet-by-username/"+username)
         .done(function(res) {
             resolve(res['data'])

          })
          .fail(function(err) {
            reject(err );
          })
    })
}


function get_tweet_classification(tweet) {
    return new Promise((resolve,reject)=> {
        $.ajax("/twitter-classification/classification-request/"+tweet)
         .done(function(res) {
            resolve(res['data'])

          })
          .fail(function(err) {
            reject(err );
          })
    })
}


function set_feedback_on_tweet_classification(feedback_data) {
    return new Promise((resolve,reject)=> {
        $.post("/twitter-classification/give-feedback-on-tweet-classification/",{feedback_data})
         .done(function(res) {
            resolve(res['data'])
          })
          .fail(function(err) {
            reject(err );
          })
    })
}

function send_feedback_request(data) {
    return new Promise((resolve,reject)=> {
     $.post("/text-gen/rank",{data})
         .done(function(res) {
            resolve(res['data'])
          })
          .fail(function(err) {
            reject(err.responseText );
          })
    })


}

function delete_history_request() {
    return new Promise((resolve,reject) => {
       $.post("/user/delete_history")
         .done(function(res) {
            resolve(res['data'])
          })
          .fail(function(err) {
            reject(err );
          })
    })
}