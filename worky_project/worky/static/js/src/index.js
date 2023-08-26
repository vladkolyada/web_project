const textarea = document.getElementById('expandingTextarea');
const stickyButton = document.getElementById('send_button');
const endBlock = document.getElementsByClassName('end_block');

textarea.addEventListener('input', () => {
  stickyButton.style.top = textarea.scrollHeight - textarea.clientHeight + 'px';
  endBlock.style.top = textarea.scrollHeight - textarea.clientHeight + 'px';
});
