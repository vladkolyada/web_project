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


// Black block variables for animation
const blackBlock = document.querySelector(".black_block");
const topPositionBlackBlock = blackBlock.offsetTop;

const lineBb = document.getElementById("line_bb");
lineBb.style.animationPlayState = "paused";
const smallWordsBb = document.getElementById("small_words_bb");
smallWordsBb.style.animationPlayState = "paused";
const bigWordsBb = document.getElementById("big_words_bb");
bigWordsBb.style.animationPlayState = "paused";


// Portfolio block variables for animation
const portfolioBlock = document.querySelector(".portfolio_block");
const topPositionPortfolioBlock = portfolioBlock.offsetTop;

const line2 = document.getElementById("line2");
line2.style.animationPlayState = "paused";
const smallWords2 = document.getElementById("small_words2");
smallWords2.style.animationPlayState = "paused";
const bigWords2 = document.getElementById("big_words2");
bigWords2.style.animationPlayState = "paused";


// Partners block variables for animation
const partnersBlock = document.querySelector(".partners_block");
const topPositionPartnersBlock = partnersBlock.offsetTop;

const line3 = document.getElementById("line3");
line3.style.animationPlayState = "paused";
const smallWords3 = document.getElementById("small_words3");
smallWords3.style.animationPlayState = "paused";
const bigWords3 = document.getElementById("big_words3");
bigWords3.style.animationPlayState = "paused";


// Get contact block variables for animation
const getContactBlock = document.querySelector(".get_contact_block");
const topPositionGetContactBlock = getContactBlock.offsetTop;

const line4 = document.getElementById("line4");
line4.style.animationPlayState = "paused";
const smallWords4 = document.getElementById("small_words4");
smallWords4.style.animationPlayState = "paused";
const bigWords4 = document.getElementById("big_words4");
bigWords4.style.animationPlayState = "paused";

function activateAnimationOnBlock (elementAnimation, topPositionClassWithElementAnimation) {
  window.addEventListener('scroll', () => {
      if (window.innerHeight + window.scrollY >= topPositionClassWithElementAnimation) {
        return elementAnimation.style.animationPlayState = "running";
    } else {
        return elementAnimation.style.animationPlayState = "paused";
    }
  });
}


activateAnimationOnBlock(line1, topPositionAboutCompanyBlock);
activateAnimationOnBlock(small_words1, topPositionAboutCompanyBlock);
activateAnimationOnBlock(big_words1, topPositionAboutCompanyBlock);

activateAnimationOnBlock(photo1AboutBlockArch, topPositionAboutCompanyBlock);
activateAnimationOnBlock(photo2AboutBlockEngi, topPositionAboutCompanyBlock);
activateAnimationOnBlock(photo3AboutBlockInte, topPositionAboutCompanyBlock);

activateAnimationOnBlock(lineBb, topPositionBlackBlock);
activateAnimationOnBlock(smallWordsBb, topPositionBlackBlock);
activateAnimationOnBlock(bigWordsBb, topPositionBlackBlock);

activateAnimationOnBlock(line2, topPositionPortfolioBlock);
activateAnimationOnBlock(smallWords2, topPositionPortfolioBlock);
activateAnimationOnBlock(bigWords2, topPositionPortfolioBlock);

activateAnimationOnBlock(line3, topPositionPartnersBlock);
activateAnimationOnBlock(smallWords3, topPositionPartnersBlock);
activateAnimationOnBlock(bigWords3, topPositionPartnersBlock);

activateAnimationOnBlock(line4, topPositionGetContactBlock);
activateAnimationOnBlock(smallWords4, topPositionGetContactBlock);
activateAnimationOnBlock(bigWords4, topPositionGetContactBlock);