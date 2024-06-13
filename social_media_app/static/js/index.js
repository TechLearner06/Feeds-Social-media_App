
var tablinks = document.getElementsByClassName("following-links");
var tabcontents = document.getElementsByClassName("following-contents");

function opentab(tabname, event) {
    for (tablink of tablinks) {
        tablink.classList.remove("active-link");
    }
    for (tabcontent of tabcontents) {
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add('active-tab');
}




// like button toggle, count increase
function toggleLike(button) {
    let likeCount = button.nextElementSibling; // Assuming count is the next sibling of the button
    let isLiked = button.classList.toggle('liked');

    // update like count
    likeCount.innerText = isLiked ? parseInt(likeCount.innerText) + 1 : parseInt(likeCount.innerText) - 1;
}



// comment page logic

/*
function toggleComment(button) {
    let commentModal = document.getElementById('commentModal');
    commentModal.style.left = '0';
}

function postComment() {
    let newComment = document.getElementById('commentInput').value;
    let commentsContainer = document.getElementById('commentsContainer');

    // Add the new comment to the comments container
    let commentElement = document.createElement('p');
    commentElement.innerText = newComment;
    commentsContainer.appendChild(commentElement);

    // Clear the input field
    document.getElementById('commentInput').value = '';
}



document.addEventListener('DOMContentLoaded', function () {
    const commentButtons = document.querySelectorAll('.fa-comment');
    const postCommentButton = document.getElementById('postCommentButton');
    const closeCommentButton = document.getElementById('closeCommentButton');

    // Function to toggle the comment modal
    function toggleComment() {
        let commentModal = document.getElementById('commentModal');
        commentModal.style.left = '0';
    }

    // Function to close the comment modal
    function closeComment() {
        let commentModal = document.getElementById('commentModal');
        commentModal.style.left = '-100%';
    }

    // Event listeners
    commentButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            toggleComment();
        });
    });

    closeCommentButton.addEventListener('click', function () {
        closeComment();
    });

    postCommentButton.addEventListener('click', function () {
        postComment();
    });
});

*/
// script.js

function toggleComments() {
    var commentSection = document.getElementById('comment-section');
    commentSection.style.right = (commentSection.style.right === '0px') ? '-300px' : '0px';
}

function addComment() {
    var commentInput = document.getElementById('comment-input');
    var commentsContainer = document.getElementById('comments-container');

    var newComment = commentInput.value.trim();
    
    if (newComment !== '') {
        var commentDiv = document.createElement('div');
        commentDiv.className = 'comment';

        var userInfoDiv = document.createElement('div');
        userInfoDiv.className = 'user-info';

        var userImg = document.createElement('img');
        userImg.src = 'user_dp.jpg'; // Set the actual path to the user's DP
        userImg.alt = 'User DP';

        var usernameSpan = document.createElement('span');
        usernameSpan.className = 'username';
        usernameSpan.innerText = 'Username'; // Set the actual username dynamically

        userInfoDiv.appendChild(userImg);
        userInfoDiv.appendChild(usernameSpan);

        commentDiv.appendChild(userInfoDiv);

        var commentText = document.createElement('p');
        commentText.className = 'comment-text';
        commentText.innerText = newComment;

        commentDiv.appendChild(commentText);

        commentsContainer.appendChild(commentDiv);
        commentInput.value = '';
    }
}
