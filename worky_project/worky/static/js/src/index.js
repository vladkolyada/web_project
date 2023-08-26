const textarea = document.getElementById('expandingTextarea');
const stickyButton = document.getElementById('send_button');
const endBlock = document.getElementsByClassName('end_block');

textarea.addEventListener('input', () => {
  stickyButton.style.top = textarea.scrollHeight - textarea.clientHeight + 'px';
  endBlock.style.top = textarea.scrollHeight - textarea.clientHeight + 'px';
});


// About company block variables for animation
const aboutCompanyBlock = document.querySelector(".about_company_block");
const topPositionAboutCompanyBlock = aboutCompanyBlock.offsetTop;

const line1 = document.getElementById("line1");
line1.style.animationPlayState = "paused";
const small_words1 = document.getElementById("small_words1");
small_words1.style.animationPlayState = "paused";
const big_words1 = document.getElementById("big_words1");
big_words1.style.animationPlayState = "paused";

const photo1AboutBlockArch = document.getElementById("photo_1_about_block_arch");
photo1AboutBlockArch.style.animationPlayState = "paused";
const photo2AboutBlockEngi = document.getElementById("photo_2_about_block_engi");
photo2AboutBlockEngi.style.animationPlayState = "paused";
const photo3AboutBlockInte = document.getElementById("photo_3_about_block_inte");
photo3AboutBlockInte.style.animationPlayState = "paused";

function activateAnimationOnBlock (elementAnimation, topPositionClassWithElementAnimation) {
  window.addEventListener('scroll', () => {
      if (window.innerHeight + window.scrollY >= topPositionClassWithElementAnimation) {
        return elementAnimation.style.animationPlayState = "running";
    } 
  });
}


activateAnimationOnBlock(line1, topPositionAboutCompanyBlock);
activateAnimationOnBlock(small_words1, topPositionAboutCompanyBlock);
activateAnimationOnBlock(big_words1, topPositionAboutCompanyBlock);
activateAnimationOnBlock(photo1AboutBlockArch, topPositionAboutCompanyBlock);
activateAnimationOnBlock(photo2AboutBlockEngi, topPositionAboutCompanyBlock);
activateAnimationOnBlock(photo3AboutBlockInte, topPositionAboutCompanyBlock);