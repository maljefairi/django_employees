
// get all read-more links
var readMoreLinks = document.querySelectorAll('.read-more');

// for each read-more link
readMoreLinks.forEach(function(link) {

  // get the corresponding full text element
  var fullText = link.parentElement.querySelector('.full');

  // get the corresponding truncated text element
  var truncatedText = link.parentElement.querySelector('.truncated');

  // add click event listener to the read-more link
  link.addEventListener('click', function(e) {
    e.preventDefault();

    // hide the read-more link
    link.style.display = 'none';

    // show the full text
    fullText.style.display = 'inline';

    // create a new reduce-text link
    var reduceTextLink = document.createElement('a');
    reduceTextLink.href = '';
    reduceTextLink.className = 'reduce-text text-primary fst-italic text-decoration-underline';
    reduceTextLink.innerHTML = ' read less';
    reduceTextLink.dataset.item = link.dataset.item;

    // add click event listener to the reduce-text link
    reduceTextLink.addEventListener('click', function(e) {
      e.preventDefault();

      // hide the full text
      fullText.style.display = 'none';

      // show the truncated text
      truncatedText.style.display = 'inline';

      // remove the reduce-text link
      reduceTextLink.remove();

      // show the read-more link again
      link.style.display = 'inline';
    });

    // hide the truncated text
    truncatedText.style.display = 'none';

    // insert the reduce-text link after the full text
    fullText.insertAdjacentElement('afterend', reduceTextLink);
  });
});
